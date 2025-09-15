#!/bin/bash

# Minimal test to reproduce the Hydra issue
cd "$(dirname "$0")/training"

echo "Testing minimal Hydra command..."

TAXONOMY_ALPHA="1.0"

python main_tau_bench.py \
  trainer.epochs=1 \
  environment.skyrl_gym.tau_bench.TAXONOMY_ALPHA="$TAXONOMY_ALPHA" \
  --help