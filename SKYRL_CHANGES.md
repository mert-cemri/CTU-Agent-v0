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

## Summary

All changes maintain backward compatibility while adding:
- Native VLLM tool calling support
- Multi-domain training capabilities
- Test set evaluation during training
- Improved logging and monitoring
- Robust error handling
- Better generalization through hyperparameter optimization

The system now supports efficient multi-domain RL training with proper tool use across different domains.