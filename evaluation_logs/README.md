# Evaluation Logs

This directory contains conversation logs from model evaluations during training.

## Structure

```
evaluation_logs/
├── tau_bench_multi_domain/     # Multi-domain training evaluations
│   └── dumped_evals/
│       ├── global_step_X_evals/
│       └── ...
├── tau_bench_retail/           # Retail-only training evaluations
│   └── dumped_evals/
│       ├── global_step_X_evals/
│       └── ...
└── [model_specific_dirs]/      # Model-specific evaluations
```

## Contents

Each evaluation directory contains:
- **Conversation traces**: Full agent-user interactions
- **Tool calls**: All tools used during conversations
- **Outcomes**: Success/failure for each conversation
- **Rewards**: Reward signals received

## Viewing Logs

The logs are in JSONL format. To view them:

```bash
# View a specific conversation log
cat evaluation_logs/tau_bench_retail/dumped_evals/global_step_100_evals/eval_results.jsonl | jq .

# Count successful conversations
grep '"success": true' evaluation_logs/*/dumped_evals/*/eval_results.jsonl | wc -l
```

## Auto-sync

To sync the latest evaluation logs from training runs:

```bash
bash training/sync_eval_logs.sh
```

Last synced: Mon Sep  1 09:40:35 UTC 2025
