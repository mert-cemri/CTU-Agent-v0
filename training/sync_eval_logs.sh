#!/bin/bash

# Script to sync evaluation logs from exports directory to GitHub repository
# This ensures evaluation conversations are tracked in version control

# Configuration
REPO_DIR="$(dirname "$0")/.."
EVAL_LOGS_DIR="$REPO_DIR/evaluation_logs"
SOURCE_EXPORTS="$HOME/exports"

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}=== Syncing Evaluation Logs to Repository ===${NC}"

# Create evaluation_logs directory if it doesn't exist
if [ ! -d "$EVAL_LOGS_DIR" ]; then
    echo "Creating evaluation_logs directory in repository..."
    mkdir -p "$EVAL_LOGS_DIR"
fi

# Function to sync a specific training run's evaluations
sync_training_run() {
    local source_dir="$1"
    local run_name="$2"
    
    if [ -d "$source_dir/dumped_evals" ]; then
        local dest_dir="$EVAL_LOGS_DIR/$run_name"
        mkdir -p "$dest_dir"
        
        echo -e "${YELLOW}Syncing $run_name evaluations...${NC}"
        
        # Copy only the latest evaluation for each checkpoint to save space
        # Or copy all if you want complete history
        cp -r "$source_dir/dumped_evals" "$dest_dir/" 2>/dev/null
        
        # Count the files synced
        local file_count=$(find "$dest_dir" -type f -name "*.json*" 2>/dev/null | wc -l)
        echo "  Synced $file_count evaluation files for $run_name"
    else
        echo "  No evaluations found for $run_name"
    fi
}

# Sync tau_bench evaluations
if [ -d "$SOURCE_EXPORTS/tau_bench" ]; then
    sync_training_run "$SOURCE_EXPORTS/tau_bench" "tau_bench_multi_domain"
fi

# Sync tau_bench_retail evaluations
if [ -d "$SOURCE_EXPORTS/tau_bench_retail" ]; then
    sync_training_run "$SOURCE_EXPORTS/tau_bench_retail" "tau_bench_retail"
fi

# Sync any model-specific exports
for model_dir in "$SOURCE_EXPORTS"/tau_bench_*; do
    if [ -d "$model_dir" ] && [ "$model_dir" != "$SOURCE_EXPORTS/tau_bench" ] && [ "$model_dir" != "$SOURCE_EXPORTS/tau_bench_retail" ]; then
        model_name=$(basename "$model_dir")
        sync_training_run "$model_dir" "$model_name"
    fi
done

echo -e "${GREEN}=== Sync Complete ===${NC}"
echo ""
echo "Evaluation logs are now in: $EVAL_LOGS_DIR"
echo "You can commit them with:"
echo "  cd $REPO_DIR"
echo "  git add evaluation_logs/"
echo "  git commit -m 'Add evaluation conversation logs'"
echo "  git push"

# Optional: Add a summary file
SUMMARY_FILE="$EVAL_LOGS_DIR/README.md"
cat > "$SUMMARY_FILE" << EOF
# Evaluation Logs

This directory contains conversation logs from model evaluations during training.

## Structure

\`\`\`
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
\`\`\`

## Contents

Each evaluation directory contains:
- **Conversation traces**: Full agent-user interactions
- **Tool calls**: All tools used during conversations
- **Outcomes**: Success/failure for each conversation
- **Rewards**: Reward signals received

## Viewing Logs

The logs are in JSONL format. To view them:

\`\`\`bash
# View a specific conversation log
cat evaluation_logs/tau_bench_retail/dumped_evals/global_step_100_evals/eval_results.jsonl | jq .

# Count successful conversations
grep '"success": true' evaluation_logs/*/dumped_evals/*/eval_results.jsonl | wc -l
\`\`\`

## Auto-sync

To sync the latest evaluation logs from training runs:

\`\`\`bash
bash training/sync_eval_logs.sh
\`\`\`

Last synced: $(date)
EOF

echo "Created summary at: $SUMMARY_FILE"