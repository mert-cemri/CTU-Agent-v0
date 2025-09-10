# SKYRL MIGRATION PLAN - From SkyRL_mod to SkyRL
**Date**: 2025-01-10  
**Branch**: skynew  
**Objective**: Complete migration from SkyRL_mod to original SkyRL codebase with all 24 sections of changes

## CRITICAL EDGE CASES ANALYSIS

### 1. Generator Functionality Integration Points

#### A. Tool Calling Flow
**Current Flow in SkyRL_mod**:
```
tau_bench_env.init() → metadata["tools"] → generator.agent_loop() → InferenceEngineInput(tools=..., use_native_tool_calling=True) → VLLM engine
```

**Missing in SkyRL**:
- `InferenceEngineInput` lacks `tools` and `use_native_tool_calling` fields
- Generator doesn't extract tools from environment metadata
- VLLM engines don't handle native tool calling
- No pre-computed token_ids extraction for structured responses

#### B. Qwen3 Integration Issues
**SkyRL Has**:
- ✅ Qwen3 thinking template in `utils.py`
- ✅ `get_custom_chat_template()` function

**SkyRL Missing**:
- ❌ `_apply_chat_template()` helper method in generator
- ❌ `is_qwen3_model` detection in generator
- ❌ `enable_thinking=False` parameter usage
- ❌ All `tokenizer.apply_chat_template()` calls replaced with helper

**Edge Case**: Qwen3 models will generate with thinking tokens enabled, causing parser failures.

#### C. Multi-turn Conversation Handling
**Critical Issue**: The response extraction logic in `skyrl_gym_generator.py` lines 201-238 has multiple edge cases:

1. **Empty Response Lists**: When `eval_before_train=true`, `chat_history[len(prompt):]` can be empty
2. **Custom Template with No Responses**: Custom template path assumes responses exist
3. **Fallback Token Extraction**: Missing fallback logic when `response_ids` is empty
4. **Assistant Message Extraction**: No logic to extract from chat history when token-based extraction fails

**Missing in SkyRL**: All the safety checks and fallback logic from Section 24.

### 2. Inference Engine Edge Cases

#### A. Native Tool Calling Support
**VLLM Engine Issues**:
- SkyRL's VLLM engine only supports `generate()` method with tokens
- No `chat()` method support for OpenAI-compatible tool calling  
- No ChatCompletionResponse handling for structured outputs
- Missing version check for VLLM >= 0.8.3

**Edge Case**: When `use_native_tool_calling=true`, the generator will pass tools but VLLM engine can't handle them.

#### B. Token ID Handling
**Missing Features**:
- No `response_token_ids` extraction from tool calling responses
- No `output_token_ids` parameter in engine output
- No pre-computed token handling for structured responses

**Impact**: Token-based training will fail with native tool calling.

### 3. Trainer and Logging Edge Cases

#### A. WandB Integration Issues
**Critical Problems in SkyRL**:
- `__del__` method in `tracking.py` likely calls `wandb.finish()` prematurely
- No taxonomy feedback project separation
- Fragmented step counting (likely multiple `total_steps` increments)

**Edge Case**: Training runs will show as "finished" after 1 step in WandB.

#### B. Empty Response Handling
**Critical Safety Issue**:
- No safety check in `_rollout_metrics()` for empty response lists
- No debugging logs for generation pipeline
- No graceful degradation when generation fails

**Edge Case**: Training crashes with `ValueError: zero-size array to reduction operation minimum`.

### 4. Environment Integration Edge Cases

#### A. SKYRL_MODE Environment Variable
**Missing in SkyRL**:
- No `SKYRL_MODE` setting in trainer methods
- No mode distinction between training and evaluation
- Tau_bench_env won't disable LLM Judge during evaluation

**Edge Case**: Evaluation metrics will be inflated by LLM Judge rewards.

### 5. Tokenizer and Chat Template Edge Cases

#### A. Enable Thinking Parameter
**Critical Issue**: Qwen3 models support `enable_thinking` parameter in `apply_chat_template()`:
```python
# Current SkyRL_mod approach:
if self.is_qwen3_model:
    kwargs["enable_thinking"] = False
return self.tokenizer.apply_chat_template(messages, **kwargs)
```

**Missing in SkyRL**: All calls use raw `tokenizer.apply_chat_template()` without thinking mode control.

### MIGRATION PRIORITY MATRIX

| Feature | SkyRL_mod Status | SkyRL Status | Migration Priority | Risk Level |
|---------|------------------|--------------|-------------------|------------|
| Tool Calling | ✅ Full | ❌ Missing | High | High |
| Qwen3 Support | ✅ Full | ⚠️ Partial | High | High |
| Empty Response Safety | ✅ Fixed | ❌ Missing | High | Critical |
| WandB Logging | ✅ Fixed | ❌ Broken | High | Critical |
| Training Examples | ✅ Full | ❌ Missing | Medium | Medium |
| SKYRL_MODE | ✅ Full | ❌ Missing | Medium | Medium |
| Multi-turn Chat | ✅ Full | ⚠️ Partial | Medium | High |
| Debug Logging | ✅ Full | ❌ Missing | Low | Low |

## Table of Contents
1. [Executive Summary](#executive-summary)
2. [Pre-Migration Checklist](#pre-migration-checklist)
3. [Section-by-Section Migration](#section-by-section-migration)
4. [Training Scripts Migration](#training-scripts-migration)
5. [Tau-bench Environment Migration](#tau-bench-environment-migration)
6. [Validation and Testing](#validation-and-testing)
7. [Post-Migration Verification](#post-migration-verification)

## Executive Summary

This plan migrates ALL 24 sections of changes documented in `skyrl_changes.md` from SkyRL_mod to the newer SkyRL codebase. The migration will:
- Preserve SkyRL_mod unchanged as backup
- Apply all changes to SkyRL in the skynew branch
- Update all training scripts and configurations
- Ensure tau_bench_env compatibility
- Maintain full functionality with no deferred work

## Pre-Migration Checklist

- [x] Current branch: skynew
- [x] SkyRL_mod preserved as backup
- [x] All 24 sections from skyrl_changes.md reviewed
- [x] File mappings verified between SkyRL_mod and SkyRL
- [x] Training scripts analyzed for path dependencies
- [x] Tau_bench_env compatibility checked

## Critical File Existence Verification (COMPLETED)

### Verified to Exist in SkyRL:
- ✅ `SkyRL/skyrl-train/skyrl_train/inference_engines/base.py`
- ✅ `SkyRL/skyrl-train/skyrl_train/generators/skyrl_gym_generator.py`
- ✅ `SkyRL/skyrl-train/skyrl_train/inference_engines/ray_wrapped_inference_engine.py`
- ✅ `SkyRL/skyrl-train/skyrl_train/inference_engines/remote_inference_engine.py`
- ✅ `SkyRL/skyrl-train/skyrl_train/trainer.py`
- ✅ `SkyRL/skyrl-train/skyrl_train/utils/tracking.py`
- ✅ `SkyRL/skyrl-train/skyrl_train/utils/trainer_utils.py`
- ✅ `SkyRL/skyrl-train/skyrl_train/entrypoints/main_base.py`
- ✅ `SkyRL/skyrl-gym/skyrl_gym/envs/base_text_env.py`

### Project-Level Files (No SkyRL Changes Needed):
- ✅ `/training/main_tau_bench.py` - Tau_bench registration stays here
- ✅ `/training/configs/tau_bench_config.yaml` - Config stays here
- ✅ `/training/configs/skyrl_gym_config/tau_bench.yaml` - Config stays here
- ✅ `/tau_bench_env/` - Environment implementation stays here

**KEY INSIGHT**: The architecture keeps tau_bench-specific code at the project level, not inside SkyRL. Only core improvements (bug fixes, logging, tool calling support) go into SkyRL.

## Section-by-Section Migration

### Section 1: Base Types - Tool Calling Support
**File**: `SkyRL/skyrl-train/skyrl_train/inference_engines/base.py`
**Changes**:
```python
# ADD to InferenceEngineInput TypedDict:
tools: Optional[List[Dict[str, Any]]]
use_native_tool_calling: Optional[bool]
```
**Verification**: Check if TypedDict exists, add imports if needed

### Section 2: Generator - Native Tool Calling
**File**: `SkyRL/skyrl-train/skyrl_train/generators/skyrl_gym_generator.py`
**Changes**:
1. Add `use_native_tool_calling` attribute in `__init__`
2. Extract tools from metadata in `agent_loop()`
3. Pass tools to InferenceEngineInput
4. Handle native tool calling responses
**Dependencies**: Requires Section 1 completed first

### Section 3: Ray Wrapped Inference Engine
**File**: `SkyRL/skyrl-train/skyrl_train/inference_engines/ray_wrapped_inference_engine.py`
**Changes**:
1. Fix VLLM version check using semantic versioning:
   ```python
   from packaging.version import Version
   assert Version(vllm.__version__) >= Version("0.8.3")
   ```
2. Add native tool calling support in `generate()` method
3. Handle ChatCompletionResponse for tool calls
**Dependencies**: Check if vllm is imported, add packaging dependency

### Section 4: Remote Inference Engine
**File**: `SkyRL/skyrl-train/skyrl_train/inference_engines/remote_inference_engine.py`
**Changes**:
1. Pass through tool calling parameters in request_data
2. Add tools and use_native_tool_calling to request
**Verification**: Check existing request_data structure

### Section 5: Environment Registration
**File**: `/training/main_tau_bench.py` (ALREADY EXISTS - NO CHANGES NEEDED)
**Current Status**:
1. ✅ Already contains tau_bench registration in `skyrl_entrypoint()`
2. ✅ Already imports skyrl_gym and registers tau_bench environment
3. ✅ Already has Ray remote entrypoint configured
**Action**: No changes needed - registration already handled at project level

### Section 6: Test Sets for Evaluation
**File**: `SkyRL/skyrl-train/skyrl_train/entrypoints/main_base.py`
**Changes**:
1. Add `get_test_datasets()` method
2. Update `_setup_trainer()` to load test datasets
3. Handle test data configuration parsing
**Verification**: Check if main_base.py exists in SkyRL

### Section 7: Multi-Domain Training Support
**File**: `SkyRL/skyrl-train/skyrl_train/entrypoints/main_base.py`
**Changes**:
1. Add `get_retail_eval_dataset()` method
2. Set retail eval dataset in trainer setup
**Dependencies**: Requires PromptDataset class availability

### Section 8: Trainer Test Dataset Support
**File**: `SkyRL/skyrl-train/skyrl_train/trainer.py`
**Changes**:
1. Add `set_test_datasets()` method
2. Add test evaluation in `eval()` method
3. Update metrics collection for test sets
**Verification**: Check trainer class structure in SkyRL

### Section 9: Configuration Updates
**Files**: 
- `/training/configs/tau_bench_config.yaml` (ALREADY EXISTS)
- `/training/configs/skyrl_gym_config/tau_bench.yaml` (ALREADY EXISTS)
**Current Status**:
1. ✅ Tau_bench specific configuration already exists at project level
2. ✅ Test_data configuration already in tau_bench_config.yaml
3. ✅ Use_native_tool_calling flags already in configs
**Action**: No changes needed - configs already at project level, not in SkyRL

### Section 10: Multi-Domain Training Script
**Note**: This is handled in training scripts migration section

### Section 11: WandB Logging Improvements
**File**: `SkyRL/skyrl-train/skyrl_train/trainer.py`
**Changes**:
1. Add parse failure rate logging
2. Add immediate reward logging after generation
3. Fix step counter consistency
**Verification**: Check existing logging structure

### Section 12: Error Handling Improvements
**File**: Create `SkyRL/skyrl-train/skyrl_train/envs/tau_bench/parser.py`
**Changes**:
1. Add malformed JSON handling
2. Add debug logging
3. Add fallback parsing strategies
**Note**: May need to be in tau_bench_env instead

### Section 13: Import and Dependency Fixes
**Files**: Various
**Changes**:
1. Add missing numpy imports where needed
2. Fix version comparison using semantic versioning
3. Fix Dict/list type handling in concatenate functions
**Verification**: Run import tests after changes

### Section 14: [Reserved - Not in skyrl_changes.md]

### Section 15: Simplified WandB Logging System
**File**: `SkyRL/skyrl-train/skyrl_train/trainer.py`
**Changes**:
1. Remove fragmented `total_steps` counter
2. Implement unified `all_metrics` collection
3. Single logging call per training step using `global_step`
4. Ensure all metric types are properly logged
**Critical**: This fixes major logging issues

### Section 16: Hyperparameter Optimization
**Note**: Configuration changes only, handled in config migration

### Section 17: WandB Tracking Fix - Premature Termination
**File**: `SkyRL/skyrl-train/skyrl_train/utils/tracking.py`
**Changes**:
1. Comment out `wandb.finish()` in `__del__` method
2. Let wandb handle cleanup automatically
**Line numbers**: Around line 121-122 in tracking.py
**Critical**: Prevents premature run termination

### Section 18: Taxonomy Feedback Project Separation
**File**: `SkyRL/skyrl-train/skyrl_train/utils/tracking.py`
**Changes**:
1. Add taxonomy feedback detection logic
2. Append `_with_taxonomy_feedback` to project name when enabled
3. Check both config and environment variables
**Dependencies**: Lines 44-57 in tracking.py

### Section 19: LLM Judge During Evaluation Fix
**Files**:
- `SkyRL/skyrl-train/skyrl_train/trainer.py`
- Note: tau_bench_env/env.py needs corresponding changes
**Changes**:
1. Set `SKYRL_MODE` environment variable in eval()
2. Reset mode after evaluation
3. Set training mode in train() method
**Critical**: Prevents inflated evaluation metrics

### Section 20: Enhanced Conversation Logging
**Files**:
- `SkyRL/skyrl-train/skyrl_train/utils/trainer_utils.py`
- `SkyRL/skyrl-train/skyrl_train/trainer.py`
**Changes**:
1. Modify `dump_per_dataset_eval_results()` for full conversation history
2. Add `_log_training_examples()` method to trainer
3. Save training examples to exports directory
**Dependencies**: Requires env_extras to contain conversation_history

### Section 21: Fixed Rewards=0 Issue
**Files**:
- Update tau_bench_config.yaml (handled in config migration)
- `SkyRL/skyrl-train/skyrl_train/trainer.py`
**Changes**:
1. Fix total_steps reference to use global_step
2. Set SKYRL_MODE early in training
**Line**: Around line 220 in trainer.py

### Section 22: Empty Response Handling
**File**: `SkyRL/skyrl-train/skyrl_train/generators/skyrl_gym_generator.py`
**Changes**:
1. Add safety check in `_rollout_metrics()` for empty responses
2. Add generation debugging logs
3. Return zero metrics when no responses
**Lines**: Around lines 399-410

### Section 23: Qwen3 Support with Thinking Mode Disabled
**File**: `SkyRL/skyrl-train/skyrl_train/generators/skyrl_gym_generator.py`
**Changes**:
1. Add `is_qwen3_model` detection in __init__
2. Add `_apply_chat_template()` helper method
3. Replace ALL `tokenizer.apply_chat_template()` calls with helper
**Critical**: Required for Qwen3 model support

### Section 24: IndexError Fix for eval_before_train
**File**: `SkyRL/skyrl-train/skyrl_train/generators/skyrl_gym_generator.py`
**Changes**:
1. Check if response_messages exist before using custom template
2. Add fallback for empty response lists
3. Prevent IndexError during evaluation
**Lines**: Around lines 201-218
**Critical**: Fixes crash during eval_before_train

## Training Scripts Migration

### Files to Update in `/training/` folder:

#### 1. main_tau_bench.py
**Current Imports**:
```python
from skyrl_gym.envs.registration import register
from skyrl_train.entrypoints.main_base import BasePPOExp
from skyrl_train.utils.utils import validate_cfg
from skyrl_train.utils.utils import initialize_ray
```
**Changes**:
- No changes needed - imports already use skyrl_train/skyrl_gym (path-agnostic)
- These will automatically use SkyRL when PYTHONPATH is updated in shell scripts

#### 2. All Shell Scripts (run_*.sh)
**Files**:
- run_multi_domain.sh
- run_multi_domain_7b.sh
- run_multi_domain_7b_optimized.sh
- run_retail_3b_grpo.sh
- run_retail_3b_grpo_repetition_fix.sh
- run_retail_3b_grpo_taxonomy.sh
- run_retail_7b_grpo.sh
- run_retail_7b_grpo_taxonomy.sh
- run_retail_8b_grpo_taxonomy.sh
- run_tau_bench.sh
- run_tau_bench_7b.sh
- run_tau_bench_llama.sh

**Changes for ALL scripts**:
```bash
# Change FROM:
export PYTHONPATH="${PYTHONPATH}:$(pwd)/../SkyRL_mod/skyrl-train:$(pwd)/../SkyRL_mod/skyrl-gym:..."

# Change TO:
export PYTHONPATH="${PYTHONPATH}:$(pwd)/../SkyRL/skyrl-train:$(pwd)/../SkyRL/skyrl-gym:..."
```

#### 3. Configuration Files
**Files in `/training/configs/`**:
- tau_bench_config.yaml
- tau_bench_llama_config.yaml
- skyrl_gym_config/tau_bench.yaml

**Changes**:
- Ensure all paths reference SkyRL instead of SkyRL_mod
- Verify configuration keys match new SkyRL structure
- Set `zero_reward_on_non_stop: false` for tau_bench

## Tau-bench Environment Migration

### Files to Review/Update in `/tau_bench_env/`:

#### 1. env.py
**Current Import**: `from skyrl_gym.envs.base_text_env import BaseTextEnv, BaseTextEnvStepOutput, ConversationType`
**Required Changes**:
- No import path changes needed (already uses skyrl_gym)
- Verify BaseTextEnv exists in `SkyRL/skyrl-gym/skyrl_gym/envs/base_text_env.py`
- Add SKYRL_MODE check for LLM Judge around line 474:
  ```python
  is_training = os.environ.get("SKYRL_MODE", "train") == "train"
  if self.llm_judge and self.llm_judge.enabled and is_training:
  ```

#### 2. parser.py
**Compatibility Checks**:
- Ensure parser works with new native tool calling format
- Verify debug logging compatible with new structure
- simple_parser.py already exists for native tool calling support

#### 3. __init__.py
**Changes**:
- Check for any SkyRL_mod specific imports
- Should remain unchanged if only using relative imports

#### 4. llm_judge_integration.py
**Compatibility Checks**:
- Verify LLM Judge works with SKYRL_MODE environment variable
- Check reward format compatibility

### Critical Compatibility Points:
1. **Import Paths**: tau_bench_env uses skyrl_gym which is path-agnostic
2. **BaseTextEnv**: Already correctly imported from skyrl_gym
3. **Step Output**: BaseTextEnvStepOutput format should be consistent
4. **Metadata**: Verify conversation_history properly passed in env_extras
5. **Tools Format**: Already converts to OpenAI format (see _convert_tools_to_openai_format)

## Validation and Testing

### Phase 1: Basic Import Test
```python
# Test script to verify imports work
from SkyRL.skyrl_train.skyrl_train.entrypoints.main_base import BasePPOExp
from SkyRL.skyrl_train.skyrl_train.trainer import Trainer
from SkyRL.skyrl_gym import skyrl_gym
import tau_bench_env
```

### Phase 2: Environment Registration Test
```python
# Test tau_bench registration
from skyrl_gym.envs.registration import register
register(id="tau_bench", entry_point="tau_bench_env.env:TauBenchEnv")
```

### Phase 3: Configuration Load Test
```bash
# Test configuration loading
python -c "from omegaconf import OmegaConf; cfg = OmegaConf.load('training/configs/tau_bench_config.yaml')"
```

### Phase 4: Single Task Test
```bash
# Run minimal training test
bash training/run_tau_bench.sh trainer.epochs=1 trainer.eval_interval=1
```

### Phase 5: Full Integration Test
- Test with Qwen3 model
- Test with eval_before_train=true
- Test with taxonomy feedback enabled
- Test WandB logging

## Post-Migration Verification

### Checklist:
- [ ] All 24 sections successfully migrated
- [ ] All training scripts updated with new paths
- [ ] Tau_bench_env compatible with new SkyRL
- [ ] Import tests pass
- [ ] Environment registration works
- [ ] Configuration loading successful
- [ ] Basic training loop runs
- [ ] WandB logging functional
- [ ] Qwen3 models work without IndexError
- [ ] Native tool calling functional (if VLLM configured)
- [ ] Test datasets load correctly
- [ ] Evaluation metrics accurate (no inflation)
- [ ] Training examples logged properly
- [ ] No premature WandB termination

### Rollback Plan:
If issues arise, we can immediately revert to using SkyRL_mod by:
1. Reverting training script path changes
2. Using git to reset SkyRL directory changes
3. SkyRL_mod remains untouched as backup

## Implementation Order

1. **Core Infrastructure** (Sections 1-4, 17, 22-24)
   - Critical fixes first (IndexError, WandB, empty responses)
   - Base types and inference engines
   
2. **Generator and Trainer** (Sections 2, 8, 11, 15, 19-21)
   - Generator updates with all safety fixes
   - Trainer improvements and logging
   
3. **Configuration and Registration** (Sections 5-7, 9)
   - Environment registration
   - Configuration updates
   
4. **Training Scripts**
   - Update all shell scripts
   - Update Python entrypoints
   
5. **Tau-bench Environment**
   - Verify compatibility
   - Add SKYRL_MODE support
   
6. **Testing and Validation**
   - Run comprehensive tests
   - Verify all functionality

## Notes and Warnings

1. **Critical Dependencies**:
   - packaging library needed for version checks
   - VLLM version >= 0.8.3 for native tool calling
   - OpenAI API key for GPT-4o user simulation

2. **Potential Issues**:
   - SkyRL may have different class structures than SkyRL_mod
   - Some methods might not exist or have different signatures
   - Configuration keys might differ

3. **Must Verify**:
   - BaseTextEnv location and interface in new SkyRL
   - Trainer class methods and signatures
   - Generator initialization parameters
   - Configuration schema compatibility

This migration plan ensures NOTHING is skipped and all functionality is preserved.

## MIGRATION SUMMARY

### What Goes INTO SkyRL:
1. **Core Bug Fixes** (Sections 17, 21, 22, 24) - WandB, rewards, empty responses, IndexError
2. **Generator Improvements** (Sections 2, 23) - Native tool calling, Qwen3 support
3. **Inference Engine Updates** (Sections 1, 3, 4) - Tool calling infrastructure
4. **Trainer Enhancements** (Sections 6, 7, 8, 11, 15, 19, 20) - Logging, test datasets, metrics
5. **Tracking Improvements** (Sections 17, 18) - WandB fixes, taxonomy separation

### What Stays at PROJECT Level:
1. **Training Scripts** (`/training/`) - Only PYTHONPATH updates needed
2. **Configurations** (`/training/configs/`) - Already correctly placed
3. **Tau-bench Environment** (`/tau_bench_env/`) - Minor SKYRL_MODE update
4. **Registration Logic** - Already in `/training/main_tau_bench.py`

### Critical Path Actions:
1. **FIRST**: Apply critical bug fixes (Sections 17, 22, 23, 24) to prevent crashes
2. **SECOND**: Add tool calling support (Sections 1-4) for native VLLM integration
3. **THIRD**: Enhance trainer/logging (Sections 15, 19, 20) for better monitoring
4. **FOURTH**: Update shell scripts to use SkyRL paths
5. **LAST**: Test end-to-end with all features enabled

### Files That Need CAREFUL Attention:
- `skyrl_gym_generator.py` - Gets the MOST changes (8+ sections affect this file)
- `trainer.py` - Gets significant changes (6+ sections)
- `tracking.py` - Critical WandB fixes
- Shell scripts - ALL need PYTHONPATH updates

### Validation Checkpoints:
After each major section, run:
```bash
# Import test
python -c "from SkyRL.skyrl_train.skyrl_train.trainer import Trainer"

# After all changes, run minimal training
bash training/run_tau_bench.sh trainer.epochs=1
```