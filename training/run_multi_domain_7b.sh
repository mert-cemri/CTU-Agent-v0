#!/bin/bash

# Multi-domain training (telecom, doordash, healthcare)
DATA_DIR="data/tau_bench_multi"
RETAIL_VAL_DIR="data/tau_bench_retail"

POLICY_MODEL="Qwen/Qwen2.5-7B-Instruct"
REF_MODEL="Qwen/Qwen2.5-7B-Instruct"
MODEL_NAME_SANITIZED=$(echo $POLICY_MODEL | tr '/' '_')_v6-multi-domain

# Run training with multi-domain data and retail validation set
bash training/run_tau_bench_7b.sh \
  data.train_data="['$DATA_DIR/train.parquet']" \
  data.val_data="['$DATA_DIR/validation.parquet']" \
  data.retail_val_data="['$RETAIL_VAL_DIR/validation.parquet']" \
  "$@"