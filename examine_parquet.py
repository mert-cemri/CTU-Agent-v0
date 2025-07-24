#!/usr/bin/env python3
import pandas as pd
import json

# Read the parquet file
df = pd.read_parquet("data/tau_bench_retail/train.parquet")

print("=== Detailed examination of data structure ===\n")
print(f"DataFrame shape: {df.shape}")
print(f"Columns: {df.columns.tolist()}\n")

# Look at the first few rows in detail
for row_idx in range(min(3, len(df))):
    print(f"\n{'='*50}")
    print(f"Row {row_idx}:")
    print(f"{'='*50}")
    
    row = df.iloc[row_idx]
    
    # Parse reward_spec
    reward_spec = row["reward_spec"]
    if isinstance(reward_spec, str):
        reward_spec = json.loads(reward_spec)
    
    print("\nReward spec structure:")
    print(f"  Type: {type(reward_spec)}")
    print(f"  Keys: {list(reward_spec.keys())}")
    
    if "method" in reward_spec:
        print(f"  method: {reward_spec['method']}")
    
    if "ground_truth" in reward_spec:
        gt = reward_spec["ground_truth"]
        print(f"\n  ground_truth:")
        print(f"    Type: {type(gt)}")
        
        if isinstance(gt, list):
            print(f"    Length: {len(gt)}")
            if len(gt) > 0:
                print(f"    First item type: {type(gt[0])}")
                if isinstance(gt[0], dict):
                    print(f"    First item keys: {list(gt[0].keys())}")
                    print(f"    First item: {json.dumps(gt[0], indent=6)}")
    
    # Parse extra_info
    extra_info = row["extra_info"]
    if isinstance(extra_info, str):
        extra_info = json.loads(extra_info)
    
    print("\nExtra info structure:")
    print(f"  Type: {type(extra_info)}")
    print(f"  Keys: {list(extra_info.keys())}")
    
    # Check actions in extra_info
    if "actions" in extra_info:
        actions = extra_info["actions"]
        print(f"\n  actions:")
        print(f"    Type: {type(actions)}")
        print(f"    Length: {len(actions)}")
        
        if len(actions) > 0:
            print(f"\n    First action:")
            first_action = actions[0]
            print(f"      Type: {type(first_action)}")
            if isinstance(first_action, dict):
                print(f"      Keys: {list(first_action.keys())}")
                
                # Check for outputs field
                if "outputs" in first_action:
                    print(f"\n      *** FOUND 'outputs' field in action! ***")
                    print(f"      outputs: {first_action['outputs']}")
                
                # Show the full first action
                print(f"\n      Full action data:")
                print(json.dumps(first_action, indent=8))

# Search for any occurrence of "output" in the data
print("\n\n=== Global search for 'output' references ===")
sample_row = df.iloc[0]
row_str = json.dumps(sample_row.to_dict(), indent=2)

# Count occurrences
output_count = row_str.lower().count("output")
print(f"Found {output_count} occurrences of 'output' in first row")

# Find all unique keys containing "output"
import re
output_keys = set(re.findall(r'"([^"]*output[^"]*)":', row_str, re.IGNORECASE))
if output_keys:
    print(f"\nKeys containing 'output': {output_keys}")