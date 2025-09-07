import os
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, AutoConfig
from torch.distributed import init_process_group, destroy_process_group
from torch.distributed.checkpoint import FileSystemReader, load_state_dict
from torch.distributed.checkpoint.state_dict import get_state_dict, set_state_dict, StateDictOptions
from concurrent.futures import ThreadPoolExecutor
from torch.distributed._tensor import DTensor

# ---- USER INPUTS ----
CKPT_DIR   = "/mnt/task_runtime/CTU-Agent-v0/checkpoints/tau_bench/mcemri_qwen2.5_3b_alldata_sft_v0_retail_grpo_taxonomy_after_sft_v3_20250905_143122/global_step_35/policy"
BASE_MODEL = "Qwen/Qwen2.5-3B-Instruct"                       
OUT_DIR    = "./qwen2p5_3b_rl_export_grpo_taxonomy_v3"                         
DTYPE      = torch.bfloat16                                   
DEVICE     = "cuda" if torch.cuda.is_available() else "cpu"

# If you used LoRA during RL (set to False if you didn't use LoRA):
USE_LORA = False
LORA_R = 16
LORA_ALPHA = 32
LORA_DROPOUT = 0.05
LORA_TARGET_MODULES = ["q_proj","k_proj","v_proj","o_proj","gate_proj","up_proj","down_proj"]

def merge_by_placement(tensors, placement):
    """Merge tensors according to their placement strategy"""
    if placement.is_replicate():
        return tensors[0]
    elif placement.is_shard():
        # Concatenate along the sharded dimension
        return torch.cat(tensors, dim=placement.dim)
    elif placement.is_partial():
        raise NotImplementedError("Partial placement is not supported yet")
    else:
        raise NotImplementedError(f"Unknown placement type: {placement}")

def convert_fsdp_checkpoint_to_hf():
    """Convert FSDP checkpoint to HuggingFace format using SkyRL approach"""
    print("Converting FSDP checkpoint to HuggingFace format...")
    
    # Load tokenizer and config
    print("Loading tokenizer and config...")
    tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL, use_fast=True, trust_remote_code=True)
    config = AutoConfig.from_pretrained(BASE_MODEL, trust_remote_code=True)
    
    # Find all checkpoint files
    checkpoint_files = []
    for filename in os.listdir(CKPT_DIR):
        if filename.startswith("model_world_size_") and filename.endswith(".pt"):
            checkpoint_files.append(filename)
    
    if not checkpoint_files:
        raise FileNotFoundError(f"No FSDP checkpoint files found in {CKPT_DIR}")
    
    # Extract world size from filename
    world_size = int(checkpoint_files[0].split("_")[3])
    print(f"Found FSDP checkpoint with world_size={world_size}")
    
    # Load all shards
    print("Loading checkpoint shards...")
    model_state_dict_lst = [None] * world_size
    
    def load_shard(rank):
        model_path = os.path.join(CKPT_DIR, f'model_world_size_{world_size}_rank_{rank}.pt')
        print(f"Loading shard {rank}: {model_path}")
        state_dict = torch.load(model_path, map_location='cpu', weights_only=False)
        model_state_dict_lst[rank] = state_dict
        return state_dict
    
    # Load first shard to get structure
    model_state_dict_lst[0] = load_shard(0)
    
    # Load remaining shards in parallel
    with ThreadPoolExecutor(max_workers=min(8, os.cpu_count())) as executor:
        futures = []
        for rank in range(1, world_size):
            future = executor.submit(load_shard, rank)
            futures.append(future)
        
        # Wait for all to complete
        for future in futures:
            future.result()
    
    print("Merging sharded parameters...")
    
    # Prepare merged state dict
    merged_state_dict = {}
    param_placements = {}
    
    # Get keys from first shard
    keys = set(model_state_dict_lst[0].keys())
    
    for key in keys:
        print(f"Processing key: {key}")
        tensors_for_key = []
        placements = None
        
        for rank in range(world_size):
            tensor = model_state_dict_lst[rank][key]
            
            if isinstance(tensor, DTensor):
                # Extract local tensor and placement info
                tensors_for_key.append(tensor._local_tensor.to(DTYPE))
                if placements is None:
                    placements = tensor.placements
                else:
                    assert placements == tensor.placements, f"Inconsistent placements for {key}"
            else:
                # Regular tensor, just use first one (should be replicated)
                merged_state_dict[key] = tensor.to(DTYPE)
                break
        
        # If we have DTensor, merge according to placement
        if tensors_for_key and placements is not None:
            if len(placements) == 1:
                # Simple case: single placement
                placement = placements[0]
                merged_tensor = merge_by_placement(tensors_for_key, placement)
                merged_state_dict[key] = merged_tensor
            else:
                # Multiple placements - for now, just concatenate along first sharded dimension
                # This is a simplified approach and may need refinement
                sharded_dims = [i for i, p in enumerate(placements) if p.is_shard()]
                if sharded_dims:
                    # Concatenate along the first sharded dimension
                    dim = placements[sharded_dims[0]].dim
                    merged_tensor = torch.cat(tensors_for_key, dim=dim)
                    merged_state_dict[key] = merged_tensor
                else:
                    # All replicated, just take first
                    merged_state_dict[key] = tensors_for_key[0]
    
    # Clean up loaded shards to free memory
    del model_state_dict_lst
    
    print("Creating HuggingFace model...")
    
    # Create model with meta device to avoid loading weights twice
    with torch.device('meta'):
        model = AutoModelForCausalLM.from_config(config, torch_dtype=DTYPE, trust_remote_code=True)
    
    # Move to CPU and load our merged state dict
    model.to_empty(device='cpu')
    
    print("Loading merged state dict into model...")
    missing_keys, unexpected_keys = model.load_state_dict(merged_state_dict, strict=False)
    
    if missing_keys:
        print(f"Missing keys: {missing_keys[:5]}...")
    if unexpected_keys:
        print(f"Unexpected keys: {unexpected_keys[:5]}...")
    
    print("Successfully loaded checkpoint!")
    
    # Save the model
    print(f"Saving model to: {OUT_DIR}")
    os.makedirs(OUT_DIR, exist_ok=True)
    
    model.save_pretrained(OUT_DIR, safe_serialization=True)
    tokenizer.save_pretrained(OUT_DIR)
    
    print(f"✅ Successfully saved HuggingFace model to: {OUT_DIR}")
    print("You can now load it with:")
    print(f"model = AutoModelForCausalLM.from_pretrained('{OUT_DIR}')")
    print(f"tokenizer = AutoTokenizer.from_pretrained('{OUT_DIR}')")

def main():
    """Main conversion function"""
    print("Starting FSDP checkpoint conversion...")
    try:
        convert_fsdp_checkpoint_to_hf()
    except Exception as e:
        print(f"Error during conversion: {e}")
        print("Traceback:")
        import traceback
        traceback.print_exc()
        raise

if __name__ == "__main__":
    main()
