# SkyRL Repository Changes for Native Tool Calling Implementation

This document lists all changes made to the SkyRL repository (`SkyRL_mod/skyrl-train/`) to implement native VLLM tool calling functionality.

## Overview of Changes

The implementation adds optional native tool calling support to SkyRL's VLLM inference engines, allowing them to use VLLM's `chat()` method with structured tool calling instead of text-based parsing. All changes maintain backward compatibility.

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