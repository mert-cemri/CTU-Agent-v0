# Test Evaluation Logs and Storage Locations

## Overview

During training, the system evaluates the model on test datasets (retail and airline) at regular intervals. These evaluations are logged in multiple locations for different purposes.

## Storage Locations

### 1. **WandB (Online Metrics)**
- **Location**: WandB cloud dashboard
- **Projects**: 
  - `tau_bench_rl` (3B model)
  - `tau_bench_rl_7b` (7B model)  
  - `tau_bench_rl_with_taxonomy_feedback` (with LLM Judge)
  - `tau_bench_rl_7b_with_taxonomy_feedback` (7B with LLM Judge)
- **Metrics Logged**:
  - `test-retail/average_reward`
  - `test-retail/success_rate`
  - `test-retail/min_reward`
  - `test-retail/max_reward`
  - `test-airline/average_reward`
  - `test-airline/success_rate`
  - `test-airline/min_reward`
  - `test-airline/max_reward`
- **Frequency**: Every `eval_interval` steps (default: 5 steps)

### 2. **Dumped Evaluation Results (Local Files)**
- **Base Path**: `$HOME/exports/tau_bench/dumped_evals/`
- **Structure**:
  ```
  ~/exports/tau_bench/dumped_evals/
  ├── global_step_5_evals/
  │   ├── test_retail/
  │   │   ├── retail.jsonl          # Individual conversation logs
  │   │   └── aggregated_results.jsonl  # Metrics summary
  │   └── test_airline/
  │       ├── airline.jsonl         # Individual conversation logs
  │       └── aggregated_results.jsonl  # Metrics summary
  ├── global_step_10_evals/
  │   ├── test_retail/
  │   └── test_airline/
  └── ...
  ```

### 3. **JSONL File Contents**

Each `{domain}.jsonl` file contains one line per evaluation sample with:
```json
{
  "input_prompt": "Full conversation prompt with system message",
  "output_response": "Model's generated response",
  "score": 0.0 or 1.0,  // Task completion score
  "stop_reason": "reason for stopping",
  "env_class": "tau_bench",
  "env_extras": {
    "domain": "retail",
    "instruction": "Original user task",
    "ground_truth_actions": [...],
    // Other metadata
  },
  "data_source": "retail"
}
```

The `aggregated_results.jsonl` contains:
```json
{
  "test-retail/average_reward": 0.35,
  "test-retail/success_rate": 0.35,
  "test-retail/num_samples": 100,
  "test-retail/min_reward": 0.0,
  "test-retail/max_reward": 1.0,
  // Plus any additional rollout metrics
}
```

### 4. **Console/Training Logs**
- **Location**: Standard output (terminal) or redirected log file
- **Format**: 
  ```
  [Test retail] Average: 0.350, Success: 0.350
  [Test airline] Average: 0.280, Success: 0.280
  Dumped test results for retail to ~/exports/tau_bench/dumped_evals/global_step_5_evals/test_retail
  ```

### 5. **Checkpoint Metadata**
- **Location**: `$HOME/ckpts/tau_bench/{model_name}/global_step_{N}/metadata.json`
- **Contains**: Last evaluation metrics at checkpoint time

## Configuration

### Enable/Disable Dumping

In `training/configs/tau_bench_config.yaml`:
```yaml
trainer:
  dump_eval_results: true  # Set to false to disable file dumping
  export_path: "${oc.env:HOME}/exports/tau_bench"
```

### Evaluation Frequency

```yaml
trainer:
  eval_interval: 5  # Evaluate every 5 training steps
  eval_before_train: true  # Also evaluate before training starts
```

### Test Datasets Configuration

```yaml
data:
  test_data:
    retail: "training/data/tau_bench_test/retail_test.parquet"
    airline: "training/data/tau_bench_test/airline_test.parquet"
```

## Accessing Logs Programmatically

### Reading JSONL Files
```python
import json
from pathlib import Path

# Read evaluation results
eval_dir = Path.home() / "exports/tau_bench/dumped_evals/global_step_10_evals/test_retail"
with open(eval_dir / "retail.jsonl") as f:
    conversations = [json.loads(line) for line in f]

# Read aggregated metrics
with open(eval_dir / "aggregated_results.jsonl") as f:
    metrics = json.loads(f.readline())
    print(f"Retail success rate: {metrics['test-retail/success_rate']}")
```

### Finding Latest Evaluation
```python
import glob

# Find all evaluation directories
eval_dirs = sorted(glob.glob(str(Path.home() / "exports/tau_bench/dumped_evals/global_step_*_evals")))
latest_eval = eval_dirs[-1] if eval_dirs else None
print(f"Latest evaluation: {latest_eval}")
```

## Trajectory Saving (Optional)

For detailed trajectory logging (including all conversation turns), use the extended trainer:

```python
# In training script
class TauBenchPPOExpWithTrajectories(BasePPOExp):
    def save_trajectories_to_file(self, trajectories, domain, eval_step):
        # Saves detailed conversation trajectories
        filepath = self.trajectory_save_path / f"test_{domain}_trajectories_eval{eval_step:04d}_{timestamp}.json"
```

Configure in YAML:
```yaml
trainer:
  save_test_trajectories: true
  trajectory_save_path: "${oc.env:HOME}/trajectories/tau_bench"
```

## Storage Requirements

- **WandB**: Minimal (metrics only)
- **Dumped Evaluations**: ~10-50 MB per evaluation (depends on test set size)
- **Full Trajectories**: ~100-500 MB per evaluation (if enabled)

## Cleanup

To clean old evaluations:
```bash
# Remove evaluations older than specific step
find ~/exports/tau_bench/dumped_evals -name "global_step_*_evals" -type d | \
  while read dir; do
    step=$(echo $dir | grep -oE '[0-9]+')
    if [ $step -lt 100 ]; then
      rm -rf "$dir"
    fi
  done
```

## Key Insights from Logs

The test evaluation logs help track:
1. **Generalization**: How well the model performs on unseen domains
2. **Training Progress**: Whether test performance improves with training
3. **Overfitting**: If training domains improve while test domains degrade
4. **Failure Analysis**: Individual conversation logs show specific failure modes
5. **LLM Judge Feedback**: When taxonomy feedback is enabled, additional failure mode analysis

## Best Practices

1. **Regular Monitoring**: Check test metrics every few training steps
2. **Early Stopping**: Stop training if test performance degrades consistently
3. **Failure Analysis**: Review low-scoring conversations to identify patterns
4. **Comparison**: Compare vanilla vs taxonomy feedback runs using separate projects
5. **Backup**: Periodically backup important evaluation logs before cleanup