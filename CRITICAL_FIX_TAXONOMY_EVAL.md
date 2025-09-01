# CRITICAL FIX: Taxonomy Feedback Should Not Apply During Evaluation

## Problem
When TAXONOMY_FEEDBACK is enabled, the LLM Judge was providing reward bonuses during BOTH training AND evaluation. This inflated evaluation metrics and made them invalid for comparing model performance.

## The Issue
- During training: LLM Judge rewards SHOULD be applied (this helps the model learn)
- During evaluation: LLM Judge rewards SHOULD NOT be applied (we want pure task performance)
- Before fix: Judge rewards were ALWAYS applied when TAXONOMY_FEEDBACK=true

## Solution Implemented

### 1. Environment Check (`tau_bench_env/env.py`)
```python
# Only apply judge rewards during training, not evaluation
is_training = os.environ.get("SKYRL_MODE", "train") == "train"
if self.llm_judge and self.llm_judge.enabled and is_training:
    # Apply judge rewards
```

### 2. Training Mode Setting (`SkyRL_mod/skyrl-train/skyrl_train/trainer.py`)
```python
# In eval() function:
os.environ["SKYRL_MODE"] = "eval"  # Disable judge rewards

# After eval() and in train():
os.environ["SKYRL_MODE"] = "train"  # Enable judge rewards
```

## Impact
- **Training**: Model still gets taxonomy feedback to improve learning
- **Evaluation**: Pure task performance without inflated rewards
- **Fair Comparison**: Vanilla vs Taxonomy models can now be compared fairly

## Verification
After this fix, evaluation success rates should be:
- Similar between vanilla and taxonomy models (since eval doesn't use judge)
- Lower than what you saw before (no more inflated rewards)
- A true measure of task completion performance

## Important Notes
1. This fix is CRITICAL for valid model comparison
2. Any evaluation results before this fix are invalid
3. Training with taxonomy feedback still works as intended
4. The fix only affects evaluation/test time behavior