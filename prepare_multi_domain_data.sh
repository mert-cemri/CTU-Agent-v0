#!/bin/bash

# Convert multi-domain tau_bench data
python -m data_prep.convert_multi_domain \
  --input_files \
    novel_datasets/train_tasks_doordash.py \
    novel_datasets/train_tasks_telecom.py \
    novel_datasets/train_tasks_healthcare.py \
  --output_dir data/tau_bench_multi \
  --train_ratio 0.9

echo "Multi-domain dataset created at: data/tau_bench_multi/"