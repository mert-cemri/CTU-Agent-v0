# SkyRL Repository Changes for CTU-Agent-v0 Training Framework

This document lists all changes made to the SkyRL repository (`SkyRL_mod/skyrl-train/`) to support the CTU-Agent-v0 multi-domain training framework.

## Overview of Changes

The implementation includes native VLLM tool calling, multi-domain training support, improved WandB logging, and robust error handling. All changes maintain backward compatibility.

## Latest Changes (Section 15): Simplified WandB Logging System

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
    tokenizer,
    model_name: str,
):
    # ... existing code ...
    self.use_native_tool_calling = getattr(generator_cfg, 'use_native_tool_calling', False)
```

#### B. Agent Loop Modification

**MODIFIED** `agent_loop()` method to extract tools from environment metadata:

```python
# Init() returns the first prompt to be given to the model, and optional metadata dict
chat_history, metadata = env.init(chat_history)

# Extract tools from metadata if native tool calling is enabled
tools = None
if self.use_native_tool_calling and metadata and "tools" in metadata:
    tools = metadata["tools"]
```

**MODIFIED** inference engine input creation in the generation loop:

```python
while not done:
    if self.use_conversation_multi_turn:
        engine_input = InferenceEngineInput(
            prompts=[chat_history], 
            trajectory_ids=[trajectory_id], 
            sampling_params=sampling_params,
            tools=tools if self.use_native_tool_calling else None,
            use_native_tool_calling=self.use_native_tool_calling
        )
    else:
        engine_input = InferenceEngineInput(
            prompt_token_ids=[input_ids], 
            trajectory_ids=[trajectory_id], 
            sampling_params=sampling_params,
            tools=tools if self.use_native_tool_calling else None,
            use_native_tool_calling=self.use_native_tool_calling
        )
```

#### C. Batched Generation Modification

**MODIFIED** `generate_batched()` method to handle tools:

```python
envs = []
init_prompts = []
all_tools = []
for env_class, env_extra, prompt in zip(env_classes, env_extras, prompts):
    env_extra["max_turns"] = self.max_turns
    env_config = self.skyrl_gym_cfg.get(env_class, DictConfig({}))
    env = skyrl_gym.make(env_class, env_config=env_config, extras=env_extra)
    init_prompt, metadata = env.init(prompt)
    init_prompts.append(init_prompt)
    envs.append(env)
    
    # Extract tools for this environment if native tool calling is enabled
    if self.use_native_tool_calling and metadata and "tools" in metadata:
        all_tools.append(metadata["tools"])
    else:
        all_tools.append(None)

# For batched generation, we need to handle cases where some envs have tools and others don't
# For simplicity, use tools from first environment or None if not consistent
tools = all_tools[0] if self.use_native_tool_calling and all(t == all_tools[0] for t in all_tools) else None

engine_input = InferenceEngineInput(
    prompts=init_prompts, 
    sampling_params=sampling_params,
    tools=tools,
    use_native_tool_calling=self.use_native_tool_calling
)
```

### Reasons for Changes

- **Tool Extraction**: Environment provides tools in metadata during initialization, generator extracts and forwards them
- **Configuration Reading**: Generator reads `use_native_tool_calling` flag from config to enable/disable feature
- **Engine Input Enhancement**: Pass tools and flag to inference engine so it knows whether to use chat() or generate()
- **Batched Support**: Handle tool extraction for batched generation scenarios
- **Backward Compatibility**: All changes are additive and optional

---

## 3. VLLM Inference Engine (`skyrl_train/inference_engines/vllm/vllm_engine.py`)

### Changes Made

#### A. Preprocessing Method Enhancement

**MODIFIED** `_preprocess_prompts()` method in `BaseVLLMInferenceEngine`:

```python
def _preprocess_prompts(self, input_batch: InferenceEngineInput):
    """Common prompt preprocessing logic."""
    prompts = input_batch.get("prompts")
    prompt_token_ids = input_batch.get("prompt_token_ids")
    request_sampling_params = input_batch.get("sampling_params")
    tools = input_batch.get("tools")
    use_native_tool_calling = input_batch.get("use_native_tool_calling", False)

    if (prompts is None and prompt_token_ids is None) or (prompts is not None and prompt_token_ids is not None):
        raise ValueError("Either `prompts` or `prompt_token_ids` must be provided, but not both.")

    sampling_params = (
        SamplingParams(**request_sampling_params) if request_sampling_params is not None else self.sampling_params
    )

    # If using native tool calling, return the prompts as-is for chat() method
    if use_native_tool_calling and prompts is not None:
        return prompts, sampling_params, tools, use_native_tool_calling

    if prompt_token_ids is None:
        prompt_token_ids = self.tokenizer.apply_chat_template(
            prompts,
            add_generation_prompt=True,
            add_special_tokens=False,
            return_dict=True,
            tokenize=True,
        )["input_ids"]

    return prompt_token_ids, sampling_params, tools, use_native_tool_calling
```

**MODIFIED** comment in `_postprocess_outputs()` method:

```python
def _postprocess_outputs(self, outputs):
    """Common output processing logic for both generate() and chat() methods."""
    # ... rest unchanged ...
```

#### B. Synchronous Engine (`VLLMInferenceEngine`)

**MODIFIED** `generate()` method to conditionally use chat() or generate():

```python
async def generate(self, input_batch: InferenceEngineInput) -> InferenceEngineOutput:
    prompts_or_token_ids, sampling_params, tools, use_native_tool_calling = self._preprocess_prompts(input_batch)

    if use_native_tool_calling:
        # Use chat() method with tools - prompts_or_token_ids is a list of conversations
        outputs = []
        for conversation in prompts_or_token_ids:
            output = await asyncio.to_thread(
                self.llm.chat,
                messages=conversation,
                sampling_params=sampling_params,
                tools=tools,
                add_generation_prompt=True,
                use_tqdm=False
            )
            outputs.extend(output)  # chat() returns list[RequestOutput]
    else:
        # Use traditional generate() method
        outputs = await asyncio.to_thread(
            self.llm.generate,
            prompts=[TokensPrompt(prompt_token_ids=r) for r in prompts_or_token_ids],
            sampling_params=sampling_params,
        )

    return self._postprocess_outputs(outputs)
```

#### C. Asynchronous Engine (`AsyncVLLMInferenceEngine`)

**MODIFIED** `generate()` method to conditionally use chat() or generate():

```python
async def generate(self, input_batch: InferenceEngineInput) -> InferenceEngineOutput:
    """Generate responses using vLLM's async engine."""
    prompts_or_token_ids, sampling_params, tools, use_native_tool_calling = self._preprocess_prompts(input_batch)

    if use_native_tool_calling:
        # Use chat() method with tools for async engine
        outputs = []
        for conversation in prompts_or_token_ids:
            # For async engine, we need to use the async chat method
            output = await self.llm.chat(
                messages=conversation,
                sampling_params=sampling_params,
                tools=tools,
                add_generation_prompt=True,
                use_tqdm=False
            )
            outputs.extend(output)  # chat() returns list[RequestOutput]
    else:
        # Use traditional generate() method
        tasks = []
        for prompt in prompts_or_token_ids:
            # Schedule the collection of outputs for each prompt.
            # Avoid duplicate request_ids
            request_id = str(uuid4().hex)
            task = asyncio.create_task(self._collect_outputs(prompt, request_id, sampling_params))
            tasks.append(task)
        outputs = await asyncio.gather(*tasks)

    return self._postprocess_outputs(outputs)
```

### Reasons for Changes

- **Preprocessing Enhancement**: Extract tools and tool calling flag from input batch for engine decision making
- **Conditional Generation**: Use appropriate VLLM method based on `use_native_tool_calling` flag
- **VLLM chat() Integration**: When enabled, use VLLM's native `chat()` method which supports structured tool calling
- **Output Compatibility**: Both `chat()` and `generate()` return `list[RequestOutput]` so same postprocessing works
- **Async Support**: Handle both synchronous and asynchronous VLLM engines
- **Conversation Iteration**: Process each conversation individually since `chat()` handles single conversations
- **Backward Compatibility**: Traditional `generate()` path remains unchanged

---

## 4. No Changes Made to Other SkyRL Components

### Trainer (`skyrl_train/trainer.py`)
**NO CHANGES** - The trainer was not modified as it operates at a higher level and doesn't need to know about tool calling specifics.

### Other Inference Engines
**NO CHANGES** - Only VLLM engines were modified as they are the only ones supporting the chat() method with tools.

### Other Generator Types
**NO CHANGES** - Only `SkyRLGymGenerator` was modified as it's the one used for gymnasium environments like tau_bench.

---

## Summary of Design Principles

### 1. Backward Compatibility
- All changes are additive and optional
- Existing code continues to work without modification
- Default behavior remains unchanged

### 2. Clean Architecture
- Tools flow cleanly: Environment → Generator → Engine
- Each component has a single responsibility
- Configuration controls behavior at appropriate levels

### 3. Type Safety
- New fields added to TypedDict maintain type checking
- Optional fields prevent breaking existing code
- Clear method signatures document expectations

### 4. Performance Considerations
- Tools are extracted once per trajectory, not per turn
- Conditional logic has minimal overhead when disabled
- Native tool calling should be more efficient than text parsing

### 5. Maintainability
- Changes are localized and well-documented
- Feature can be easily disabled or removed
- Code follows existing patterns and conventions

---

## Configuration Impact

To enable the new functionality, users need to set configuration flags:

```yaml
# In training/configs/tau_bench_config.yaml
generator:
  use_native_tool_calling: true  # Enable in generator

environment:
  skyrl_gym:
    tau_bench:
      use_native_tool_calling: true  # Enable in environment
```

Both flags must be `true` for native tool calling to be active. If either is `false`, the system falls back to traditional text-based parsing.

---

## 5. Debugging and Empty Response Fixes (`skyrl_train/generators/skyrl_gym_generator.py`)

### Changes Made

#### A. Added Debug Logging for Native Tool Calling

**ADDED** debug logging after engine output generation:

```python
# Debug logging for native tool calling
if self.use_native_tool_calling and os.environ.get("DEBUG_PARSER", "0") == "1":
    print(f"\n🎮 GENERATOR DEBUG:")
    print(f"   output type: {type(output)}")
    print(f"   output length: {len(output) if isinstance(output, str) else 'N/A'}")
    print(f"   output preview: {repr(output[:200])}")
```

**ADDED** debug logging for input_ids growth tracking:

```python
if self.use_conversation_multi_turn:
    prev_input_ids_len = len(input_ids)
    chat_history, chat_end_index, loss_mask, input_ids = self._update_engine_input_chat_history(
        chat_history, chat_end_index, loss_mask, input_ids, output, new_obs
    )
    if self.use_native_tool_calling and os.environ.get("DEBUG_PARSER", "0") == "1":
        print(f"   input_ids growth: {prev_input_ids_len} -> {len(input_ids)} (+{len(input_ids) - prev_input_ids_len})")
```

**ADDED** debug logging for response_ids extraction:

```python
# Debug logging before extracting response_ids
if self.use_native_tool_calling and os.environ.get("DEBUG_PARSER", "0") == "1":
    print(f"\n🔍 RESPONSE_IDS EXTRACTION DEBUG:")
    print(f"   initial_prompt_length: {initial_prompt_length}")
    print(f"   input_ids length: {len(input_ids)}")
    print(f"   custom_chat_template: {self.custom_chat_template is not None}")
    print(f"   use_conversation_multi_turn: {self.use_conversation_multi_turn}")
```

**ADDED** debug logging for final response_ids:

```python
# Debug logging for response_ids
if self.use_native_tool_calling and os.environ.get("DEBUG_PARSER", "0") == "1":
    print(f"\n📊 FINAL RESPONSE_IDS DEBUG:")
    print(f"   response_ids length: {len(response_ids)}")
    print(f"   response_ids preview: {response_ids[:20] if response_ids else 'EMPTY'}")
    print(f"   reward: {reward}")
```

#### B. Critical Fix for Empty Response IDs

**ADDED** fallback logic to extract response_ids from chat history when empty:

```python
# CRITICAL FIX: If response_ids is empty but we have a chat history, extract from chat history
if len(response_ids) == 0 and self.use_conversation_multi_turn and len(chat_history) > len(prompt):
    # Extract all assistant messages from chat history
    assistant_messages = []
    for msg in chat_history[len(prompt):]:
        if msg.get("role") == "assistant":
            assistant_messages.append(msg.get("content", ""))
    
    # Tokenize all assistant messages
    if assistant_messages:
        combined_response = " ".join(assistant_messages)
        response_ids = self.tokenizer.encode(combined_response, add_special_tokens=False)
        if self.use_native_tool_calling and os.environ.get("DEBUG_PARSER", "0") == "1":
            print(f"   FALLBACK: Extracted {len(response_ids)} tokens from {len(assistant_messages)} assistant messages")
```

### Reasons for Changes

- **Debug Logging**: Essential for understanding why all 768 responses were being filtered as empty
- **Response ID Extraction Fix**: The core issue was that when using `use_conversation_multi_turn=true` with native tool calling, the `input_ids` weren't being properly updated, resulting in empty `response_ids`
- **Fallback Logic**: Provides a safety net to extract response tokens from the chat history when the normal extraction fails

---

## 6. Enhanced Debug Logging in Trainer (`skyrl_train/trainer.py`)

### Changes Made

**MODIFIED** empty response filtering to add detailed debug logging:

```python
# Filter out empty responses
valid_indices = [i for i, r in enumerate(generator_output["response_ids"]) if len(r) > 0]

# Debug logging for empty responses
if len(valid_indices) < len(uids):
    empty_count = len(uids) - len(valid_indices)
    logger.warning(f"Found {empty_count} empty responses out of {len(uids)} total")
    # Sample a few empty responses for debugging
    empty_indices = [i for i, r in enumerate(generator_output["response_ids"]) if len(r) == 0]
    for idx in empty_indices[:3]:  # Show first 3 empty responses
        logger.debug(f"Empty response at index {idx}:")
        logger.debug(f"  Prompt: {generator_output['prompts'][idx] if 'prompts' in generator_output else 'N/A'}")
        logger.debug(f"  Reward: {generator_output['rewards'][idx] if idx < len(generator_output['rewards']) else 'N/A'}")
```

### Reasons for Changes

- **Better Visibility**: Provides insight into why responses are empty
- **Debugging Aid**: Shows prompts and rewards for empty responses to help diagnose issues
- **Limited Output**: Only shows first 3 empty responses to avoid log spam

---

## 7. Debug Logging in VLLM Engines (`skyrl_train/inference_engines/vllm/vllm_engine.py`)

### Changes Made

**ADDED** debug logging for native tool calling in both sync and async engines:

```python
if use_native_tool_calling:
    # Use chat() method with tools - prompts_or_token_ids is a list of conversations
    import os
    if os.environ.get("DEBUG_PARSER", "0") == "1":
        print(f"\n🚀 VLLM ENGINE DEBUG:")
        print(f"   Using native tool calling: {use_native_tool_calling}")
        print(f"   Number of conversations: {len(prompts_or_token_ids)}")
        print(f"   Tools provided: {tools is not None}")
        if tools:
            print(f"   Number of tools: {len(tools)}")
            print(f"   Tool names: {[t.get('function', {}).get('name', 'unknown') for t in tools]}")
    
    outputs = []
    for i, conversation in enumerate(prompts_or_token_ids):
        if os.environ.get("DEBUG_PARSER", "0") == "1":
            print(f"   🎯 Processing conversation {i+1}")
            print(f"   Conversation length: {len(conversation)} messages")
        
        # ... chat() call ...
        
        if os.environ.get("DEBUG_PARSER", "0") == "1":
            print(f"   📤 Chat output type: {type(output)}")
            print(f"   📤 Chat output length: {len(output) if hasattr(output, '__len__') else 'N/A'}")
            if output and len(output) > 0:
                resp = output[0].outputs[0] if hasattr(output[0], 'outputs') and output[0].outputs else None
                if resp:
                    print(f"   📤 First response text: {repr(resp.text[:100])}...")
```

### Reasons for Changes

- **Tool Verification**: Confirms tools are being passed correctly to VLLM
- **Response Tracking**: Shows what VLLM returns from the chat() method
- **Conversation Insights**: Helps understand the structure of inputs and outputs

---

## Impact of Changes

These debugging additions and fixes address the critical issue where all 768 responses were being filtered as empty, preventing any training from occurring. The root cause was that `response_ids` extraction wasn't working correctly with the combination of `use_conversation_multi_turn=true` and native tool calling.

The fallback mechanism ensures that even if the normal token tracking fails, we can still extract the assistant's responses from the chat history and tokenize them for training.

**ADDED** enhanced debugging for structured tool call outputs:

```python
# Check if this is a structured tool call output that needs processing
if isinstance(output, str) and '<tool_call>' in output:
    print(f"   🔧 Detected structured tool call output")
elif isinstance(output, str) and output.strip().startswith('{') and '"tool_calls"' in output:
    print(f"   🔧 Detected JSON tool call output")
elif not output or (isinstance(output, str) and len(output.strip()) == 0):
    print(f"   ⚠️  WARNING: Empty output detected!")
```

**ADDED** detailed tokenization debugging in `_update_engine_input_chat_history`:

```python
# CRITICAL FIX: For native tool calling, we need to ensure output is properly tokenized
if self.use_native_tool_calling and os.environ.get("DEBUG_PARSER", "0") == "1":
    print(f"\n🔧 TOKENIZING OUTPUT:")
    print(f"   Raw output: {repr(output[:100])}")
    
num_output_tokens = len(self.tokenizer.encode(output, add_special_tokens=False))

# ... later ...

if self.use_native_tool_calling and os.environ.get("DEBUG_PARSER", "0") == "1":
    print(f"   Template diff: {repr(curr[len(prev):])}")
    print(f"   New response tokens: {len(new_resp_tokens)} tokens")
    print(f"   Generation prompt tokens: {len(self.generation_prompt_ids)}")
    print(f"   Original output tokens: {num_output_tokens}")
    print(f"   Added {len(new_resp_tokens)} tokens to input_ids")
    print(f"   Total input_ids length: {len(input_ids)}")
```

These debugging additions help identify exactly where the tokenization process is failing with structured tool call outputs from VLLM's `chat()` method.

---

## 8. Critical Fix for Native Tool Calling Token Handling

### Problem Identified

The core issue was that SkyRL's generator was designed for `generate()` outputs but when using native tool calling with `chat()` method, VLLM provides pre-computed `token_ids` that were being discarded. Instead, the system was re-tokenizing the text output, which caused mismatches and empty `response_ids`.

### Changes Made

#### A. Extended InferenceEngineOutput (`skyrl_train/inference_engines/base.py`)

**ADDED** new field to capture token IDs from VLLM:

```python
class InferenceEngineOutput(TypedDict):
    responses: List[str]
    stop_reasons: List[str]
    response_token_ids: Optional[List[List[int]]]  # Token IDs from VLLM for native tool calling
```

#### B. Enhanced VLLM Engine Output Processing (`skyrl_train/inference_engines/vllm/vllm_engine.py`)

**MODIFIED** `_postprocess_outputs()` to extract token_ids from VLLM's CompletionOutput:

```python
def _postprocess_outputs(self, outputs):
    """Common output processing logic for both generate() and chat() methods."""
    responses: List[str] = []
    stop_reasons: List[str] = []
    response_token_ids: List[List[int]] = []
    
    for output in outputs:
        # ... existing code ...
        resp = output.outputs[0]
        responses.append(resp.text)
        stop_reasons.append(resp.finish_reason)
        
        # Extract token_ids if available (from chat() method)
        if hasattr(resp, 'token_ids') and resp.token_ids is not None:
            response_token_ids.append(resp.token_ids)
        else:
            response_token_ids.append([])  # Empty list for generate() method

    return InferenceEngineOutput(
        responses=responses,
        stop_reasons=stop_reasons,
        response_token_ids=response_token_ids,
    )
```

#### C. Generator Token Handling (`skyrl_train/generators/skyrl_gym_generator.py`)

**ADDED** extraction of pre-computed token_ids from engine output:

```python
# Extract pre-computed token_ids if available (for native tool calling)
output_token_ids = None
if "response_token_ids" in engine_output and engine_output["response_token_ids"]:
    output_token_ids = engine_output["response_token_ids"][0]
```

**MODIFIED** `_update_engine_input_chat_history()` method signature to accept optional token_ids:

```python
def _update_engine_input_chat_history(
    self,
    chat_history: ConversationType,
    chat_end_index: int,
    loss_mask: List[int],
    input_ids: List[int],
    output: str,
    new_obs: ConversationType,
    output_token_ids: Optional[List[int]] = None,  # NEW PARAMETER
):
```

**MODIFIED** token counting logic to use pre-computed tokens when available:

```python
# Use pre-computed token_ids if available (from native tool calling), otherwise tokenize
if output_token_ids is not None and len(output_token_ids) > 0:
    num_output_tokens = len(output_token_ids)
    # Debug logging for pre-computed tokens
else:
    # Fallback: tokenize the output text (for generate() method or when token_ids unavailable)
    num_output_tokens = len(self.tokenizer.encode(output, add_special_tokens=False))
    # Debug logging for tokenized output
```

### Key Benefits

1. **Eliminates Token Mismatch**: Uses VLLM's exact token_ids instead of re-tokenizing text
2. **Maintains Backward Compatibility**: Falls back to text tokenization when token_ids unavailable
3. **Fixes Empty Response Issue**: Proper token counting prevents `response_ids` from being empty
4. **Performance Improvement**: Avoids redundant tokenization when tokens are already available

### Impact

This fix addresses the root cause where all 768 responses were being filtered as empty. The issue was that VLLM's `chat()` method provides structured tool call outputs with pre-computed token_ids, but SkyRL was discarding these and re-tokenizing the text, leading to mismatches in the token tracking logic.

---

## 9. Critical Fix for Chat Template Comparison Logic

### Problem Identified

After implementing token ID extraction, the responses were still empty due to a logic error in `_update_engine_input_chat_history`. The template comparison was happening AFTER adding the assistant response to chat history, causing both `prev` and `curr` templates to include the same content, resulting in empty template diff and zero tokens added to `input_ids`.

**Debug evidence**: 
- "Template diff: ''" (empty string)
- "New response tokens: 0 tokens" 
- "Added 0 tokens to input_ids"

### Root Cause

The sequence was:
1. Add assistant response to `chat_history`
2. Compare `chat_history[:chat_end_index]` vs `chat_history[:chat_end_index + 1]`
3. Both slices included the assistant response, so template diff was empty

### Solution

**MODIFIED** template comparison logic to capture the "before" state properly:

```python
# CRITICAL FIX: Get the template state BEFORE adding assistant response for proper comparison
if not self.custom_chat_template:
    prev_template = self.tokenizer.apply_chat_template(
        chat_history[:chat_end_index], add_generation_prompt=False, tokenize=False
    )

# Add assistant response to chat history
chat_history += [{"role": "assistant", "content": output}]

# ... later ...

# Use the pre-computed previous template and compute current template
prev = prev_template
curr = self.tokenizer.apply_chat_template(
    chat_history[:chat_end_index + 1], add_generation_prompt=False, tokenize=False
)
```

**ADDED** comprehensive debugging to track template comparison:

```python
# Debug the template comparison issue
if self.use_native_tool_calling and os.environ.get("DEBUG_PARSER", "0") == "1":
    print(f"\n🔍 TEMPLATE COMPARISON DEBUG:")
    print(f"   chat_end_index: {chat_end_index}")
    print(f"   chat_history length: {len(chat_history)}")
    print(f"   prev slice: chat_history[:{chat_end_index}] = {len(chat_history[:chat_end_index])} messages")
    print(f"   curr slice: chat_history[:{chat_end_index + 1}] = {len(chat_history[:chat_end_index + 1])} messages")
    print(f"   Template diff length: {len(curr) - len(prev)}")
```

### Impact

This fix ensures that:
1. Template comparison captures the actual difference introduced by the assistant response
2. `new_resp_tokens` correctly represents the assistant's output in tokenized form
3. `input_ids` grows properly with each turn
4. `response_ids` extraction succeeds instead of returning empty arrays

This should resolve the final blocker preventing training from proceeding.

---

## 10. Multi-Domain Training Support

### Files Modified:
- `skyrl_train/trainer.py`
- `skyrl_train/entrypoints/main_base.py`
- `skyrl_train/utils/trainer_utils.py`

### Changes Made:

#### A. Retail Validation Dataset Support (`trainer.py`)

**ADDED** method to set retail validation dataset:
```python
def set_retail_eval_dataset(self, retail_eval_dataset: Optional[PromptDataset]):
    """Set the retail validation dataset for multi-domain training evaluation."""
    self.retail_eval_dataset = retail_eval_dataset
    self.retail_eval_dataloader = self.build_dataloader(retail_eval_dataset, is_train=False) if retail_eval_dataset is not None else None
```

**MODIFIED** `eval()` method to evaluate retail validation set separately:
```python
# 5. Evaluate on retail validation set if available
if hasattr(self, 'retail_eval_dataloader') and self.retail_eval_dataloader is not None:
    logger.info("Evaluating on retail validation set...")
    # ... evaluation logic ...
    retail_eval_metrics = {
        "eval-retail/average_reward": np.mean(retail_rewards),
        "eval-retail/success_rate": np.mean([r > 0 for r in retail_rewards]),
        "eval-retail/num_samples": len(retail_rewards),
    }
```

#### B. Test Dataset Support

**ADDED** method to load test datasets (`main_base.py`):
```python
def get_test_datasets(self):
    """Load test datasets for evaluation.
    
    Returns:
        dict: Dictionary mapping test set names to PromptDataset objects
    """
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
```

**ADDED** method to set test datasets (`trainer.py`):
```python
def set_test_datasets(self, test_datasets: Dict[str, PromptDataset]):
    """Set test datasets for evaluation during training."""
    self.test_datasets = test_datasets
    self.test_dataloaders = {}
    for name, dataset in test_datasets.items():
        self.test_dataloaders[name] = self.build_dataloader(dataset, is_train=False)
```

**MODIFIED** `eval()` method to evaluate test sets:
```python
# 6. Evaluate on test sets if available
if hasattr(self, 'test_dataloaders') and self.test_dataloaders:
    logger.info(f"Evaluating on {len(self.test_dataloaders)} test sets...")
    
    for test_name, test_dataloader in self.test_dataloaders.items():
        # ... evaluation logic ...
        test_metrics = {
            f"test-{test_name}/average_reward": float(np.mean(test_rewards)),
            f"test-{test_name}/success_rate": float(np.mean([r > 0 for r in test_rewards])),
            f"test-{test_name}/num_samples": len(test_rewards),
        }
```

#### C. Per-Dataset Metrics (`trainer_utils.py`)

**ADDED** function to calculate metrics per data source:
```python
def calculate_per_dataset_metrics(
    concat_generator_outputs: GeneratorOutput,
    concat_uids: List[str],
    concat_data_sources: List[str],
    n_samples_per_prompt: int,
) -> Dict[str, float]:
    """Calculate metrics per data source."""
    # Group indices by data source
    data_source_indices = {}
    for i, data_source in enumerate(concat_data_sources):
        if data_source not in data_source_indices:
            data_source_indices[data_source] = []
        data_source_indices[data_source].append(i)
    
    # Calculate metrics for each data source
    for data_source, indices in data_source_indices.items():
        # ... metric calculation ...
```

### Reasons for Changes:
- Support training on multiple domains with separate validation sets
- Track performance on domain-specific test sets during training
- Enable fine-grained analysis of model performance per domain

---

## 11. WandB Logging Improvements

### Files Modified:
- `skyrl_train/trainer.py`
- `skyrl_train/utils/tracking.py`

### Changes Made:

#### A. Unified Step Counter

**Problem**: Mixed use of `global_step`, `batch_counter`, and `batch_step` caused WandB monotonic step warnings

**Solution**: Introduced unified `total_steps` counter:
```python
# In train() method
self.global_step = 0
self.total_steps = 0  # Unified counter for all WandB logging

# All logging now uses total_steps
self.tracker.log(metrics, step=self.total_steps)
```

**MODIFIED** all logging calls to use `total_steps`:
- Main eval logging: `step=self.total_steps`
- Training metrics: `step=self.total_steps`
- Reward metrics: `step=self.total_steps`
- Test metrics: `step=self.total_steps`

#### B. More Frequent Reward Logging

**ADDED** generation-time logging:
```python
# Log generation rewards immediately for better visibility
if "rewards" in generator_output and len(generator_output["rewards"]) > 0:
    rewards = generator_output["rewards"]
    generation_metrics = {
        "generation/avg_reward": avg_reward,
        "generation/success_rate": success_rate,
        "generation/num_samples": len(rewards),
        "generation/min_reward": min(rewards),
        "generation/max_reward": max(rewards),
    }
    self.tracker.log(generation_metrics, step=self.total_steps)
```

**ADDED** training batch logging:
```python
# Log training rewards immediately after calculation
if "rewards" in training_input and len(training_input["rewards"]) > 0:
    self.total_steps += 1
    train_rewards = training_input["rewards"].cpu().numpy()
    train_reward_metrics = {
        "train/instant_avg_reward": float(np.mean(train_rewards)),
        "train/instant_min_reward": float(np.min(train_rewards)),
        "train/instant_max_reward": float(np.max(train_rewards)),
        "train/instant_std_reward": float(np.std(train_rewards)),
    }
    self.tracker.log(train_reward_metrics, step=self.total_steps)
```

**ADDED** evaluation instant logging:
```python
# Log evaluation rewards immediately for better visibility
eval_reward_metrics = {
    "eval/instant_avg_reward": sum(eval_rewards) / len(eval_rewards),
    "eval/instant_success_rate": sum(1 for r in eval_rewards if r > 0) / len(eval_rewards),
    "eval/instant_num_samples": len(eval_rewards),
    "eval/instant_failure_rate": sum(1 for r in eval_rewards if r == 0) / len(eval_rewards),
}
```

#### C. Removed Aggressive WandB Flushing

**REMOVED** force commit logic in `tracking.py`:
```python
# Removed this problematic code:
# if any("reward" in key or "batch" in key for key in data.keys()):
#     logger_instance.log({}, commit=True)  # Force commit
```

### Impact:
- Eliminated "step X is less than current step Y" warnings
- Reward metrics now appear frequently throughout training
- All metrics on unified timeline in WandB dashboard

---

## 12. Error Handling Improvements

### Files Modified:
- `skyrl_train/trainer.py`
- `skyrl_train/generators/utils.py`
- `skyrl_train/utils/trainer_utils.py`

### Changes Made:

#### A. Empty Response Handling (`trainer.py`)

**ADDED** filtering for empty responses:
```python
# Filter out empty responses
valid_indices = [i for i, r in enumerate(generator_output["response_ids"]) if len(r) > 0]

if len(valid_indices) < len(uids):
    empty_count = len(uids) - len(valid_indices)
    logger.warning(f"Found {empty_count} empty responses out of {len(uids)} total")
```

#### B. Parse Failure Tracking (`trainer.py`)

**ADDED** parse failure rate calculation:
```python
# Calculate parse failure rate (assuming 0 reward means failure)
parse_failures = sum(1 for r in rewards if r == 0)
parse_failure_rate = parse_failures / len(rewards) if rewards else 0

reward_metrics = {
    "reward/parse_failure_rate": parse_failure_rate,
}
```

#### C. Rollout Metrics Recalculation (`generators/utils.py`)

**FIXED** missing rollout_metrics in concatenate_generator_outputs:
```python
# Recalculate rollout_metrics from concatenated data
result["rollout_metrics"] = {
    "generate/min_num_tokens": np.min(num_tokens_arr).item() if len(num_tokens_arr) > 0 else 0,
    "generate/max_num_tokens": np.max(num_tokens_arr).item() if len(num_tokens_arr) > 0 else 0,
    "generate/avg_num_tokens": np.mean(num_tokens_arr).item() if len(num_tokens_arr) > 0 else 0,
    "generate/std_num_tokens": np.std(num_tokens_arr).item() if len(num_tokens_arr) > 0 else 0,
    "generate/avg_tokens_non_zero_rewards": avg_tokens_non_zero_rewards.item(),
    "generate/avg_tokens_zero_rewards": avg_tokens_zero_rewards.item(),
}
```

#### D. Dict/List Type Handling (`trainer_utils.py`)

**FIXED** type mismatch in calculate_per_dataset_metrics:
```python
# Extract subset for this data source - only process list-type fields
subset_generator_output = {}
for key, value in concat_generator_outputs.items():
    if isinstance(value, list):
        subset_generator_output[key] = [value[i] for i in indices]

# Recalculate rollout_metrics for this subset if we have the necessary data
if "response_ids" in subset_generator_output and "rewards" in subset_generator_output:
    # ... recalculation logic ...
```

---

## 13. Import Fixes

### File Modified:
- `skyrl_train/utils/trainer_utils.py`

### Change:
**ADDED** missing numpy import:
```python
import numpy as np
```

### Reason:
Fixed `NameError: name 'np' is not defined` in calculate_per_dataset_metrics

---

## Summary of All Changes

The SkyRL framework has been extensively enhanced to support:

1. **Native VLLM Tool Calling**: Full integration with VLLM's chat() method for structured tool calling
2. **Multi-Domain Training**: Support for training on multiple domains with separate validation sets
3. **Test Set Evaluation**: Automatic evaluation on test sets during training
4. **Improved Logging**: Unified step counter with frequent reward updates
5. **Better Error Handling**: Graceful handling of empty responses and parsing failures
6. **Version Compatibility**: Fixed vLLM version checking
7. **Type Safety**: Fixed type mismatches in metrics calculation

All changes maintain backward compatibility and can be disabled through configuration.