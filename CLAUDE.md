# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

**IMPORTANT**: This file should be updated whenever there are significant changes to the system architecture, configuration, or development practices.

## Table of Contents

1. [Project Overview](#project-overview)
2. [System Architecture](#system-architecture)
3. [Core Components](#core-components)
4. [Dataset and Data Pipeline](#dataset-and-data-pipeline)
5. [Training Pipeline](#training-pipeline)
6. [Environment Variables and Configuration](#environment-variables-and-configuration)
7. [Development Commands](#development-commands)
8. [Debugging and Monitoring](#debugging-and-monitoring)
9. [Common Issues and Solutions](#common-issues-and-solutions)

## Project Overview

CTU-Agent-v0 is a sophisticated reinforcement learning system that trains language models to effectively use tools in multi-turn conversations. The project integrates:

- **tau_bench**: A multi-domain conversational AI benchmark with tool-use capabilities
- **SkyRL-Train**: A distributed RL training framework from Sky Computing Lab
- **Policy Model**: Qwen/Qwen2.5-3B-Instruct (being trained)
- **User Simulation**: GPT-4o for realistic user behavior

**Primary Objective**: Train language models to correctly use tools across multiple domains (airline, healthcare, telecom, doordash, retail) through reinforcement learning, achieving high task completion rates.

## System Architecture

### High-Level Flow

```
tau_bench environments → TauBenchEnv wrapper → SkyRL Gymnasium interface
                                                        ↓
                                              SkyRL Training Loop
                                                        ↓
                                            Model generates tool calls
                                                        ↓
                                          Parser extracts actions
                                                        ↓
                                        Environment executes tools
                                                        ↓
                                          Reward calculation
```

### Key Integration Points

1. **Environment Registration** (training/main_tau_bench.py:56-59):
   ```python
   register(
       id="tau_bench",
       entry_point="tau_bench_env.env:TauBenchEnv",
   )
   ```

2. **SkyRL-tau_bench Bridge** (tau_bench_env/env.py):
   - Converts tau_bench actions to SkyRL format
   - Manages multi-turn conversations
   - Calculates rewards based on task completion

3. **Training Pipeline** (SkyRL_mod/skyrl-train/skyrl_train/trainer.py):
   - Modified to handle empty responses (lines 734-755)
   - Tracks parse failure rates (lines 710-719)
   - Early metric logging to prevent data loss (lines 722-728)

## Core Components

### 1. tau_bench_env/env.py - Main Environment Class

**Purpose**: Wraps tau_bench environments with SkyRL-compatible Gymnasium interface

**Key Methods**:
- `__init__()`: Initializes domain-specific environment and user simulation
- `reset()`: Starts new conversation, returns initial observation
- `step()`: Processes agent action, returns next observation and reward
- `get_messages()`: Formats conversation history for LLM input

**Important Details**:
- Max turns: 20 (configurable)
- Reward: Binary (0 or 1) at conversation end
- Supports all 5 tau_bench domains

### 2. tau_bench_env/parser.py - Response Parser

**Purpose**: Robustly extracts tool calls from LLM outputs

**Supported Formats**:
1. Direct JSON: `{"name": "tool_name", "arguments": {...}}`
2. OpenAI format: `{"tool_calls": [{"function": {...}}]}`
3. Code blocks: ````python\ntool_name(arg="value")\n````
4. ReAct style: `Action: tool_name\nAction Input: {...}`

**Fallback**: Returns "respond" action for natural language

### 3. data_prep/convert_tau_data.py - Data Converter

**Purpose**: Converts tau_bench JSON to SkyRL parquet format

**Usage**:
```bash
python -m data_prep.convert_tau_data \
  --input_path tau_bench/data/novel_sft_dataset.json \
  --output_dir $HOME/data/tau_bench \
  --train_ratio 0.9
```

**Output Format**:
- `prompt`: JSON string with conversation format
- `env_class`: "tau_bench"
- `reward_spec`: Ground truth actions
- `extra_info`: Domain, instruction, etc.

### 4. training/main_tau_bench.py - Training Entry Point

**Purpose**: Hydra-based training launcher with Ray integration

**Key Features**:
- Validates configuration
- Sets up Ray cluster with OPENAI_API_KEY
- Registers tau_bench environment
- Launches distributed training

### 5. SkyRL_mod/skyrl-train/skyrl_train/trainer.py - Modified Trainer

**Modifications**:
- **Empty Response Handling** (lines 734-755): Filters out empty generations
- **Parse Failure Tracking** (lines 710-719): Monitors parsing success rate
- **Early Metric Flushing** (lines 722-728, 819-828, 1061-1066): Prevents metric loss

**Training Algorithm**: GRPO (Group Relative Policy Optimization) with KL regularization

## Dataset and Data Pipeline

### Current Dataset

**Location**: `data/tau_bench_retail/`
- Using retail domain subset of tau_bench
- Train: 248KB (train.parquet)
- Validation: 26KB (validation.parquet)

### Data Structure

```python
{
    "prompt": {
        "messages": [
            {"role": "system", "content": "...tools..."},
            {"role": "user", "content": "task instruction"}
        ]
    },
    "env_class": "tau_bench",
    "reward_spec": {
        "ground_truth_actions": [...],
        "ground_truth_outputs": [...]
    },
    "extra_info": {
        "domain": "retail",
        "user_strategy": "llm",
        "instruction": "..."
    }
}
```

### Available Datasets

- `tau_bench/data/novel_sft_dataset.json`: Full multi-domain dataset
- Domain-specific splits can be created using convert_tau_data.py

## Training Pipeline

### 1. Initialization Flow

```
main_tau_bench.py
    ↓
Validate config
    ↓
Initialize Ray cluster
    ↓
Register environment
    ↓
Launch SkyRL trainer
```

### 2. Training Loop (SkyRL)

```
For each epoch:
    1. Generate trajectories (multiple samples per prompt)
    2. Parse model outputs → tool calls
    3. Execute in environment
    4. Calculate rewards
    5. Compute advantages (GRPO)
    6. Update policy model
    7. Save checkpoints
```

### 3. Generation Pipeline

**SkyRLGymGenerator** (skyrl_train/generators/skyrl_gym_generator.py):
- Manages parallel trajectory generation
- Handles multi-turn conversations via `agent_loop()`
- Integrates with VLLM for efficient inference

### 4. Reward Calculation

**Location**: tau_bench/envs/base.py

**Logic**:
1. Initial reward: 1.0
2. Check data consistency (environment state hash)
3. Verify required outputs in agent responses
4. Final: 0.0 if any check fails, 1.0 if all pass

## Environment Variables and Configuration

### Required Environment Variables

```bash
export OPENAI_API_KEY="your-key"  # For user simulation
export WANDB_API_KEY="your-key"   # Optional: experiment tracking
export RAY_RUNTIME_ENV_HOOK=ray._private.runtime_env.uv_runtime_env_hook.hook
```

### Configuration Files

**training/configs/tau_bench_config.yaml**:
```yaml
model_name_or_path: Qwen/Qwen2.5-3B-Instruct
trainer:
  epochs: 50
  train_batch_size: 256
  max_model_len: 16384  # Increased for tool-rich prompts
generator:
  n_samples_per_prompt: 3
  rollout_strategy: "non-batched"
  engine: "vllm"
algorithm:
  name: "grpo"
  kl_weight: 0.01
  advantage_estimator: "grpo"
```

### Key Parameters

- **max_turns**: 20 (tau_bench_env/env.py:50)
- **temperature**: 0.7 (for generation)
- **user_model**: "gpt-4o" (tau_bench user simulation)
- **user_strategy**: "llm" (can be: llm, react, verify, reflection)

## Development Commands

### Setup
```bash
# Install dependencies
cd SkyRL_mod/skyrl-train
uv sync --extra vllm
source .venv/bin/activate
export RAY_RUNTIME_ENV_HOOK=ray._private.runtime_env.uv_runtime_env_hook.hook
```

### Data Preparation
```bash
# Convert full dataset
python -m data_prep.convert_tau_data \
  --input_path tau_bench/data/novel_sft_dataset.json \
  --output_dir $HOME/data/tau_bench \
  --train_ratio 0.9

# Convert specific domain
python -m data_prep.convert_tau_data \
  --input_path tau_bench/data/novel_sft_dataset.json \
  --output_dir $HOME/data/tau_bench_airline \
  --domain airline \
  --train_ratio 0.9
```

### Training
```bash
# Default training
bash training/run_tau_bench.sh

# Custom parameters
bash training/run_tau_bench.sh \
  trainer.epochs=100 \
  trainer.train_batch_size=512 \
  generator.n_samples_per_prompt=5 \
  algorithm.kl_weight=0.05

# Resume from checkpoint
bash training/run_tau_bench.sh \
  trainer.load_checkpoint=latest
```

### Testing
```bash
# Run integration tests
python test_tau_bench_integration.py

# Test specific component
python -m pytest tau_bench_env/test_parser.py -v
```

### Linting and Type Checking
```bash
# Format code
black . --line-length 120

# Sort imports
isort .

# Type check (if configured)
mypy tau_bench_env/
```

## Debugging and Monitoring

### Training Logs
```bash
# Real-time training logs
tail -f $HOME/ckpts/tau_bench/logs/train.log

# Parse failure rates
grep "parse_failure_rate" $HOME/ckpts/tau_bench/logs/train.log
```

### Checkpoints
```bash
# View checkpoints
ls -la $HOME/ckpts/tau_bench/

# Latest checkpoint
cat $HOME/ckpts/tau_bench/latest_ckpt_global_step.txt

# Checkpoint structure
tree $HOME/ckpts/tau_bench/global_step_10/
```

### Exports
```bash
# View exported models
ls -la $HOME/exports/tau_bench/

# Load exported model
from transformers import AutoModelForCausalLM
model = AutoModelForCausalLM.from_pretrained("$HOME/exports/tau_bench/global_step_100")
```

### Weights & Biases
```bash
# If using W&B tracking
wandb login
# Training will automatically log to W&B
```

## Common Issues and Solutions

### 1. Empty Response Handling
**Issue**: Model generates empty responses causing training crashes
**Solution**: Implemented in trainer.py:734-755 - filters out empty responses
**File**: SkyRL_mod/skyrl-train/skyrl_train/trainer.py

### 2. Parse Failures
**Issue**: Model outputs don't match expected tool call format
**Solution**: Robust parser with multiple format support
**File**: tau_bench_env/parser.py
**Fix**: Commit 80eba5c improved parser robustness

### 3. Low Success Rate
**Issue**: Current success rate ~0.4 (commit 813d75b)
**Potential Solutions**:
- Increase n_samples_per_prompt for better exploration
- Add few-shot examples to system prompt
- Tune temperature for tool selection
- Consider curriculum learning (start with easier domains)

### 4. Memory Issues
**Issue**: OOM with large batch sizes or context length
**Solutions**:
- Reduce train_batch_size
- Enable gradient_accumulation_steps
- Use gradient_checkpointing: true
- Reduce max_model_len if possible

### 5. Ray Initialization
**Issue**: Ray fails to initialize with UV
**Solution**: Set RAY_RUNTIME_ENV_HOOK environment variable
```bash
export RAY_RUNTIME_ENV_HOOK=ray._private.runtime_env.uv_runtime_env_hook.hook
```

### Recent Fixes
- **80eba5c**: Made parser robust to unexpected output formats
- **2fa1da9**: Fixed using training split of tau_bench retail
- **14a0e32**: Fixed len(rsp)=0 crashes

## Notes for Future Development

1. **Success Rate Improvement**: Current 0.4 success rate needs investigation
2. **Multi-Domain Training**: Consider domain-specific fine-tuning
3. **Tool Format**: May benefit from instruction tuning on tool format
4. **User Simulation**: Experiment with different user strategies
5. **Reward Shaping**: Consider intermediate rewards for partial success