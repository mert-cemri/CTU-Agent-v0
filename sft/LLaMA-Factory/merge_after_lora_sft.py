# merge_lora.py
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel
import torch, json, os

base = "Qwen/Qwen2.5-3B-Instruct"   # use the exact base you fine-tuned
adapter = "saves/qwen2_5_3b_tau_bench_lora"
out = "merged_models/merged-qwen2.5-3b-tau"

tok = AutoTokenizer.from_pretrained(base, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    base, torch_dtype=torch.bfloat16, device_map="auto", trust_remote_code=True
)

# Load LoRA and merge
model = PeftModel.from_pretrained(model, adapter)
model = model.merge_and_unload()

# If you added tokens during SFT, resize embeddings
added = os.path.join(adapter, "added_tokens.json")
if os.path.exists(added):
    with open(added) as f:
        extra = list(json.load(f).keys())
    if extra:
        tok.add_tokens(extra)
        model.resize_token_embeddings(len(tok))

model.save_pretrained(out, safe_serialization=True)
tok.save_pretrained(out)
print("Saved merged model to:", out)
