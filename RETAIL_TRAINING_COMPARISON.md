# Retail Domain Training Comparison Guide

## Overview

Four training scripts for comparing vanilla GRPO vs GRPO with taxonomy feedback on the retail domain.

## Training Scripts

### 1. **3B Model - Vanilla GRPO** (`run_retail_3b_grpo.sh`)
- **Model**: Qwen/Qwen2.5-3B-Instruct
- **Method**: Standard GRPO rewards (0/1 for task completion)
- **WandB Project**: `tau_bench_retail_grpo`
- **Checkpoints**: `~/ckpts/tau_bench/Qwen_Qwen2.5-3B-Instruct_retail_grpo_vanilla/`

### 2. **3B Model - GRPO + Taxonomy** (`run_retail_3b_grpo_taxonomy.sh`)
- **Model**: Qwen/Qwen2.5-3B-Instruct
- **Method**: GRPO + LLM Judge feedback (granular rewards)
- **Alpha**: 0.3 (conservative weight for judge rewards)
- **WandB Project**: `tau_bench_retail_grpo_with_taxonomy_feedback`
- **Checkpoints**: `~/ckpts/tau_bench/Qwen_Qwen2.5-3B-Instruct_retail_grpo_taxonomy/`

### 3. **7B Model - Vanilla GRPO** (`run_retail_7b_grpo.sh`)
- **Model**: Qwen/Qwen2.5-7B-Instruct
- **Method**: Standard GRPO rewards (0/1 for task completion)
- **Memory Optimized**: Yes (CPU offloading, reduced batch sizes)
- **WandB Project**: `tau_bench_retail_grpo_7b`
- **Checkpoints**: `~/ckpts/tau_bench/Qwen_Qwen2.5-7B-Instruct_retail_grpo_vanilla/`

### 4. **7B Model - GRPO + Taxonomy** (`run_retail_7b_grpo_taxonomy.sh`)
- **Model**: Qwen/Qwen2.5-7B-Instruct
- **Method**: GRPO + LLM Judge feedback (granular rewards)
- **Alpha**: 0.5 (moderate weight for judge rewards)
- **Memory Optimized**: Yes (CPU offloading, reduced batch sizes)
- **WandB Project**: `tau_bench_retail_grpo_7b_with_taxonomy_feedback`
- **Checkpoints**: `~/ckpts/tau_bench/Qwen_Qwen2.5-7B-Instruct_retail_grpo_taxonomy/`

## Usage

### Basic Usage

```bash
# 1. Vanilla GRPO - 3B Model
bash training/run_retail_3b_grpo.sh

# 2. GRPO + Taxonomy - 3B Model
export OPENAI_API_KEY="your_actual_key"
bash training/run_retail_3b_grpo_taxonomy.sh

# 3. Vanilla GRPO - 7B Model
bash training/run_retail_7b_grpo.sh

# 4. GRPO + Taxonomy - 7B Model
export OPENAI_API_KEY="your_actual_key"
bash training/run_retail_7b_grpo_taxonomy.sh
```

### Adjusting Taxonomy Alpha

```bash
# Conservative weight (less judge influence)
TAXONOMY_ALPHA="0.1" bash training/run_retail_3b_grpo_taxonomy.sh

# Moderate weight (balanced)
TAXONOMY_ALPHA="0.5" bash training/run_retail_3b_grpo_taxonomy.sh

# Aggressive weight (strong judge influence)
TAXONOMY_ALPHA="1.0" bash training/run_retail_3b_grpo_taxonomy.sh
```

## Key Differences

### Reward Mechanism

**Vanilla GRPO**:
- Binary rewards: 0 for failure, 1 for success
- Only evaluates final task completion
- No intermediate feedback

**GRPO + Taxonomy**:
- Formula: `base_reward + alpha * (1 / total_failures)`
- Evaluates 14 failure modes continuously
- Provides granular feedback at each step

### Expected Outcomes

**Vanilla GRPO**:
- ✅ Simpler training dynamics
- ✅ Lower computational cost (no LLM judge)
- ❌ May struggle with partial successes
- ❌ No feedback on conversation quality

**GRPO + Taxonomy**:
- ✅ Better conversation quality
- ✅ Learns from partial successes
- ✅ Reduces specific failure modes
- ❌ Higher computational cost (OpenAI API calls)
- ❌ More complex reward landscape

## Hyperparameter Comparison

| Parameter | 3B Vanilla | 3B Taxonomy | 7B Vanilla | 7B Taxonomy |
|-----------|------------|-------------|------------|-------------|
| **Batch Size** | 64 | 64 | 32 | 32 |
| **Mini Batch** | 16 | 16 | 8 | 8 |
| **Learning Rate** | 3e-7 | 3e-7 | 2e-7 | 2e-7 |
| **KL Coefficient** | 0.02 | 0.02 | 0.01 | 0.01 |
| **Eval Interval** | 5 | 5 | 10 | 10 |
| **Samples/Prompt** | 5 | 5 | 3 | 3 |
| **Temperature** | 0.9 | 0.9 | 0.8 | 0.8 |
| **GPU Memory** | 0.8 | 0.8 | 0.75 | 0.75 |
| **Max Context** | 32768 | 32768 | 16384 | 16384 |
| **CPU Offload** | No | No | Yes | Yes |
| **Gradient Checkpointing** | No | No | Yes | Yes |

## Monitoring Training

### WandB Metrics to Compare

1. **Training Efficiency**:
   - `train/avg_reward`: Average reward per batch
   - `generation/success_rate`: Task completion rate
   - `timing/step`: Time per training step

2. **Conversation Quality** (Taxonomy only):
   - `judge_reward_bonus`: Additional reward from judge
   - `taxonomy_alpha`: Weight used for judge rewards
   - Individual failure mode counts (if logged)

3. **Validation Performance**:
   - `eval/all/avg_score`: Overall validation score
   - `eval/all/success_rate`: Validation success rate

### Expected Training Curves

**Vanilla GRPO**:
- Steep initial improvement
- May plateau around 30-40% success rate
- Consistent training dynamics

**GRPO + Taxonomy**:
- Gradual, steady improvement
- Higher final performance (expected 40-50% success rate)
- More stable training with less variance

## Cost Considerations

### Vanilla GRPO
- **GPU Cost**: ~$X per hour (8 GPUs)
- **API Cost**: $0 (no LLM judge)
- **Total**: GPU cost only

### GRPO + Taxonomy
- **GPU Cost**: ~$X per hour (8 GPUs)
- **OpenAI API Cost**: ~$5-10 per 1000 training steps
- **Total**: GPU + API costs

## Experiment Design

### Recommended Comparison Protocol

1. **Baseline Run**: Start with vanilla GRPO for both models
2. **Taxonomy Runs**: Try different alpha values (0.1, 0.3, 0.5, 1.0)
3. **Evaluation**: Compare on same test set after equal training steps
4. **Analysis**: Review failure modes reduced by taxonomy feedback

### Success Metrics

Compare models on:
1. **Task Success Rate**: % of conversations completing the task
2. **Average Reward**: Mean reward across all conversations
3. **Failure Mode Distribution**: Which errors are most common
4. **Conversation Length**: Steps to task completion
5. **Tool Use Accuracy**: Correct tool calls vs errors

## Troubleshooting

### Common Issues

1. **OPENAI_API_KEY not set**:
   ```bash
   export OPENAI_API_KEY="sk-..."
   ```

2. **GPU OOM on 7B model**:
   - Reduce `generator.gpu_memory_utilization` to 0.7
   - Reduce `trainer.train_batch_size` to 16
   - Ensure CPU offloading is enabled

3. **Slow training with taxonomy**:
   - Reduce `generator.n_samples_per_prompt` to 3
   - Increase `trainer.eval_interval` to 10
   - Use smaller alpha to reduce API calls

4. **WandB project confusion**:
   - Vanilla runs → base project name
   - Taxonomy runs → project name + "_with_taxonomy_feedback"

## Next Steps

After training:
1. Export models: Check `~/exports/tau_bench_retail/`
2. Compare WandB runs side-by-side
3. Run evaluation on held-out test sets
4. Analyze conversation logs in `~/exports/tau_bench_retail/dumped_evals/`
5. Fine-tune alpha based on results