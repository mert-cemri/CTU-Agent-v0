#!/usr/bin/env python3
"""
Debug script to check why rewards are 0
"""

import os
import sys

def debug_rewards_issue():
    print("=== Debugging Rewards Issue ===\n")
    
    print("1. Check SKYRL_MODE environment variable:")
    mode = os.environ.get("SKYRL_MODE", "not_set")
    print(f"   SKYRL_MODE = {mode}")
    if mode == "not_set":
        print("   ⚠️  SKYRL_MODE not set - defaulting to 'train'")
    print()
    
    print("2. Common issues causing rewards=0:")
    print()
    
    print("   a) REF_MODEL Configuration Issue:")
    print("      Your script has: REF_MODEL=mcemri/qwen2.5_3b_alldata_sft_v0")
    print("      ❌ WRONG: Using SFT model as reference")
    print("      ✅ CORRECT: Use base model as reference")
    print("      FIX: REF_MODEL=\"Qwen/Qwen2.5-3B-Instruct\"")
    print()
    
    print("   b) Model Not Following Tool Format:")
    print("      - SFT model might not be trained with tool calling format")
    print("      - Check if model outputs valid tool calls")
    print("      - Enable DEBUG_PARSER=1 to see what model outputs")
    print()
    
    print("   c) All Tasks Failing:")
    print("      - If success_rate=0, agent is failing all tasks")
    print("      - Check tau_bench API key is valid")
    print("      - Check if model can parse tool format correctly")
    print()
    
    print("3. Recommended Debug Steps:")
    print()
    print("   # Step 1: Fix REF_MODEL in your script")
    print("   REF_MODEL=\"Qwen/Qwen2.5-3B-Instruct\"")
    print()
    print("   # Step 2: Enable debug logging")
    print("   export DEBUG_PARSER=1")
    print()
    print("   # Step 3: Run with smaller batch for testing")
    print("   trainer.train_batch_size=4")
    print()
    print("   # Step 4: Check model outputs")
    print("   # Look for lines starting with:")
    print("   #   🔍 PARSER DEBUG:")
    print("   #   📝 ACTION PARSED:")
    print()
    
    print("4. Quick Test Script:")
    print("   Run this to test if your model can generate tool calls:\n")
    
    test_code = '''
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_path = "mcemri/qwen2.5_3b_alldata_sft_v0"
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path, torch_dtype=torch.float16, device_map="auto")

# Test prompt with tool format
test_prompt = """You are a helpful assistant.

## Tools Available:
- search_flights: Search for flights
- book_flight: Book a specific flight

User: Find me a flight from NYC to LAX tomorrow
Assistant: """

inputs = tokenizer(test_prompt, return_tensors="pt").to(model.device)
outputs = model.generate(**inputs, max_new_tokens=200, temperature=0.7)
response = tokenizer.decode(outputs[0][inputs.input_ids.shape[-1]:], skip_special_tokens=True)

print("Model Response:")
print(response)
print()
print("Does it contain tool calls? Look for patterns like:")
print("  - Action: search_flights")
print("  - <tool>search_flights</tool>")
print("  - {\"tool\": \"search_flights\"}")
'''
    print(test_code)

if __name__ == "__main__":
    debug_rewards_issue()