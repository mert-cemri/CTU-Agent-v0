# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

CTU-Agent-v0 is a reinforcement learning system that trains language models (specifically Qwen-1.5B-Instruct) to effectively use tools across multiple domains (airline, healthcare, telecom, doordash, retail). It integrates tau_bench's conversational AI framework with SkyRL-Train for distributed RL training.

## Key Commands

### Setup and Installation
```bash
# Install dependencies
cd SkyRL_mod/skyrl-train
uv sync --extra vllm
source .venv/bin/activate
export RAY_RUNTIME_ENV_HOOK=ray._private.runtime_env.uv_runtime_env_hook.hook
```

### Data Preparation
```bash
# Convert tau_bench data to SkyRL format
python -m data_prep.convert_tau_data \
  --input_path tau_bench/data/novel_sft_dataset.json \
  --output_dir $HOME/data/tau_bench \
  --train_ratio 0.9
```

### Training
```bash
# Run training with defaults
bash training/run_tau_bench.sh

# Custom parameters
bash training/run_tau_bench.sh trainer.epochs=100 trainer.train_batch_size=512
```

### Testing
```bash
# Run integration tests
python test_tau_bench_integration.py
```

### Monitoring
```bash
# Check training logs
tail -f $HOME/ckpts/tau_bench/logs/train.log

# View checkpoints and exports
ls -la $HOME/ckpts/tau_bench/
ls -la $HOME/exports/tau_bench/
```

## Architecture

### Core Components

1. **tau_bench_env/** - Main integration layer
   - `env.py`: TauBenchEnv class wrapping tau_bench environments with gymnasium interface
   - `parser.py`: Robust LLM response parser for extracting tool calls

2. **data_prep/** - Data preprocessing
   - `convert_tau_data.py`: Converts tau_bench JSON to SkyRL parquet format
   - `prompts.py`: Domain-specific system prompts

3. **training/** - Training pipeline
   - `main_tau_bench.py`: Hydra-based training entrypoint
   - `configs/`: YAML configuration files for experiments

4. **External Dependencies**
   - `tau_bench/`: Multi-domain conversational environments
   - `SkyRL_mod/`: Modified SkyRL framework for distributed RL

### Key Design Patterns

- **Configuration-Driven**: Uses Hydra for all configuration management
- **Environment Abstraction**: Single TauBenchEnv class handles all tau_bench domains
- **Distributed Training**: Ray-based distributed computing with GPU placement
- **Multi-Turn Conversations**: Supports configurable max turns (default: 20)
- **Flexible User Simulation**: Multiple strategies (llm, react, verify, reflection)

### Important Files to Understand

1. `tau_bench_env/env.py` - Core environment logic and reward calculation
2. `tau_bench_env/parser.py` - Critical for parsing model outputs correctly
3. `training/configs/tau_bench.yaml` - Main configuration file
4. `SkyRL_mod/skyrl-train/skyrl_train/trainer.py` - Modified trainer logic

### Development Notes

- Python 3.12 required, CUDA 12.8 for GPU support
- Requires OpenAI API key for user simulation (export OPENAI_API_KEY)
- Uses UV package manager (not pip)
- Black formatting with line length 120
- Integration tests should pass without API keys where possible