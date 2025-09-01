#!/bin/bash

# Script to sync evaluation logs from remote server to local repository
# Run this from your local machine (Mac) to pull logs from the training server

# Configuration - MODIFY THESE FOR YOUR SETUP
SERVER_USER="root"
SERVER_HOST="your-server-ip"  # Replace with your server IP or hostname
SERVER_EXPORTS_DIR="/root/exports"
LOCAL_EVAL_DIR="$(dirname "$0")/../evaluation_logs"

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${GREEN}=== Syncing Evaluation Logs from Server ===${NC}"
echo ""

# Check if we have server details
if [ "$SERVER_HOST" = "your-server-ip" ]; then
    echo -e "${RED}Error: Please edit this script and set SERVER_HOST to your server's IP address${NC}"
    echo "Edit the file: training/sync_from_server.sh"
    echo "Change SERVER_HOST=\"your-server-ip\" to your actual server IP"
    exit 1
fi

# Create local evaluation_logs directory if it doesn't exist
mkdir -p "$LOCAL_EVAL_DIR"

# Function to sync a specific directory
sync_from_server() {
    local remote_path="$1"
    local local_name="$2"
    
    echo -e "${YELLOW}Syncing $local_name from server...${NC}"
    echo "  Remote: $SERVER_USER@$SERVER_HOST:$remote_path"
    echo "  Local: $LOCAL_EVAL_DIR/$local_name/"
    
    # Use rsync to efficiently sync the files
    # -a: archive mode (preserves permissions, timestamps, etc.)
    # -v: verbose
    # -z: compress during transfer
    # --progress: show progress
    if command -v rsync &> /dev/null; then
        rsync -avz --progress \
            "$SERVER_USER@$SERVER_HOST:$remote_path/dumped_evals/" \
            "$LOCAL_EVAL_DIR/$local_name/dumped_evals/" 2>/dev/null
        
        if [ $? -eq 0 ]; then
            echo -e "  ${GREEN}✓ Sync successful${NC}"
            # Count synced files
            local file_count=$(find "$LOCAL_EVAL_DIR/$local_name" -type f \( -name "*.json*" -o -name "*.txt" \) 2>/dev/null | wc -l)
            echo "  Synced $file_count files"
        else
            echo -e "  ${RED}✗ Sync failed or no files found${NC}"
        fi
    else
        # Fallback to scp if rsync is not available
        echo "  Using scp (rsync not available)..."
        scp -r "$SERVER_USER@$SERVER_HOST:$remote_path/dumped_evals" \
            "$LOCAL_EVAL_DIR/$local_name/" 2>/dev/null
    fi
    echo ""
}

# Check if we can connect to the server
echo "Testing connection to server..."
if ssh -o ConnectTimeout=5 "$SERVER_USER@$SERVER_HOST" "echo 'Connected'" &>/dev/null; then
    echo -e "${GREEN}✓ Connection successful${NC}"
    echo ""
    
    # List available exports on server
    echo "Available exports on server:"
    ssh "$SERVER_USER@$SERVER_HOST" "ls -la $SERVER_EXPORTS_DIR/ 2>/dev/null | head -10"
    echo ""
    
    # Sync tau_bench_retail
    sync_from_server "$SERVER_EXPORTS_DIR/tau_bench_retail" "tau_bench_retail"
    
    # Sync tau_bench (multi-domain)
    sync_from_server "$SERVER_EXPORTS_DIR/tau_bench" "tau_bench_multi_domain"
    
    # Sync any other model-specific exports
    echo "Checking for other model exports..."
    ssh "$SERVER_USER@$SERVER_HOST" "ls -d $SERVER_EXPORTS_DIR/tau_bench_* 2>/dev/null" | while read -r export_dir; do
        if [[ "$export_dir" != */tau_bench_retail && "$export_dir" != */tau_bench ]]; then
            dir_name=$(basename "$export_dir")
            sync_from_server "$export_dir" "$dir_name"
        fi
    done
    
else
    echo -e "${RED}✗ Cannot connect to server${NC}"
    echo ""
    echo "Please check:"
    echo "1. Is the server running and accessible?"
    echo "2. Is SERVER_HOST set correctly in this script?"
    echo "3. Do you have SSH access to $SERVER_USER@$SERVER_HOST?"
    echo ""
    echo "You may need to:"
    echo "- Set up SSH keys: ssh-copy-id $SERVER_USER@$SERVER_HOST"
    echo "- Or manually copy files from server and run local sync script"
    exit 1
fi

# Create/Update README
cat > "$LOCAL_EVAL_DIR/README.md" << EOF
# Evaluation Logs

This directory contains conversation logs from model evaluations during training.
Synced from server: $SERVER_HOST

## Last Sync
$(date)

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

## How to Sync from Server

1. Edit \`training/sync_from_server.sh\` and set your server details
2. Run: \`bash training/sync_from_server.sh\`
3. Commit the synced files to git

## Viewing Logs

\`\`\`bash
# View evaluation results
cat evaluation_logs/tau_bench_retail/dumped_evals/*/eval_results.jsonl | jq .
\`\`\`
EOF

echo -e "${GREEN}=== Sync Complete ===${NC}"
echo ""
echo "Evaluation logs synced to: $LOCAL_EVAL_DIR"
echo ""
echo "To commit to GitHub:"
echo "  git add evaluation_logs/"
echo "  git commit -m 'Sync evaluation logs from training server'"
echo "  git push"