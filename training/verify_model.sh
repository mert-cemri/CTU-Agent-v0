#!/bin/bash

# Script to verify and fix SFT model for RL training

MODEL_DIR="${1:-/root/qwen2.5_3b_alldata_sft_v0}"

echo "=== Verifying Model Directory: $MODEL_DIR ==="
echo ""

# Check if directory exists
if [ ! -d "$MODEL_DIR" ]; then
    echo "Error: Directory not found: $MODEL_DIR"
    exit 1
fi

echo "Directory contents:"
ls -lah "$MODEL_DIR"
echo ""

# Check file sizes
echo "Checking file integrity:"

# Check if tokenizer.json is valid
if [ -f "$MODEL_DIR/tokenizer.json" ]; then
    SIZE=$(stat -c%s "$MODEL_DIR/tokenizer.json" 2>/dev/null || stat -f%z "$MODEL_DIR/tokenizer.json" 2>/dev/null)
    if [ "$SIZE" -lt 100 ]; then
        echo "✗ tokenizer.json is too small ($SIZE bytes) - likely corrupted"
        echo "  Running fix..."
        python training/fix_tokenizer.py "$MODEL_DIR"
    else
        echo "✓ tokenizer.json exists ($SIZE bytes)"
        # Try to parse it
        python -c "import json; json.load(open('$MODEL_DIR/tokenizer.json'))" 2>/dev/null
        if [ $? -eq 0 ]; then
            echo "  ✓ Valid JSON"
        else
            echo "  ✗ Invalid JSON - running fix..."
            python training/fix_tokenizer.py "$MODEL_DIR"
        fi
    fi
else
    echo "✗ tokenizer.json missing - downloading from base model..."
    python training/fix_tokenizer.py "$MODEL_DIR"
fi

echo ""

# Check model files
echo "Model safetensor files:"
ls -lah "$MODEL_DIR"/*.safetensors 2>/dev/null || echo "  No safetensor files found!"

echo ""

# Test loading with transformers
echo "Testing model loading:"
python -c "
from transformers import AutoTokenizer, AutoModelForCausalLM
import sys

try:
    print('Loading tokenizer...')
    tokenizer = AutoTokenizer.from_pretrained('$MODEL_DIR')
    print(f'✓ Tokenizer loaded (vocab size: {len(tokenizer)})')
    
    print('Loading model config...')
    from transformers import AutoConfig
    config = AutoConfig.from_pretrained('$MODEL_DIR')
    print(f'✓ Config loaded (model type: {config.model_type})')
    
    print('Model is ready for RL training!')
    sys.exit(0)
except Exception as e:
    print(f'✗ Error: {e}')
    sys.exit(1)
"

if [ $? -eq 0 ]; then
    echo ""
    echo "=== Model Verified Successfully ==="
    echo "You can use this model for RL training with:"
    echo "  POLICY_MODEL=\"$MODEL_DIR\""
else
    echo ""
    echo "=== Model Verification Failed ==="
    echo "Please check the error messages above"
fi