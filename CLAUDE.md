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