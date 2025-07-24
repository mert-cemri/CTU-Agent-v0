# Tool Calling Implementation Progress Report

## Background
The goal is to enable native VLLM tool calling for the Qwen model to avoid complex text parsing and improve reliability. The user discovered that VLLM's `LLM` class has a `chat()` method that supports the `tools` parameter directly.

## Current Status

### What Has Been Done ✅ IMPLEMENTATION COMPLETE

1. **Created Simple Parser** (`tau_bench_env/simple_parser.py`)
   - 50-line parser for structured tool calling responses
   - Handles OpenAI-compatible format
   - Ready to use when tool calling is enabled

2. **Environment Configuration** ✅ COMPLETED
   - Added `use_native_tool_calling` flag to `tau_bench_env/env.py`
   - Environment can switch between simple parser (for native tool calling) and complex parser (legacy)
   - Added `_convert_tools_to_openai_format()` method to convert tau_bench tools to OpenAI format
   - Tools are passed through metadata when `use_native_tool_calling=true`

3. **Generator Configuration** ✅ COMPLETED
   - Added `use_native_tool_calling: false` to `training/configs/tau_bench_config.yaml`
   - Modified `skyrl_gym_generator.py` to read this config and extract tools from environment
   - Tools are passed to inference engine when enabled

4. **VLLM Engine Integration** ✅ COMPLETED
   - Modified both sync and async VLLM engines to use `chat()` method when `use_native_tool_calling=true`
   - Added tools and use_native_tool_calling fields to `InferenceEngineInput`
   - Maintains backward compatibility with traditional `generate()` method

### What Was Discovered

1. **SkyRL Architecture Issue**
   - SkyRL uses `vllm.LLM.generate()` method (offline inference API)
   - This method does NOT support tools parameter
   - Tool calling requires either:
     - OpenAI chat completions API, OR
     - `vllm.LLM.chat()` method with `tools` parameter

2. **The Solution**
   - User found that VLLM's `LLM` class has a `chat()` method that accepts:
     ```python
     chat(
         messages: list[ChatCompletionMessageParam],
         sampling_params: Optional[SamplingParams] = None,
         tools: Optional[list[dict[str, Any]]] = None,
         ...
     )
     ```
   - This is perfect - we can use this instead of `generate()`

## Detailed TODO List

### 1. Pass Tools from Environment to Generator ✅ COMPLETED
**File**: `tau_bench_env/env.py`
- [x] Add method to get tools in OpenAI format from `self.tools_info`
- [x] Pass tools through environment step output metadata

### 2. Pass Tools from Generator to Engine ✅ COMPLETED
**File**: `skyrl_train/generators/skyrl_gym_generator.py`
- [x] Extract tools from environment (first iteration)
- [x] Add tools to `InferenceEngineInput` when `use_native_tool_calling=true`
- [x] Ensure tools are passed through to the engine

### 3. Modify VLLM Engine to Use Chat Method ✅ COMPLETED
**File**: `skyrl_train/inference_engines/vllm/vllm_engine.py`
- [x] Modify `_preprocess_prompts` to handle tools parameter
- [x] Modify `generate` method to:
  - Check if `use_native_tool_calling` and `prompts` are provided
  - If yes, use `llm.chat()` with tools
  - If no, use existing `llm.generate()` path
- [x] Handle chat() output format (same RequestOutput structure)
- [x] Update both sync and async VLLM engines

### 4. Update InferenceEngineInput Type ✅ COMPLETED
**File**: `skyrl_train/inference_engines/base.py`
- [x] Add optional `tools` field to `InferenceEngineInput`
- [x] Add optional `use_native_tool_calling` field

### 5. Handle Tool Calling Responses ✅ COMPLETED
**File**: `skyrl_train/generators/skyrl_gym_generator.py`
- [x] When `use_native_tool_calling=true`, structured responses are handled by simple_parser.py
- [x] Response passed directly to environment which uses appropriate parser

### 6. Test Integration
- [ ] Test with `use_native_tool_calling: false` (ensure nothing breaks)
- [ ] Test with `use_native_tool_calling: true` (ensure tools are passed and parsed)
- [ ] Compare parse success rates between methods

## Key Implementation Details

### Tools Format
Tools need to be in OpenAI format:
```python
[{
    "type": "function",
    "function": {
        "name": "cancel_order",
        "description": "Cancel a pending order",
        "parameters": {
            "type": "object",
            "properties": {
                "order_id": {"type": "string"}
            },
            "required": ["order_id"]
        }
    }
}]
```

### Environment Integration Points
1. `env.init()` - First time to get tools
2. `env.step()` - Pass tools in metadata if needed
3. Generator extracts tools and passes to engine

### VLLM Chat Method Usage
```python
# Instead of:
outputs = self.llm.generate(prompts=[TokensPrompt(...)])

# Use:
outputs = self.llm.chat(
    messages=prompts,  # Already in chat format
    sampling_params=sampling_params,
    tools=tools,  # Pass tools here
    add_generation_prompt=True,
    use_tqdm=False
)
```

## Important Notes

1. **Backward Compatibility**: Everything must work with `use_native_tool_calling: false`
2. **Optional Feature**: This is opt-in, not default behavior
3. **Environment Config**: Both generator and environment need the flag enabled
4. **VLLM Version**: Requires VLLM version that supports chat() with tools

## Files Modified So Far

1. `tau_bench_env/simple_parser.py` - Created
2. `tau_bench_env/env.py` - Added use_native_tool_calling flag
3. `training/configs/tau_bench_config.yaml` - Added generator.use_native_tool_calling
4. `skyrl_train/generators/skyrl_gym_generator.py` - Started modification
5. `CLAUDE.md` - Updated with current status

## ✅ IMPLEMENTATION COMPLETE

The native tool calling implementation is now complete! Here's what was implemented:

### Core Implementation Changes

1. **Environment Integration** (`tau_bench_env/env.py`):
   - Added `_convert_tools_to_openai_format()` method
   - Tools are passed in metadata during `env.init()` when `use_native_tool_calling=true`

2. **Generator Integration** (`skyrl_train/generators/skyrl_gym_generator.py`):
   - Extracts tools from environment metadata on first iteration
   - Passes tools to `InferenceEngineInput` when enabled
   - Handles both batched and non-batched generation

3. **VLLM Engine Integration** (`skyrl_train/inference_engines/vllm/vllm_engine.py`):
   - Modified `_preprocess_prompts()` to handle tools and tool calling flag
   - Both sync and async engines use `llm.chat()` when `use_native_tool_calling=true`
   - Falls back to traditional `llm.generate()` when disabled

4. **Type System** (`skyrl_train/inference_engines/base.py`):
   - Added `tools` and `use_native_tool_calling` fields to `InferenceEngineInput`

### Ready for Testing

The implementation is complete and ready for testing:

## Configuration When Complete

```yaml
# training/configs/tau_bench_config.yaml
generator:
  use_conversation_multi_turn: true
  use_native_tool_calling: true  # Enable VLLM chat() with tools

environment:
  skyrl_gym:
    tau_bench:
      use_native_tool_calling: true  # Use simple parser for structured responses
```

## Expected Benefits

1. **Reliability**: No more regex parsing of malformed JSON
2. **Performance**: Structured responses from VLLM
3. **Simplicity**: 50-line parser vs 500+ line parser
4. **Standards**: Following OpenAI tool calling format