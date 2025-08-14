# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

**IMPORTANT**: This file should be updated whenever there are significant changes to the system architecture, configuration, or development practices.

## Table of Contents

1. [Project Overview](#project-overview)
2. [System Architecture](#system-architecture)
3. [Core Components](#core-components)
4. [Dataset and Data Pipeline](#dataset-and-data-pipeline)
5. [Training Pipeline](#training-pipeline)
6. [Reward Calculation](#reward-calculation)
7. [Environment Variables and Configuration](#environment-variables-and-configuration)
8. [Development Commands](#development-commands)
9. [Debugging and Monitoring](#debugging-and-monitoring)
10. [Common Issues and Solutions](#common-issues-and-solutions)

## Project Overview

CTU-Agent-v0 is a sophisticated reinforcement learning system that trains language models to effectively use tools in multi-turn conversations. The project integrates:

- **tau_bench**: A multi-domain conversational AI benchmark with tool-use capabilities
- **SkyRL-Train**: A distributed RL training framework from Sky Computing Lab
- **Policy Model**: Qwen/Qwen2.5-3B-Instruct (being trained)
- **User Simulation**: GPT-4o for realistic user behavior

**Primary Objective**: Train language models to correctly use tools across multiple domains (airline, healthcare, telecom, doordash, retail) through reinforcement learning, achieving high task completion rates.

## Guiding Principles

- Always use the simplest and minimalist approach that solves the problem, focus on neat and elegant solutions

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

## Native Tool Calling Integration

**Added**: Native VLLM tool calling support for improved reliability and performance.

### Tool Calling System

The system now supports two approaches for tool calling:

#### 1. Native Tool Calling (Recommended)
- **File**: `tau_bench_env/simple_parser.py`
- **Purpose**: Handles structured OpenAI-compatible tool calling responses from VLLM
- **Configuration**: Set `use_native_tool_calling: true` in environment config
- **VLLM Setup**: Uses `--tool-call-parser hermes` for Qwen models
- **Benefits**: 
  - Clean, structured responses
  - No complex regex parsing
  - Higher reliability
  - Follows OpenAI standard

#### 2. Legacy Text Parsing (Fallback)
- **File**: `tau_bench_env/parser.py` 
- **Purpose**: Complex text parsing for unstructured model outputs
- **Configuration**: Set `use_native_tool_calling: false`
- **When to use**: Only when native tool calling is not available

### Current Status

**Tool calling is prepared but NOT yet active** due to SkyRL architecture limitations:

1. **SkyRL uses remote VLLM servers** (`remote_inference_engine_urls`)
2. **Tool calling requires OpenAI chat completions API** with `tools=` parameter
3. **Current SkyRL generators don't pass tools to VLLM servers**

### Configuration

Currently configured for legacy parsing:

```yaml
environment:
  skyrl_gym:
    tau_bench:
      use_native_tool_calling: false  # Fallback to text parsing
```

### Future Implementation Options

#### Option 1: Manual VLLM Server with Tool Calling
Run VLLM server manually with tool calling:
```bash
vllm serve Qwen/Qwen2.5-3B-Instruct \
    --enable-auto-tool-choice \
    --tool-call-parser hermes \
    --port 8001
```

Then modify SkyRL to use OpenAI client instead of direct generation.

#### Option 2: Extend SkyRL VLLM Integration
Modify `skyrl_train/inference_engines/vllm/vllm_engine.py` to:
- Support OpenAI chat completions API
- Pass tools from environment to generation calls
- Handle structured tool calling responses

### Current Approach

The system falls back to the robust text parser (`tau_bench_env/parser.py`) which handles the malformed outputs we observed, making training functional while we work on native tool calling integration.

This improvement significantly reduces the complex text parsing overhead and makes tool calling more reliable.

## LLaMA-Factory Integration

### Overview

The repository includes **LLaMA-Factory** (`sft/LLaMA-Factory/`), a comprehensive fine-tuning framework for large language models. While currently standalone, it provides infrastructure for supervised fine-tuning (SFT) that could complement the RL training pipeline.

### LLaMA-Factory Components

#### Core Features
- **Model Support**: 100+ models including LLaMA, Qwen, Mistral, DeepSeek, Yi, Gemma, ChatGLM, Phi
- **Training Methods**: Pre-training, SFT, DPO, PPO, KTO, ORPO, reward modeling
- **Optimization**: LoRA, QLoRA (2-8 bit), full-tuning, freeze-tuning
- **Advanced Algorithms**: GaLore, BAdam, APOLLO, Adam-mini, Muon, DoRA, LongLoRA, PiSSA
- **Performance**: FlashAttention-2, Unsloth, Liger Kernel, RoPE scaling

#### Directory Structure
```
sft/LLaMA-Factory/
├── src/llamafactory/       # Core training library
│   ├── api/                # OpenAI-style API server
│   ├── chat/               # Chat inference engines (HF, vLLM, SGLang)
│   ├── data/               # Data loading and preprocessing
│   ├── model/              # Model utilities and adapters
│   ├── train/              # Training workflows (SFT, DPO, PPO, etc.)
│   └── webui/              # Gradio-based GUI (LLaMA Board)
├── examples/               # Training configurations
│   ├── train_lora/         # LoRA fine-tuning examples
│   ├── train_full/         # Full fine-tuning examples
│   └── inference/          # Inference configurations
├── data/                   # Dataset definitions and samples
└── scripts/                # Utility scripts
```

#### Key Capabilities

1. **Multi-Modal Support**
   - Text, image, video, and audio understanding
   - Tool calling and function calling support
   - Multi-turn dialogue handling

2. **Flexible Training**
   - YAML-based configuration system
   - Support for custom datasets via `dataset_info.json`
   - Both CLI and Web UI interfaces

3. **Inference Options**
   - OpenAI-compatible API server
   - vLLM and SGLang backends for fast inference
   - Gradio UI for interactive testing

### Potential Integration Points with CTU-Agent

While LLaMA-Factory is currently standalone in this repository, it could potentially be integrated to provide:

1. **Initial SFT Phase**
   - Pre-train models on tau_bench demonstrations before RL
   - Create better initialization for PPO/GRPO training
   - Fine-tune on successful trajectories from RL training

2. **Alternative Training Pipeline**
   - Use LLaMA-Factory's PPO implementation as comparison
   - Leverage its DPO/KTO methods for preference learning
   - Utilize its efficient LoRA/QLoRA for larger models

3. **Data Processing**
   - Convert tau_bench data to LLaMA-Factory format
   - Use its data preprocessing pipeline for cleaning
   - Leverage its multi-modal data handling

4. **Inference Infrastructure**
   - Deploy trained models via LLaMA-Factory's API server
   - Use its vLLM integration for production serving
   - Leverage Web UI for model evaluation

### Current Status

- **Standalone**: LLaMA-Factory is present but not actively integrated
- **Ready to Use**: Full framework available for SFT experiments
- **Complementary**: Could enhance the RL pipeline with SFT capabilities

### Usage Example

To use LLaMA-Factory for SFT on tau_bench data:

1. Convert tau_bench data to LLaMA-Factory format
2. Add dataset entry to `data/dataset_info.json`
3. Create training config in `examples/`
4. Run training via CLI or Web UI

```bash
# Example: LoRA fine-tuning on Qwen2.5
cd sft/LLaMA-Factory
llamafactory-cli train examples/train_lora/qwen2_lora_sft.yaml

# Or use the Web UI
llamafactory-cli webui
```