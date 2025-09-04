# Fix for Generation Rewards = 0 Issue

## Root Cause
The primary issue was `zero_reward_on_non_stop: true` in the config file. This setting zeros out ALL rewards if the generation doesn't stop with reason "stop".

## Why This Breaks tau_bench
1. **Multi-turn conversations** often hit the max token limit (stop_reason = "length")
2. **Tool-calling models** may use EOS tokens differently (stop_reason = "eos")
3. **tau_bench rewards** are based on task completion, not generation stopping correctly
4. When `zero_reward_on_non_stop: true`, ALL these valid completions get reward=0

## The Fixes Applied

### 1. **Primary Fix: Disabled zero_reward_on_non_stop**
```yaml
# In training/configs/tau_bench_config.yaml
zero_reward_on_non_stop: false  # Was true, causing all rewards to be 0
```

### 2. **Fixed total_steps Error**
```python
# In SkyRL_mod/skyrl-train/skyrl_train/trainer.py line 220
logger.info(f"[Eval Step {self.global_step}] ...")  # Was self.total_steps
```

### 3. **Set Training Mode Early**
```python
# In training/main_tau_bench.py line 7
os.environ.setdefault("SKYRL_MODE", "train")  # Ensures training mode from start
```

### 4. **REF_MODEL Configuration (Important but separate issue)**
Your script should use:
```bash
POLICY_MODEL="mcemri/qwen2.5_3b_alldata_sft_v0"  # Your SFT model
REF_MODEL="Qwen/Qwen2.5-3B-Instruct"  # Base model (not SFT)
```

## Testing the Fix

Run with debug mode to see rewards:
```bash
export DEBUG_PARSER=1
bash training/run_retail_3b_grpo.sh trainer.train_batch_size=4
```

You should now see:
- Non-zero rewards for successful task completions
- Proper success rates
- Generation metrics being logged correctly

## Why This Wasn't Caught Earlier

The `zero_reward_on_non_stop` setting makes sense for simple single-turn generation tasks where you want exact format following. But for multi-turn tool-use conversations like tau_bench, it's catastrophic because conversations naturally hit length limits or end differently.

## Verification

After these fixes, you should see in the logs:
- `generation/avg_reward` > 0
- `generation/success_rate` > 0 (even if small)
- Individual rewards in the printed examples that aren't all 0