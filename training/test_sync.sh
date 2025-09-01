#!/bin/bash

# Debug script to test evaluation log syncing

echo "Testing evaluation log sync..."
echo ""

# Check if exports directory exists
if [ -d "$HOME/exports" ]; then
    echo "✓ Found exports directory at: $HOME/exports"
    echo "  Contents:"
    ls -la "$HOME/exports/" | head -10
else
    echo "✗ No exports directory found at $HOME/exports"
fi

echo ""

# Check for tau_bench_retail
if [ -d "$HOME/exports/tau_bench_retail" ]; then
    echo "✓ Found tau_bench_retail exports"
    echo "  Contents:"
    ls -la "$HOME/exports/tau_bench_retail/" | head -10
    
    if [ -d "$HOME/exports/tau_bench_retail/dumped_evals" ]; then
        echo ""
        echo "✓ Found dumped_evals directory"
        echo "  Number of evaluation directories:"
        ls -d "$HOME/exports/tau_bench_retail/dumped_evals"/*/ 2>/dev/null | wc -l
        
        echo "  First few directories:"
        ls -d "$HOME/exports/tau_bench_retail/dumped_evals"/*/ 2>/dev/null | head -5
        
        # Try to copy manually
        echo ""
        echo "Attempting manual copy to repository..."
        DEST_DIR="$(dirname "$0")/../evaluation_logs/tau_bench_retail"
        mkdir -p "$DEST_DIR"
        
        if cp -r "$HOME/exports/tau_bench_retail/dumped_evals" "$DEST_DIR/" ; then
            echo "✓ Manual copy successful!"
            echo "  Files copied to: $DEST_DIR/dumped_evals/"
            ls -la "$DEST_DIR/dumped_evals/" | head -10
        else
            echo "✗ Manual copy failed"
            echo "  Error code: $?"
        fi
    else
        echo "✗ No dumped_evals directory found"
    fi
else
    echo "✗ No tau_bench_retail exports found"
fi

echo ""
echo "Repository evaluation_logs contents:"
ls -la "$(dirname "$0")/../evaluation_logs/"