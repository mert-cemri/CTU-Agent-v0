# LLM Judge (Taxonomy Feedback) Integration Guide

## Overview

The CTU-Agent-v0 system now supports LLM Judge evaluation using the MAST taxonomy to provide granular reward feedback during RL training. This enables the model to receive detailed feedback on 14 different failure modes throughout conversations, not just at completion.

## Key Features

- **Granular Rewards**: Receive feedback at every conversation step
- **14 Failure Modes**: MAST taxonomy covers task compliance, communication, and verification issues
- **Configurable Weight**: Alpha hyperparameter to balance judge rewards with task completion
- **Separate Tracking**: Runs with taxonomy feedback get their own wandb projects
- **Cost Control**: Uses GPT-4o-mini for efficient evaluation

## Configuration

### Environment Variables

```bash
# Enable/disable taxonomy feedback (required)
export TAXONOMY_FEEDBACK=true

# Weight for judge rewards (optional, default: 1.0)
export TAXONOMY_ALPHA=0.5

# OpenAI API key for LLM judge (required when enabled)
export OPENAI_API_KEY=your_openai_api_key_here

# Enable debug logging (optional)
export DEBUG_PARSER=1
```

### Training Script Usage

For **3B model**:
```bash
# With taxonomy feedback
TAXONOMY_FEEDBACK=true TAXONOMY_ALPHA=0.3 bash training/run_multi_domain.sh

# Without taxonomy feedback (vanilla training)
bash training/run_multi_domain.sh
```

For **7B model**:
```bash
# With taxonomy feedback
TAXONOMY_FEEDBACK=true TAXONOMY_ALPHA=0.5 bash training/run_multi_domain_7b_optimized.sh

# Without taxonomy feedback (vanilla training)  
bash training/run_multi_domain_7b_optimized.sh
```

## Reward Formula

The final reward calculation is:
```
final_reward = base_reward + alpha * (1 / total_failures)
```

Where:
- `base_reward`: Original tau-bench reward (0.0 intermediate, 0-1 final)
- `alpha`: Weighting hyperparameter (configurable)
- `total_failures`: Number of MAST taxonomy failures detected (0-14)

### Reward Examples

With `alpha=0.5`:
- Perfect conversation (0 failures): +0.5 bonus
- Good conversation (2 failures): +0.25 bonus  
- Poor conversation (10 failures): +0.05 bonus
- Very poor conversation (14 failures): +0.036 bonus

## WandB Project Organization

When taxonomy feedback is enabled, runs will be tracked in separate projects:

- **Without taxonomy feedback**: `tau_bench_rl` (3B), `tau_bench_rl_7b` (7B)
- **With taxonomy feedback**: `tau_bench_rl_with_taxonomy_feedback` (3B), `tau_bench_rl_7b_with_taxonomy_feedback` (7B)

This allows clear separation and comparison between vanilla and enhanced training runs.

## MAST Taxonomy Categories

### Category 1: Task & Role Compliance
- 1.1 Disobey Task Specification
- 1.2 Disobey Role Specification  
- 1.3 Step Repetition
- 1.4 Loss of Conversation History
- 1.5 Unaware of Termination Conditions

### Category 2: Communication & Coordination  
- 2.1 Conversation Reset
- 2.2 Fail to Ask for Clarification
- 2.3 Task Derailment
- 2.4 Information Withholding
- 2.5 Ignored Other Agent's Input
- 2.6 Action-Reasoning Mismatch

### Category 3: Verification & Completion
- 3.1 Premature Termination
- 3.2 No or Incorrect Verification
- 3.3 Weak Verification

## Implementation Details

### Files Modified/Added

1. **`llm_judge.py`**: Core MAST taxonomy evaluation using GPT-4o-mini
2. **`tau_bench_env/llm_judge_integration.py`**: Integration wrapper for tau-bench
3. **`tau_bench_env/env.py`**: Environment with judge reward integration
4. **`SkyRL_mod/skyrl-train/skyrl_train/utils/tracking.py`**: Wandb project naming logic
5. **Training scripts**: Updated with taxonomy feedback parameters

### Debug Information

When `DEBUG_PARSER=1`, you'll see detailed logging:

```
🏛️ LLM JUDGE EVALUATION:
   Total failures: 3
   Alpha weight: 0.5
   Raw bonus: 0.333
   Weighted bonus: 0.167
   Summary: Agent failed to ask clarification and showed weak verification...
```

### Error Handling

- Graceful fallback if OpenAI API fails (bonus = 0.0)
- Malformed tool calls handled safely in trace formatting
- Network errors logged but don't crash training

## Best Practices

### Recommended Alpha Values
- **Conservative**: 0.1-0.3 (small judge influence)
- **Balanced**: 0.5-0.7 (moderate judge influence) 
- **Aggressive**: 0.8-1.0 (strong judge influence)

### Cost Management
- Uses GPT-4o-mini (~$0.15/1M input tokens, ~$0.60/1M output tokens)
- Each evaluation ~500-1000 tokens input + 200-500 tokens output
- Estimated cost: ~$0.0005-0.001 per conversation step

### Performance Considerations
- Each LLM judge call adds ~1-3 seconds per step
- API rate limits may slow training with high parallelism
- Consider alpha tuning based on your specific domains

## Troubleshooting

### Common Issues

1. **"OpenAI API key is required" error**
   ```bash
   export OPENAI_API_KEY=your_key_here
   ```

2. **Taxonomy feedback not enabled**
   ```bash
   export TAXONOMY_FEEDBACK=true
   # Check that it appears in your training logs
   ```

3. **Wrong wandb project name**
   - Check that taxonomy feedback is properly detected
   - Verify environment variable is set before training starts

4. **Judge evaluation errors**
   ```bash
   export DEBUG_PARSER=1  # Enable detailed logging
   # Check logs for specific error messages
   ```

### Verification

To verify taxonomy feedback is working:

1. Check wandb project name includes `_with_taxonomy_feedback`
2. Look for judge reward metadata in training logs
3. Monitor `judge_reward_bonus` and `taxonomy_alpha` in metrics
4. Debug logs should show evaluation details when `DEBUG_PARSER=1`

## Example Training Command

Complete example with all parameters:

```bash
#!/bin/bash
export WANDB_API_KEY=your_wandb_key
export OPENAI_API_KEY=your_openai_key
export TAXONOMY_FEEDBACK=true
export TAXONOMY_ALPHA=0.5
export DEBUG_PARSER=1

# Run 3B training with taxonomy feedback
bash training/run_multi_domain.sh
```

This will create a run in the `tau_bench_rl_with_taxonomy_feedback` project with alpha-weighted judge rewards throughout training.