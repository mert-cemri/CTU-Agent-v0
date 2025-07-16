# Tau Bench Integration with SkyRL-Train

This project integrates tau_bench's multi-domain conversational AI framework with SkyRL-Train to enable reinforcement learning training of language models on tool-use tasks.

## Overview

- **Assistant Agent**: Qwen-7B-Instruct (policy model to be trained)
- **User Proxy**: GPT-4o with tau_bench user simulation strategies
- **Domains**: airline, healthcare, telecom, doordash, retail
- **Reward**: Based on tool usage accuracy compared to ground truth actions

## Project Structure

```
CTU-Agent-v0/
├── tau_bench_env/                 # Environment integration
│   ├── __init__.py
│   ├── env.py                     # Main TauBenchEnv class
│   └── parser.py                  # LLM response parser
├── data_prep/                     # Data preparation utilities
│   ├── convert_tau_data.py        # Data conversion script
│   └── prompts.py                 # Domain-specific prompts
├── training/                      # Training pipeline
│   ├── main_tau_bench.py          # Training entrypoint
│   ├── run_tau_bench.sh           # Training script
│   └── configs/                   # Training configurations
│       ├── tau_bench_config.yaml
│       └── skyrl_gym_config/
│           └── tau_bench.yaml
├── test_tau_bench_integration.py  # Integration tests
├── tau_bench_integration_plan.md  # Implementation plan
└── README_tau_bench_integration.md # This file
```

## Setup Instructions

### 1. Prerequisites

- Python 3.12+
- CUDA 12.8
- UV package manager
- Access to OpenAI API (for GPT-4o user simulation)
- Weights & Biases account (for logging)

### 2. Environment Setup

```bash
# Install dependencies (from SkyRL-Train directory)
cd SkyRL_mod/skyrl-train
uv sync --extra vllm
source .venv/bin/activate

# Set up Ray for UV
export RAY_RUNTIME_ENV_HOOK=ray._private.runtime_env.uv_runtime_env_hook.hook
```

### 3. API Keys Configuration

```bash
# Set up your API keys
export OPENAI_API_KEY="your_openai_api_key"
export WANDB_API_KEY="your_wandb_api_key"

# Optional: Add to your .bashrc for persistence
echo 'export OPENAI_API_KEY="your_openai_api_key"' >> ~/.bashrc
echo 'export WANDB_API_KEY="your_wandb_api_key"' >> ~/.bashrc
```

### 4. Data Preparation

Convert tau_bench training data to SkyRL format:

```bash
# Convert training data
python -m data_prep.convert_tau_data \
  --input_path tau_bench/data/novel_sft_dataset.json \
  --output_dir $HOME/data/tau_bench \
  --train_ratio 0.9 \
  --max_tasks_per_domain 1000  # Optional: limit for testing

# Verify data conversion
ls -la $HOME/data/tau_bench/
# Should contain: train.parquet, validation.parquet
```

### 5. Testing

Run integration tests to verify everything is working:

```bash
# Run all integration tests
python test_tau_bench_integration.py

# Expected output: All tests passed
```

## Training

### Quick Start

```bash
# Run training with default settings
bash training/run_tau_bench.sh
```

### Custom Training

```bash
# Run training with custom parameters
bash training/run_tau_bench.sh \
  trainer.epochs=100 \
  trainer.train_batch_size=512 \
  generator.n_samples_per_prompt=5 \
  environment.skyrl_gym.tau_bench.user_strategy="react"
```

### Training Configuration

Key configuration options in `training/configs/tau_bench_config.yaml`:

```yaml
# Model settings
trainer.policy.model.path: "Qwen/Qwen2.5-7B-Instruct"

# Training parameters
trainer.epochs: 50
trainer.train_batch_size: 256
trainer.policy.optimizer_config.lr: 1.0e-6

# Environment settings
environment.skyrl_gym.tau_bench.user_strategy: "llm"  # llm, react, verify, reflection
environment.skyrl_gym.tau_bench.user_model: "gpt-4o"
environment.skyrl_gym.tau_bench.max_turns: 20

# Generation settings
generator.max_turns: 20
generator.use_conversation_multi_turn: true
generator.batched: false  # Required for multi-turn conversations
```

## Monitoring

### Weights & Biases

Training metrics are logged to W&B:
- Visit https://wandb.ai/your-username/tau_bench_rl
- Monitor: loss, reward, tool usage accuracy, conversation length

### Local Monitoring

```bash
# Check training progress
tail -f $HOME/ckpts/tau_bench/logs/train.log

# View checkpoints
ls -la $HOME/ckpts/tau_bench/

# View exports
ls -la $HOME/exports/tau_bench/
```

## Environment Details

### Supported Domains

| Domain | Description | Key Tools |
|--------|-------------|-----------|
| airline | Flight bookings, cancellations | `book_reservation`, `cancel_reservation` |
| healthcare | Medical appointments | `schedule_appointment`, `get_patient_info` |
| telecom | Phone services, billing | `get_customer_info`, `process_payment` |
| doordash | Food delivery orders | `search_restaurants`, `create_order` |
| retail | Product orders, returns | `get_order_details`, `return_items` |

### User Simulation Strategies

- **llm**: Standard LLM-based user simulation
- **react**: Reasoning + Acting pattern with explicit thoughts
- **verify**: Multiple attempts with verification
- **reflection**: Self-reflection and improvement

### Reward Calculation

Rewards are calculated based on:
1. **Tool Usage Accuracy**: Comparing agent tools vs ground truth
2. **Database State**: Verification of correct data modifications
3. **Output Requirements**: Checking required information is communicated

## Troubleshooting

### Common Issues

1. **Import Errors**
   ```bash
   # Ensure proper Python path
   export PYTHONPATH=$PYTHONPATH:/path/to/CTU-Agent-v0
   ```

2. **API Key Issues**
   ```bash
   # Test OpenAI API access
   python -c "import openai; print(openai.OpenAI().models.list())"
   ```

3. **Memory Issues**
   ```bash
   # Reduce batch size
   bash training/run_tau_bench.sh trainer.train_batch_size=128
   ```

4. **GPU Issues**
   ```bash
   # Adjust GPU settings
   bash training/run_tau_bench.sh trainer.placement.policy_num_gpus_per_node=4
   ```

### Debugging

Enable verbose logging:
```bash
# Set debug mode
export SKYRL_DEBUG=1

# Run with detailed logging
bash training/run_tau_bench.sh trainer.logger=console
```

## Performance Optimization

### For Limited Resources

```bash
# Smaller model for testing
bash training/run_tau_bench.sh trainer.policy.model.path="Qwen/Qwen2.5-1.5B-Instruct"

# Reduced batch size
bash training/run_tau_bench.sh trainer.train_batch_size=64

# Fewer environment workers
bash training/run_tau_bench.sh environment.skyrl_gym.max_env_workers=8
```

### For High-Performance Training

```bash
# Larger batch size
bash training/run_tau_bench.sh trainer.train_batch_size=512

# More inference engines
bash training/run_tau_bench.sh generator.num_inference_engines=4

# More environment workers
bash training/run_tau_bench.sh environment.skyrl_gym.max_env_workers=32
```

## Architecture

The integration follows these key principles:

1. **Minimal Changes**: No modifications to existing SkyRL or tau_bench code
2. **Clean Integration**: Single environment class handles all domains
3. **Direct Reuse**: Leverages existing tau_bench tools and user simulation
4. **Flexible Configuration**: Easy to modify training parameters and strategies

## Contributing

1. Follow the existing code style and patterns
2. Add tests for new functionality
3. Update documentation for changes
4. Ensure all tests pass before submitting

## Support

For issues related to:
- **SkyRL-Train**: Check [SkyRL documentation](https://skyrl.readthedocs.io/)
- **tau_bench**: Check tau_bench repository
- **Integration**: File issues in this repository

## License

This integration inherits the licenses of both SkyRL and tau_bench projects. 