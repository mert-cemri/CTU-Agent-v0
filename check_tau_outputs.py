#!/usr/bin/env python3
import json

# Read the source tau_bench data
with open('tau_bench/data/novel_sft_dataset.json', 'r') as f:
    data = json.load(f)

print(f'Total conversations: {len(data)}')

# Look at the first few retail domain conversations
retail_count = 0
for i, conv in enumerate(data):
    if conv.get('domain') == 'retail' and retail_count < 3:
        retail_count += 1
        print(f'\n{"="*60}')
        print(f'Retail conversation {retail_count} (index {i}):')
        print(f'{"="*60}')
        
        # Show basic info
        print(f'Domain: {conv.get("domain")}')
        print(f'Instruction: {conv.get("instruction", "")[:100]}...')
        
        # Check for outputs
        if 'outputs' in conv:
            print(f'\nFOUND OUTPUTS in conversation!')
            print(f'Outputs type: {type(conv["outputs"])}')
            if isinstance(conv["outputs"], list):
                print(f'Number of outputs: {len(conv["outputs"])}')
                if len(conv["outputs"]) > 0:
                    print(f'First output: {conv["outputs"][0][:200]}...' if len(conv["outputs"][0]) > 200 else conv["outputs"][0])
        
        # Check actions
        if 'actions' in conv:
            print(f'\nActions: {len(conv["actions"])} actions')
            for j, action in enumerate(conv["actions"][:2]):
                print(f'  Action {j}: {json.dumps(action, indent=4)}')
        
        # Check for any other keys
        print(f'\nAll keys in conversation: {list(conv.keys())}')
        
        # Look for any field containing "output" in its name
        output_related_keys = [k for k in conv.keys() if 'output' in k.lower()]
        if output_related_keys:
            print(f'\nKeys containing "output": {output_related_keys}')
            for key in output_related_keys:
                value = conv[key]
                if isinstance(value, list) and len(value) > 0:
                    print(f'{key}: {value[0][:100]}...' if len(str(value[0])) > 100 else value)