import os
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from torch.distributed import init_process_group, destroy_process_group
from torch.distributed.checkpoint import FileSystemReader, load_state_dict
from torch.distributed.checkpoint.state_dict import get_state_dict, set_state_dict, StateDictOptions

# ---- USER INPUTS ----
CKPT_DIR   = "/path/to/checkpoints/.../global_step_5/policy"  # the 'policy' folder in your screenshot
BASE_MODEL = "Qwen/Qwen2.5-3B-Instruct"                       # same base you started RL from
OUT_DIR    = "./qwen2p5_3b_rl_export"                         # where to write HF weights
DTYPE      = torch.bfloat16                                   # or torch.float16 / float32
DEVICE     = "cuda" if torch.cuda.is_available() else "cpu"
