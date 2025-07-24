# Reward Calculation Documentation

This document describes the reward calculation mechanism used in the CTU-Agent-v0 training system, which integrates tau_bench environments with SkyRL for reinforcement learning.

## Overview

The reward calculation is designed to evaluate whether an agent successfully completes a task by:
1. Making correct changes to the environment's data state
2. Communicating required information back to the user

## Reward Structure

- **Type**: Binary reward (0.0 or 1.0)
- **Timing**: Calculated only at episode termination (when `done=True`)
- **During episode**: Reward is always 0.0

## Calculation Process

The reward calculation follows these steps in order:

### 1. Initial State
```python
reward = 1.0  # Start with success assumption
```

### 2. Data Consistency Check

The system verifies that the agent's actions produced the correct changes to the environment's data:

```python
# Get current data state hash after agent's actions
current_data_hash = env.get_data_hash()

# Replay ground truth actions to get expected data state
env.data = env.data_load_func()  # Reset to initial state
for action in task.ground_truth_actions:
    if action.name not in terminate_tools:
        env.step(action)
gt_data_hash = env.get_data_hash()

# Compare hashes
if current_data_hash != gt_data_hash:
    reward = 0.0  # Fail if data state doesn't match
```

### 3. Required Output Verification

If the task specifies required outputs (information that must be communicated to the user):

```python
if len(task.outputs) > 0:
    for output in task.outputs:
        found = False
        for action in agent_actions:
            if action.name == "respond":
                # Case-insensitive check, ignoring commas
                if output.lower() in action.kwargs["content"].lower().replace(",", ""):
                    found = True
                    break
        if not found:
            reward = 0.0  # Fail if any required output is missing
```

## Task Components

### Task.outputs Field
- **Type**: `List[str]`
- **Purpose**: Specifies information that must be communicated to the user
- **Examples**:
  - Reservation numbers: `["23553"]`
  - Prices: `["481.5"]`
  - Product details: `["polyester", "cotton"]`
  - Quantities: `["10"]`
  - Multiple values: `["60", "mastercard"]`

### Output Checking Rules
- **Case-insensitive**: `"MasterCard"` matches `"mastercard"`
- **Comma-agnostic**: `"1,234.56"` matches `"1234.56"`
- **Only in user responses**: Checked only in `respond` actions
- **All required**: Every output must be found for success

## Integration with Training

### Environment Wrapper (tau_bench_env/env.py)
- Delegates reward calculation to tau_bench's native implementation
- Returns reward only when episode ends:
  ```python
  reward = tau_result.reward if done else 0.0
  ```

### SkyRL Training Loop
- Uses these binary rewards for policy optimization
- Applies GRPO (Group Relative Policy Optimization) algorithm
- Tracks success rate metrics for monitoring

## Common Failure Modes

1. **Incorrect Tool Usage**: Agent uses wrong tools or parameters
2. **Missing Communication**: Agent performs correct actions but doesn't tell user the results
3. **Incomplete Information**: Agent mentions some but not all required outputs
4. **Wrong Data State**: Agent's actions don't match expected database changes

## Future Considerations

When modifying reward calculation:
1. Update this document
2. Consider backward compatibility with existing tasks
3. Test with multiple domains
4. Monitor impact on training success rates

## Related Files
- Implementation: `tau_bench/envs/base.py::calculate_reward()`
- Wrapper integration: `tau_bench_env/env.py::step()`
- Type definitions: `tau_bench/tau_types.py`