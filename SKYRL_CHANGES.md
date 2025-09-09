# SkyRL Repository Changes for CTU-Agent-v0 Training Framework

## Date: 2025-01-09

### Section 23: Support for Qwen3-8B Model with Thinking Mode Disabled

#### Purpose
Enable support for Qwen/Qwen3-8B model and disable thinking mode in the tokenizer to prevent errors during training.

#### Changes Made

##### 1. Updated Training Script
**File**: `/training/run_retail_8b_grpo_taxonomy.sh`
- Changed model from `Qwen/Qwen3-8B-Base` to `Qwen/Qwen3-8B`
- Reason: Base model doesn't have proper chat template support

##### 2. Added Thinking Mode Disable Support
**File**: `/SkyRL_mod/skyrl-train/skyrl_train/generators/skyrl_gym_generator.py`

###### Added Helper Method (Lines 54-66)
```python
# Check if model is Qwen3 and needs thinking mode disabled
self.is_qwen3_model = 'Qwen3' in getattr(tokenizer, 'name_or_path', '') or 'Qwen/Qwen3' in model_name

def _apply_chat_template(self, messages, add_generation_prompt=True, tokenize=True, **kwargs):
    """Helper method to apply chat template with enable_thinking=False for Qwen3 models"""
    if self.is_qwen3_model:
        kwargs["enable_thinking"] = False
    return self.tokenizer.apply_chat_template(
        messages,
        add_generation_prompt=add_generation_prompt,
        tokenize=tokenize,
        **kwargs
    )
```

###### Updated All apply_chat_template Calls
Replaced all instances of `self.tokenizer.apply_chat_template()` with `self._apply_chat_template()` at the following lines:
- Line 113: Initial prompt tokenization
- Line 202: Response encoding with custom template
- Line 330: Prompt token IDs generation
- Line 519: Previous template state
- Line 532: Re-apply chat template after adding responses
- Line 540: Current template computation
- Lines 594, 597: Observation encoding

#### Why These Changes?

1. **Qwen3 Models Have Thinking Mode**: By default, Qwen3 models use a "thinking mode" which adds internal reasoning tokens. This causes issues during tool-calling tasks in tau-bench.

2. **enable_thinking=False**: This parameter disables the thinking mode, making the model responses more direct and compatible with the tau-bench environment.

3. **Centralized Helper Method**: Instead of modifying each call individually, we created a helper method that automatically adds `enable_thinking=False` for Qwen3 models.

#### Testing
After these changes, the model should:
- Properly handle chat templates without thinking tokens
- Work correctly with tau-bench tool-calling tasks
- Not produce the `IndexError: list index out of range` error

#### Rollback Instructions
To rollback these changes:
1. In the training script, change back to `Qwen/Qwen3-8B-Base` if needed
2. In skyrl_gym_generator.py:
   - Remove the `_apply_chat_template` helper method (lines 57-66)
   - Remove the `self.is_qwen3_model` initialization (lines 54-55)
   - Replace all `self._apply_chat_template()` calls with `self.tokenizer.apply_chat_template()`

---

# SkyRL Repository Changes for CTU-Agent-v0 Training Framework

This document lists all changes made to the SkyRL repository (`SkyRL_mod/skyrl-train/`) to support the CTU-Agent-v0 multi-domain training framework.

## Overview of Changes

The implementation includes native VLLM tool calling, multi-domain training support, improved WandB logging, robust error handling, and hyperparameter optimization for better generalization. All changes maintain backward compatibility.

## Latest Changes (Section 16): Hyperparameter Optimization for Better Generalization

### Problem
The model was overfitting to training domains (telecom, healthcare, doordash) while showing poor performance on held-out domains (retail, airline). This is a classic domain generalization challenge in multi-domain RL.

### Solution
Adjusted hyperparameters to improve generalization through:

1. **Stronger Regularization**
   - Increased KL loss coefficient: `0.001 → 0.01` (10x)
   - Increased weight decay: `0.01 → 0.05` (5x)
   - Added KL coefficient in training script: `0.02`

2. **More Conservative Updates**
   - Reduced learning rate: `1e-6 → 5e-7` (config), `5e-6 → 3e-7` (script)
   - Reduced PPO clip range: `0.2 → 0.1`
   - Reduced value clip: `0.2 → 0.1`
   - Reduced max gradient norm: `1.0 → 0.5`
   - Added warmup steps: `0 → 50` (config), `100 → 200` (script)

3. **Smaller Batch Sizes**
   - Reduced train batch size: `128 → 64`
   - Reduced mini batch size: `32 → 16`
   - Reduced eval batch size: `64 → 32`

4. **More Exploration**
   - Increased samples per prompt: `3 → 5`
   - Adjusted temperature: `0.7 → 0.8` (config), `1.0 → 0.9` (script)
   - Increased top_p: `0.9 → 0.95`
   - Reduced eval frequency: `2 → 3` steps

### Files Changed
- **`training/configs/tau_bench_config.yaml`**: Updated algorithm, optimizer, and sampling parameters
- **`training/run_tau_bench.sh`**: Adjusted batch sizes, learning rates, and exploration settings

### Expected Improvements
- Better generalization to unseen domains through regularization
- More stable training with conservative updates
- Increased exploration to discover domain-invariant strategies
- Reduced overfitting with smaller batches and stronger regularization

---

## Section 15: Simplified WandB Logging System

### Problem
Only generation metrics were appearing in WandB despite multiple logging attempts throughout the training loop. The system had 9 separate `total_steps` increments per training iteration, causing step count inflation and logging failures.

### Solution
Replaced fragmented logging with unified collection system:

```python
# Before: Multiple increments and individual logging attempts
self.total_steps += 1  # 9 different locations
self.tracker.log(metrics, step=self.total_steps)

# After: Single collection and unified logging
self.all_metrics.update(metrics)  # Collect all metrics
self.tracker.log(self.all_metrics, step=self.global_step)  # Log once per step
```

### Files Changed
- **`trainer.py`**: Removed `total_steps` counter, unified all metric collection into `self.all_metrics`, single logging call per training step using `global_step`

### Metrics Now Properly Logged
- **Generation metrics**: `generation/avg_reward`, `generation/success_rate`
- **Training metrics**: `train/avg_reward`, `train/min_reward`, `train/max_reward`
- **Batch metrics**: `reward/avg_raw_reward`, `reward/parse_failure_rate`
- **Evaluation metrics**: `eval/all/avg_score`, `eval-retail/success_rate`
- **Test metrics**: `test-retail/average_reward`, `test-airline/average_reward`
- **Loss metrics**: `loss/avg_raw_rewards`, `loss/avg_raw_advantages`
- **Timing metrics**: `timing/step`, `timing/generate`

### Logging Frequency
- **Every training step**: Generation, training, batch, loss, timing metrics
- **Every eval_interval (5 steps)**: Evaluation and test metrics  
- **Global step**: Single monotonic counter aligned with actual training progress

---

## 1. Base Types (`skyrl_train/inference_engines/base.py`)

### Changes Made

**ADDED** two new optional fields to `InferenceEngineInput` TypedDict:

```python
class InferenceEngineInput(TypedDict):
    # Either prompts or prompt_token_ids must be provided, but not both.
    prompts: Optional[List[ConversationType]]
    prompt_token_ids: Optional[List[List[int]]]
    sampling_params: Optional[Dict[str, Any]]
    trajectory_ids: Optional[List[Hashable]]
    # Tool calling support
    tools: Optional[List[Dict[str, Any]]]
    use_native_tool_calling: Optional[bool]
```

### Reason for Changes

- **`tools`**: Allows passing OpenAI-format tool definitions from environment through generator to inference engine
- **`use_native_tool_calling`**: Flag to indicate whether the engine should use VLLM's `chat()` method with tools or traditional `generate()` method
- These fields are optional to maintain backward compatibility with existing code

---

## 2. Generator (`skyrl_train/generators/skyrl_gym_generator.py`)

### Changes Made

#### A. Constructor Modification

**ADDED** new attribute in `__init__()` method:

```python
def __init__(
    self,
    generator_cfg: DictConfig,
    skyrl_gym_cfg: DictConfig,
    inference_engine_client: InferenceEngineClient,
    tokenizer: PreTrainedTokenizer,
    model_name: str,
):
    # ... existing code ...
    self.use_native_tool_calling = generator_cfg.get("use_native_tool_calling", False)
```

#### B. agent_loop() Method Update

**MODIFIED** tool information collection and inference engine input:

```python
# Existing code that collects tools
tools = None
use_native_tool_calling = False
if env_info and isinstance(env_info, dict):
    tools = env_info.get('tools')
    use_native_tool_calling = env_info.get('use_native_tool_calling', False) and self.use_native_tool_calling

# Modified inference_engine_input creation
inference_engine_input = InferenceEngineInput(
    prompts=messages,
    trajectory_ids=uids,
    sampling_params=sampling_params,
    tools=tools,  # ADDED
    use_native_tool_calling=use_native_tool_calling  # ADDED
)
```

### Reason for Changes

- Enables generator to detect when environments provide tools and want native tool calling
- Passes tool information through to inference engines that support it
- Only activates when both environment AND generator config enable native tool calling

---

## 3. Ray Wrapped Inference Engine (`skyrl_train/inference_engines/ray_wrapped_inference_engine.py`)

### Changes Made

#### A. Version Check Update

**MODIFIED** VLLM version assertion to use semantic versioning:

```python
from packaging.version import Version  # ADDED import

# Changed from string comparison to semantic version comparison
assert Version(vllm.__version__) >= Version("0.8.3"), f"SkyRL only supports vLLM >= 0.8.3, got {vllm.__version__}"
```

#### B. generate() Method Enhancement

**ADDED** native tool calling support:

```python
async def generate(self, inference_engine_input: InferenceEngineInput) -> InferenceEngineOutput:
    # ... existing code ...
    
    # ADDED: Native tool calling support
    if inference_engine_input.get("use_native_tool_calling", False) and inference_engine_input.get("tools"):
        # Use chat() method with tools
        chat_responses = await self.llm_engine.chat(
            messages=prompts,
            sampling_params=sampling_params,
            tools=inference_engine_input["tools"]
        )
        
        # Extract response_ids from ChatCompletionResponse objects
        response_ids = []
        for resp in chat_responses:
            if resp.outputs and len(resp.outputs) > 0:
                # Get token IDs from the first output
                token_ids = resp.outputs[0].token_ids
                response_ids.append(token_ids)
            else:
                response_ids.append([])
    else:
        # Original text generation path
        responses = await self.llm_engine.generate(
            prompts=generate_prompts,
            sampling_params=sampling_params,
            prompt_token_ids=prompt_token_ids
        )
        response_ids = [resp.outputs[0].token_ids for resp in responses]
```

### Reason for Changes

- Enables VLLM's native chat() method when tools are provided
- Falls back to standard generate() for non-tool scenarios
- Extracts token IDs properly from ChatCompletionResponse format

---

## 4. Remote Inference Engine (`skyrl_train/inference_engines/remote_inference_engine.py`)

### Changes Made

**ADDED** pass-through of tool calling parameters:

```python
async def generate(self, inference_engine_input: InferenceEngineInput) -> InferenceEngineOutput:
    # ... existing code ...
    
    # Handle prompts/prompt_token_ids
    request_data = {
        "prompts": prompts,
        "sampling_params": sampling_params,
        # ADDED: Pass through tool calling parameters
        "tools": inference_engine_input.get("tools"),
        "use_native_tool_calling": inference_engine_input.get("use_native_tool_calling", False)
    }
```

### Reason for Changes

- Ensures remote inference engines receive tool calling information
- Maintains compatibility with both local and remote deployment scenarios

---

## 5. Environment Registration (`training/main_tau_bench.py`)

### Changes Made

**ADDED** tau_bench environment registration in skyrl_entrypoint:

```python
@ray.remote(num_cpus=1)
def skyrl_entrypoint(cfg: DictConfig):
    # ... existing code ...
    
    # Register the tau_bench environment
    # This needs to be done inside the entrypoint task
    register(
        id="tau_bench",
        entry_point="tau_bench_env.env:TauBenchEnv",
    )
    
    # Run the training experiment
    exp = BasePPOExp(cfg)
    exp.run()
```

### Reason for Changes

- Ensures tau_bench environment is registered in Ray worker processes
- Required for SkyRL's environment lookup mechanism

---

## 6. Test Sets for Evaluation

### Changes Made

#### A. Added get_test_datasets() method to BasePPOExp (main_base.py)

```python
def get_test_datasets(self):
    """Load test datasets for evaluation."""
    test_datasets = {}
    if (self.cfg.trainer.eval_interval > 0 and 
        hasattr(self.cfg.data, 'test_data') and 
        self.cfg.data.test_data):
        
        for name, path in self.cfg.data.test_data.items():
            if path and os.path.exists(path):
                test_dataset = PromptDataset(
                    [path],
                    self.tokenizer,
                    self.cfg.trainer.max_prompt_length,
                    num_processors=8,
                )
                test_datasets[name] = test_dataset
                logger.info(f"Loaded test dataset '{name}' from {path}")
            else:
                logger.warning(f"Test dataset '{name}' not found at {path}")
    
    return test_datasets
```

#### B. Updated _setup_trainer() to load test datasets

```python
# Set test datasets if available
test_datasets = self.get_test_datasets()
if test_datasets:
    trainer.set_test_datasets(test_datasets)
```

### Reason for Changes

- Enables evaluation on separate test sets during training
- Tracks generalization performance on held-out domains

---

## 7. Multi-Domain Training Support

### Changes Made

#### A. Added retail validation dataset support (main_base.py)

```python
def get_retail_eval_dataset(self):
    """Initializes the retail evaluation dataset for multi-domain training."""
    if (self.cfg.trainer.eval_interval > 0 and 
        hasattr(self.cfg.data, 'retail_val_data') and 
        self.cfg.data.retail_val_data):
        prompts_dataset = PromptDataset(
            self.cfg.data.retail_val_data,
            self.tokenizer,
            self.cfg.trainer.max_prompt_length,
            num_processors=8,
        )
        return prompts_dataset
    return None
```

#### B. Updated trainer setup to include retail eval

```python
# Set retail eval dataset if available (for multi-domain training)
if self.retail_eval_dataset is not None:
    trainer.set_retail_eval_dataset(self.retail_eval_dataset)
```

### Reason for Changes

- Enables tracking performance on retail domain during multi-domain training
- Provides additional validation metric for generalization

---

## 8. Trainer Enhancements

### Changes Made

#### A. Added test dataset support (trainer.py)

```python
def set_test_datasets(self, test_datasets: Dict[str, PromptDataset]):
    """Set test datasets for evaluation during training."""
    self.test_datasets = test_datasets
    self.test_dataloaders = {}
    for name, dataset in test_datasets.items():
        self.test_dataloaders[name] = self.build_dataloader(dataset, is_train=False)
```

#### B. Added test evaluation in eval() method

```python
# Evaluate on test datasets if available
if hasattr(self, 'test_datasets') and self.test_datasets:
    for test_name, test_dataloader in self.test_dataloaders.items():
        logger.info(f"Evaluating on test set: {test_name}")
        # ... evaluation logic ...
        test_metrics = {
            f"test-{test_name}/average_reward": float(np.mean(test_rewards)),
            f"test-{test_name}/success_rate": float(np.mean([r > 0 for r in test_rewards])),
            # ... other metrics ...
        }
        eval_metrics.update(test_metrics)
```

### Reason for Changes

- Provides comprehensive evaluation during training
- Tracks performance on multiple test domains

---

## 9. Configuration Updates

### Changes Made

#### A. Added test data configuration (tau_bench_config.yaml)

```yaml
data:
  train_data: ["${oc.env:HOME}/data/tau_bench/train.parquet"]
  val_data: ["${oc.env:HOME}/data/tau_bench/validation.parquet"]
  retail_val_data: null  # Optional: retail validation set for multi-domain training
  test_data:  # Test sets for final evaluation
    retail: "training/data/tau_bench_test/retail_test.parquet"
    airline: "training/data/tau_bench_test/airline_test.parquet"
```

#### B. Added native tool calling flags

```yaml
generator:
  use_native_tool_calling: true  # Enable VLLM native tool calling
  
environment:
  skyrl_gym:
    tau_bench:
      use_native_tool_calling: true  # Enable native tool calling in environment
```

### Reason for Changes

- Configures test datasets for evaluation
- Enables native tool calling throughout the pipeline

---

## 10. Multi-Domain Training Script

Created specialized training script for multi-domain scenarios with:
- Automatic domain detection from data
- Retail validation tracking
- Test set evaluation
- Optimized hyperparameters for multi-domain learning

---

## 11. WandB Logging Improvements

### Fixed Issues

1. **Parse failure rate logging**: Added early logging of parse failures
2. **Reward logging frequency**: Increased frequency of reward metric logging
3. **Monotonic step warnings**: Fixed by using consistent step counter

### Changes Made

- Added immediate reward logging after generation
- Added parse failure tracking with proper metrics
- Fixed step counter consistency issues

---

## 12. Error Handling Improvements

### Parser Enhancements (tau_bench_env/parser.py)

1. **Malformed JSON handling**: Added recovery for truncated JSON
2. **Debug logging**: Added comprehensive debug output
3. **Fallback parsing**: Multiple parsing strategies for robustness

### Empty Response Handling (trainer.py)

Added filtering for empty model responses to prevent training crashes

---

## 13. Import and Dependency Fixes

### Fixed Issues

1. **Missing numpy import**: Added import in trainer_utils.py
2. **Version comparison**: Fixed semantic version comparison for VLLM
3. **Dict/list type handling**: Fixed type checking in concatenate functions

---

## Section 17: WandB Tracking Fix - Premature Session Termination

### Problem
WandB runs were appearing as finished after 1 epoch/step despite training continuing. The issue was in `skyrl_train/utils/tracking.py` where `wandb.finish()` was being called in the `__del__` destructor method, causing premature termination when garbage collection occurred.

### Solution
Commented out the `wandb.finish()` call in the destructor, allowing wandb to handle cleanup automatically at program exit:

```python
def __del__(self):
    try:
        # FIXED: Commenting out wandb.finish() to prevent premature termination
        # wandb handles cleanup automatically at program exit
        # if "wandb" in self.logger:
        #     self.logger["wandb"].finish(exit_code=0)
        if "swanlab" in self.logger:
            self.logger["swanlab"].finish()
        # ... other loggers ...
```

### Files Changed
- **`SkyRL_mod/skyrl-train/skyrl_train/utils/tracking.py`**: Lines 121-122 commented out

### Impact
- WandB sessions now properly track the entire training run
- Metrics continue logging throughout all epochs
- No more premature "finished" status after 1 step

---

## Section 18: Taxonomy Feedback WandB Project Separation

### Problem
Need to distinguish between vanilla training runs and runs with LLM Judge taxonomy feedback enabled for better experiment tracking and comparison.

### Solution
Modified WandB project naming to automatically append `_with_taxonomy_feedback` when taxonomy feedback is enabled:

```python
# In tracking.py __init__ method
if "wandb" in default_backend:
    # Check if taxonomy feedback is enabled
    taxonomy_feedback_enabled = False
    if config is not None:
        if hasattr(config, 'environment') and hasattr(config.environment, 'skyrl_gym'):
            if hasattr(config.environment.skyrl_gym, 'tau_bench'):
                taxonomy_feedback_enabled = getattr(config.environment.skyrl_gym.tau_bench, 'TAXONOMY_FEEDBACK', False)
        
        # Also check environment variable
        if not taxonomy_feedback_enabled:
            taxonomy_feedback_enabled = os.environ.get('TAXONOMY_FEEDBACK', 'false').lower() == 'true'
    
    # Append taxonomy feedback indicator to project name
    if taxonomy_feedback_enabled:
        project_name = f"{project_name}_with_taxonomy_feedback"
```

### Files Changed
- **`SkyRL_mod/skyrl-train/skyrl_train/utils/tracking.py`**: Lines 44-57 added taxonomy feedback detection and project name modification

### Impact
- Vanilla runs: `tau_bench_rl` (3B), `tau_bench_rl_7b` (7B)
- With taxonomy: `tau_bench_rl_with_taxonomy_feedback` (3B), `tau_bench_rl_7b_with_taxonomy_feedback` (7B)
- Clear separation of experiments with different reward mechanisms
- Easy comparison between vanilla and enhanced training approaches

---

## Summary

All changes maintain backward compatibility while adding:
- Native VLLM tool calling support
- Multi-domain training capabilities
- Test set evaluation during training
- Improved logging and monitoring
- Robust error handling
- Better generalization through hyperparameter optimization
- Fixed WandB premature termination issue
- Taxonomy feedback with separate project tracking

The system now supports efficient multi-domain RL training with proper tool use across different domains, optional LLM Judge evaluation, and reliable experiment tracking.

---

## Section 19: Critical Fix - Disable LLM Judge During Evaluation

### Problem
When TAXONOMY_FEEDBACK was enabled, the LLM Judge was providing reward bonuses during BOTH training AND evaluation. This inflated evaluation metrics and made them invalid for comparing model performance. Evaluation success rates appeared artificially high because they included judge reward bonuses that should only apply during training.

### Solution
Added environment variable `SKYRL_MODE` to distinguish between training and evaluation phases:

#### A. Environment Check (`tau_bench_env/env.py`, line 474)
```python
# Before: Always apply judge rewards if enabled
if self.llm_judge and self.llm_judge.enabled:

# After: Only apply during training
is_training = os.environ.get("SKYRL_MODE", "train") == "train"
if self.llm_judge and self.llm_judge.enabled and is_training:
```

#### B. Mode Setting in Trainer (`skyrl_train/trainer.py`)

1. **In eval() method** (lines 160-163):
```python
# Set environment variable to indicate we're in evaluation mode
# This prevents LLM Judge rewards from being applied during evaluation
import os
os.environ["SKYRL_MODE"] = "eval"
```

2. **After eval() completion** (line 354):
```python
# Reset mode back to training after evaluation
os.environ["SKYRL_MODE"] = "train"
```

3. **In train() method** (lines 362-364):
```python
# Ensure we're in training mode (for LLM Judge rewards)
import os
os.environ["SKYRL_MODE"] = "train"
```

### Files Changed
- **`tau_bench_env/env.py`**: Line 474 - Added training mode check
- **`SkyRL_mod/skyrl-train/skyrl_train/trainer.py`**: Lines 160-163, 354, 362-364 - Added mode management

### Impact
- **Training**: Model still receives taxonomy feedback rewards to improve learning
- **Evaluation**: Pure task performance without inflated rewards
- **Fair Comparison**: Vanilla vs Taxonomy models can now be compared fairly
- **Valid Metrics**: Evaluation results now reflect true task completion rates

### Verification
After this fix, evaluation success rates should be:
- Similar between vanilla and taxonomy models (since eval doesn't use judge)
- Lower than pre-fix results (no more inflated rewards)
- A true measure of task completion performance

---

## Summary

All changes maintain backward compatibility while adding:
- Native VLLM tool calling support
- Multi-domain training capabilities
- Test set evaluation during training
- Improved logging and monitoring
- Robust error handling
- Better generalization through hyperparameter optimization
- Fixed WandB premature termination issue
- Taxonomy feedback with separate project tracking
- **Critical fix: LLM Judge rewards only apply during training, not evaluation**

The system now supports efficient multi-domain RL training with proper tool use across different domains, optional LLM Judge evaluation during training only, and reliable experiment tracking with valid evaluation metrics.

---

## Section 20: Enhanced Conversation Logging and Training Examples

### Problem
1. Evaluation logs only contained model responses, not full conversation trajectories with user/tool interactions
2. No visibility into training generation quality during runs
3. Missing context about domains, turns, and conversation flow

### Solution
Enhanced logging to capture complete conversation histories and training examples:

#### A. Enhanced Evaluation Logging (`skyrl_train/utils/trainer_utils.py`)

**Modified `dump_per_dataset_eval_results` function** (lines 246-265):
```python
# Before: Only logged input prompt and output response
entry = {
    "input_prompt": input_prompts[i],
    "output_response": output_responses[i],
    "score": concat_generator_outputs["rewards"][i],
    ...
}

# After: Full conversation history with user/tool interactions
# Extract full conversation history from env_extras if available
conversation_history = []
if concat_env_extras[i] and "conversation_history" in concat_env_extras[i]:
    conversation_history = concat_env_extras[i]["conversation_history"]

entry = {
    "input_prompt": input_prompts[i],
    "output_response": output_responses[i],
    "conversation_history": conversation_history,  # Full conversation with user/tool responses
    "score": concat_generator_outputs["rewards"][i],
    "stop_reason": concat_generator_outputs.get("stop_reasons", [None] * len(input_prompts))[i],
    "env_class": concat_all_envs[i],
    "env_extras": concat_env_extras[i],
    "data_source": data_source,
    "timestamp": concat_env_extras[i].get("timestamp") if concat_env_extras[i] else None,
    "domain": concat_env_extras[i].get("domain") if concat_env_extras[i] else None,
    "turns": concat_env_extras[i].get("turns") if concat_env_extras[i] else None,
}
```

#### B. Added Training Examples Logging (`skyrl_train/trainer.py`)

1. **Replaced simple debug print** (line 430-432):
```python
# Before:
vis = self.tokenizer.decode(generator_output["response_ids"][0])
print("example: ", vis)

# After:
self._log_training_examples(generator_output, uids[:10])  # Log first 10 examples
```

2. **Added `_log_training_examples` method** (lines 358-407):
```python
def _log_training_examples(self, generator_output: GeneratorOutput, example_uids: List[str]):
    """Log training generation examples with full conversation histories."""
    try:
        # Only log occasionally to avoid spam (every 10 steps)
        if self.global_step % 10 != 1:
            return
            
        # Print one quick example to console
        if generator_output["response_ids"]:
            vis = self.tokenizer.decode(generator_output["response_ids"][0])
            print(f"Training example (step {self.global_step}): {vis[:200]}...")
        
        # Save detailed examples to exports directory
        if self.cfg.trainer.dump_eval_results and len(example_uids) > 0:
            from pathlib import Path
            import json
            from datetime import datetime
            
            train_examples_dir = Path(self.cfg.trainer.export_path) / "training_examples"
            train_examples_dir.mkdir(parents=True, exist_ok=True)
            
            examples_file = train_examples_dir / f"step_{self.global_step}_examples.jsonl"
            
            with open(examples_file, "w") as f:
                for i, uid in enumerate(example_uids):
                    if i >= len(generator_output["response_ids"]):
                        break
                        
                    # Get conversation history from rollout metadata if available
                    conversation_history = []
                    if "rollout_metadata" in generator_output and i < len(generator_output["rollout_metadata"]):
                        metadata = generator_output["rollout_metadata"][i]
                        if isinstance(metadata, dict) and "conversation_history" in metadata:
                            conversation_history = metadata["conversation_history"]
                    
                    entry = {
                        "global_step": self.global_step,
                        "uid": uid,
                        "input_prompt": self.tokenizer.decode(generator_output["prompt_token_ids"][i]),
                        "output_response": self.tokenizer.decode(generator_output["response_ids"][i]),
                        "conversation_history": conversation_history,  # Full conversation trajectory
                        "reward": generator_output["rewards"][i],
                        "stop_reason": generator_output.get("stop_reasons", [None] * len(example_uids))[i],
                        "timestamp": str(datetime.now()),
                    }
                    f.write(json.dumps(entry, ensure_ascii=False) + "\n")
            
            print(f"Saved {len(example_uids)} training examples to {examples_file}")
            
    except Exception as e:
        logger.warning(f"Failed to log training examples: {e}")
```

### Files Changed
- **`SkyRL_mod/skyrl-train/skyrl_train/utils/trainer_utils.py`**: Lines 246-265 - Enhanced eval logging
- **`SkyRL_mod/skyrl-train/skyrl_train/trainer.py`**: Lines 430-432, 358-407 - Added training examples logging

### Impact
- **Full conversation context**: Logs now include complete trajectories with user queries, assistant responses, tool calls, and tool results
- **Training visibility**: Can monitor generation quality during training with 10 examples every 10 steps
- **Debugging improvements**: Additional metadata (domain, turns, timestamp) helps identify issues
- **Research enablement**: Complete conversation data enables analysis of multi-turn interactions

### Output Structure
Logged conversations now match the requested format:
```json
{
  "conversation_history": [
    {"role": "user", "content": "Find me a flight..."},
    {"role": "assistant", "content": "I'll help you...", "tool_calls": [...]},
    {"role": "tool", "name": "search_flights", "content": "{...}"},
    {"role": "assistant", "content": "I found these flights..."}
  ],
  "domain": "airline",
  "turns": 5,
  "score": 1.0
}
```

---

## Section 21: Fixed Rewards=0 Issue and Configuration Problems

### Problem
All generation rewards were 0 due to `zero_reward_on_non_stop: true` configuration setting that zeroed rewards when conversations hit length limits or used EOS tokens.

### Solution

#### A. Disabled zero_reward_on_non_stop (`training/configs/tau_bench_config.yaml`, line 198)
```yaml
# Before:
zero_reward_on_non_stop: true

# After:
zero_reward_on_non_stop: false  # CRITICAL: Set to false for tau_bench - conversations often hit length limit
```

#### B. Fixed total_steps Reference Error (`skyrl_train/trainer.py`, line 220)
```python
# Before:
logger.info(f"[Eval Step {self.total_steps}] ...")

# After:
logger.info(f"[Eval Step {self.global_step}] ...")
```

#### C. Set Training Mode Early (`training/main_tau_bench.py`, line 7)
```python
# Added early to ensure training mode from start
os.environ.setdefault("SKYRL_MODE", "train")
```

### Impact
- Rewards now properly reflect task completion instead of being zeroed
- Fixed attribute error that was causing logging failures
- Ensures consistent training mode from initialization

---

## Summary

All changes maintain backward compatibility while adding:
- Native VLLM tool calling support
- Multi-domain training capabilities
- Test set evaluation during training
- Improved logging and monitoring
- Robust error handling
- Better generalization through hyperparameter optimization
- Fixed WandB premature termination issue
- Taxonomy feedback with separate project tracking
- **Critical fix: LLM Judge rewards only apply during training, not evaluation**
- **Enhanced conversation logging with full trajectories**
- **Training generation examples for monitoring**
- **Fixed rewards=0 configuration issue**

The system now supports efficient multi-domain RL training with proper tool use across different domains, optional LLM Judge evaluation during training only, reliable experiment tracking with valid evaluation metrics, and comprehensive conversation logging for analysis.

---

## Section 22: Empty Response Handling and Memory Optimizations

### Problem
1. Generator returning empty responses causing `ValueError: zero-size array to reduction operation minimum`
2. OOM errors during critic and policy training with 3B model
3. Batch size configuration causing empty input batches

### Solution

#### A. Added Safety Check for Empty Responses (`skyrl_gym_generator.py`, lines 399-410)
```python
def _rollout_metrics(self, responses: List[List[int]], rewards: List[float]):
    # Safety check for empty responses
    if len(responses) == 0:
        logger.warning("No responses generated in _rollout_metrics. Returning zero metrics.")
        return {
            "generate/min_num_tokens": 0,
            "generate/max_num_tokens": 0,
            "generate/avg_num_tokens": 0,
            "generate/std_num_tokens": 0,
            "generate/avg_tokens_non_zero_rewards": 0,
            "generate/avg_tokens_zero_rewards": 0,
        }
```

#### B. Added Generation Debugging Logs (`skyrl_gym_generator.py`)
- Line 349: Log number of prompts received
- Line 370: Log number of generation tasks started  
- Line 378: Log number of outputs received

#### C. Enabled CPU Offloading for Critic (`tau_bench_config.yaml`, line 76)
```yaml
critic:
  fsdp_config:
    cpu_offload: true  # Changed from false to reduce GPU memory
```

### Files Changed
- **`SkyRL_mod/skyrl-train/skyrl_train/generators/skyrl_gym_generator.py`**: Lines 399-410, 349, 370, 378
- **`training/configs/tau_bench_config.yaml`**: Line 76

### Impact
- Prevents crashes when generation fails or returns empty results
- Provides debugging visibility into generation pipeline
- Reduces GPU memory usage through CPU offloading
- Maintains stability with proper error handling