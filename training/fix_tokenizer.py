#!/usr/bin/env python3
"""
Fix corrupted tokenizer.json by re-downloading from the base model
"""

import os
import shutil
from transformers import AutoTokenizer
import json

def fix_tokenizer(model_dir, base_model="Qwen/Qwen2.5-3B-Instruct"):
    """
    Fix corrupted tokenizer files by copying from base model
    """
    print(f"Fixing tokenizer in: {model_dir}")
    
    # Check if tokenizer.json exists and is valid
    tokenizer_json_path = os.path.join(model_dir, "tokenizer.json")
    
    if os.path.exists(tokenizer_json_path):
        try:
            with open(tokenizer_json_path, 'r') as f:
                data = json.load(f)
                print(f"✓ tokenizer.json is valid (has {len(data)} keys)")
                return  # File is OK
        except Exception as e:
            print(f"✗ tokenizer.json is corrupted: {e}")
            # Back up the corrupted file
            backup_path = tokenizer_json_path + ".corrupted"
            shutil.move(tokenizer_json_path, backup_path)
            print(f"  Backed up to: {backup_path}")
    else:
        print(f"✗ tokenizer.json not found")
    
    # Download tokenizer from base model
    print(f"Downloading tokenizer from: {base_model}")
    base_tokenizer = AutoTokenizer.from_pretrained(base_model)
    
    # Save only tokenizer files to the model directory
    print(f"Saving tokenizer files to: {model_dir}")
    base_tokenizer.save_pretrained(model_dir)
    
    # Verify the fix
    try:
        fixed_tokenizer = AutoTokenizer.from_pretrained(model_dir)
        print(f"✓ Tokenizer fixed successfully!")
        print(f"  Vocab size: {len(fixed_tokenizer)}")
    except Exception as e:
        print(f"✗ Failed to fix tokenizer: {e}")
        return False
    
    return True

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python fix_tokenizer.py /path/to/model/directory")
        print("\nExample:")
        print("  python fix_tokenizer.py /root/qwen2.5_3b_alldata_sft_v0")
        sys.exit(1)
    
    model_dir = sys.argv[1]
    
    if not os.path.exists(model_dir):
        print(f"Error: Directory not found: {model_dir}")
        sys.exit(1)
    
    success = fix_tokenizer(model_dir)
    sys.exit(0 if success else 1)