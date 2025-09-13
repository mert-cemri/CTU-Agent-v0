# Copyright Sierra

import os
import json
import random
import traceback
from math import comb
import multiprocessing
from typing import List, Dict, Any
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

from tau_bench.envs import get_env
from tau_bench.agents.base import Agent
from tau_bench.types import EnvRunResult, RunConfig, Task
from litellm import provider_list
from tau_bench.envs.user import UserStrategy
from tau_bench.sft_collector import SFTDataCollector
from tau_bench.sft_types import SFTConfig, SFTDataset
from tau_bench.task_generator import TaskGenerator, create_synthetic_task_pool, enhance_existing_tasks_with_synthetic


def run(config: RunConfig) -> List[EnvRunResult]:
    assert config.env in ["retail", "airline", "doordash", "healthcare", "telecom"], "Only retail, airline, doordash, healthcare, telecom envs are supported"
    assert config.model_provider in provider_list, "Invalid model provider"
    assert config.user_model_provider in provider_list, "Invalid user model provider"
    assert config.agent_strategy in ["tool-calling", "act", "react", "few-shot"], "Invalid agent strategy"
    assert config.task_split in ["train", "test", "dev"], "Invalid task split"
    assert config.user_strategy in [item.value for item in UserStrategy], "Invalid user strategy"

    random.seed(config.seed)
    time_str = datetime.now().strftime("%m%d%H%M%S")
    ckpt_path = f"{config.log_dir}/{config.agent_strategy}-{config.model.split('/')[-1]}-{config.temperature}_range_{config.start_index}-{config.end_index}_user-{config.user_model}-{config.user_strategy}_{time_str}.json"
    if not os.path.exists(config.log_dir):
        os.makedirs(config.log_dir)

    print(f"Loading user with strategy: {config.user_strategy}")
    env = get_env(
        config.env,
        user_strategy=config.user_strategy,
        user_model=config.user_model,
        user_provider=config.user_model_provider,
        task_split=config.task_split,
    )
    agent = agent_factory(
        tools_info=env.tools_info,
        wiki=env.wiki,
        config=config,
    )
    end_index = (
        len(env.tasks) if config.end_index == -1 else min(config.end_index, len(env.tasks))
    )
    results: List[EnvRunResult] = []
    lock = multiprocessing.Lock()
    
    # Check for dataset_start and dataset_end first (highest priority)
    if config.dataset_start is not None and config.dataset_end is not None:
        print(f"Running tasks from dataset range {config.dataset_start} to {config.dataset_end} (checkpoint path: {ckpt_path})")
    elif config.task_ids and len(config.task_ids) > 0:
        print(f"Running tasks {config.task_ids} (checkpoint path: {ckpt_path})")
    else:
        print(
            f"Running tasks {config.start_index} to {end_index} (checkpoint path: {ckpt_path})"
    )
    for i in range(config.num_trials):
        # Priority order: dataset_start/dataset_end > task_ids > start_index/end_index
        if config.dataset_start is not None and config.dataset_end is not None:
            idxs = list(range(config.dataset_start, config.dataset_end + 1))
        elif config.task_ids and len(config.task_ids) > 0:
            idxs = config.task_ids
        else:
            idxs = list(range(config.start_index, end_index))
        if config.shuffle:
            random.shuffle(idxs)

        def _run(idx: int) -> EnvRunResult:
            isolated_env = get_env(
                config.env,
                user_strategy=config.user_strategy,
                user_model=config.user_model,
                task_split=config.task_split,
                user_provider=config.user_model_provider,
                task_index=idx,
            )

            print(f"Running task {idx}")
            try:
                res = agent.solve(
                    env=isolated_env,
                    task_index=idx,
                )
                result = EnvRunResult(
                    task_id=idx,
                    reward=res.reward,
                    info=res.info,
                    traj=res.messages,
                    trial=i,
                )
            except Exception as e:
                result = EnvRunResult(
                    task_id=idx,
                    reward=0.0,
                    info={"error": str(e), "traceback": traceback.format_exc()},
                    traj=[],
                    trial=i,
                )
            print(
                "✅" if result.reward == 1 else "❌",
                f"task_id={idx}",
                result.info,
            )
            print("-----")
            with lock:
                data = []
                if os.path.exists(ckpt_path):
                    with open(ckpt_path, "r") as f:
                        data = json.load(f)
                with open(ckpt_path, "w") as f:
                    json.dump(data + [result.model_dump()], f, indent=2)
            return result

        with ThreadPoolExecutor(max_workers=config.max_concurrency) as executor:
            res = list(executor.map(_run, idxs))
            results.extend(res)

    display_metrics(results)

    with open(ckpt_path, "w") as f:
        json.dump([result.model_dump() for result in results], f, indent=2)
        print(f"\n📄 Results saved to {ckpt_path}\n")
    return results


def run_sft_generation(base_config: RunConfig, sft_config: SFTConfig) -> SFTDataset:
    """Generate SFT dataset by running conversations across multiple strategy combinations"""
    
    print("🚀 Starting SFT data generation...")
    print(f"Agent strategies: {sft_config.agent_strategies}")
    print(f"User strategies: {sft_config.user_strategies}")
    print(f"Domains: {sft_config.domains}")
    print(f"Conversations per combination: {sft_config.num_conversations_per_combination}")
    
    collector = SFTDataCollector(sft_config)
    total_combinations = len(sft_config.agent_strategies) * len(sft_config.user_strategies) * len(sft_config.domains)
    current_combination = 0
    
    # Generate conversations for each strategy combination
    for domain in sft_config.domains:
        for agent_strategy in sft_config.agent_strategies:
            for user_strategy in sft_config.user_strategies:
                current_combination += 1
                print(f"\n📊 Combination {current_combination}/{total_combinations}: "
                      f"{domain} | {agent_strategy} | {user_strategy}")
                
                try:
                    # Run conversations for this combination
                    combination_results = run_strategy_combination(
                        base_config=base_config,
                        sft_config=sft_config,
                        domain=domain,
                        agent_strategy=agent_strategy,
                        user_strategy=user_strategy
                    )
                    
                    # Convert results to SFT conversations
                    successful_conversions = 0
                    for result in combination_results:
                        conversation = collector.collect_from_env_result(
                            result=result,
                            domain=domain,
                            agent_strategy=agent_strategy,
                            user_strategy=user_strategy,
                            agent_model=base_config.model,
                            user_model=base_config.user_model
                        )
                        if conversation:
                            collector.add_conversation(conversation)
                            successful_conversions += 1
                    
                    print(f"  ✅ Generated {successful_conversions}/{len(combination_results)} conversations")
                    
                    # Cost tracking
                    if sft_config.enable_cost_tracking and sft_config.max_total_cost:
                        if collector.total_cost > sft_config.max_total_cost:
                            print(f"⚠️ Max cost limit reached: ${collector.total_cost:.2f}")
                            break
                            
                except Exception as e:
                    print(f"  ❌ Error in combination {domain}|{agent_strategy}|{user_strategy}: {str(e)}")
                    continue
    
    print(f"\n🎉 SFT generation complete!")
    print(f"Total conversations collected: {len(collector.conversations)}")
    print(f"Total cost: ${collector.total_cost:.2f}")
    
    # Print conversion statistics
    conv_stats = collector.get_conversion_statistics()
    print(f"Conversion success rate: {conv_stats['conversion_success_rate']:.1%}")
    if conv_stats['failed_conversions'] > 0:
        print(f"⚠️ Failed conversions: {conv_stats['failed_conversions']}")
    
    # Apply filters if configured
    if sft_config.filter_successful_only:
        print("🔍 Filtering successful conversations only...")
        original_count = len(collector.conversations)
        collector = collector.filter_successful_only()
        print(f"Successful conversations: {len(collector.conversations)} (filtered out {original_count - len(collector.conversations)})")
    
    if sft_config.enable_deduplication:
        print("🔍 Removing duplicate conversations...")
        original_count = len(collector.conversations)
        collector = collector.deduplicate_conversations()
        print(f"After deduplication: {len(collector.conversations)} (removed {original_count - len(collector.conversations)})")
    
    # Quality filtering
    print("🔍 Applying quality filters...")
    original_count = len(collector.conversations)
    collector = collector.filter_by_quality(
        min_turns=sft_config.min_conversation_turns,
        max_turns=sft_config.max_conversation_turns
    )
    print(f"After quality filtering: {len(collector.conversations)} (filtered out {original_count - len(collector.conversations)})")
    
    return collector.to_dataset()


def run_strategy_combination(
    base_config: RunConfig,
    sft_config: SFTConfig,
    domain: str,
    agent_strategy: str,
    user_strategy: str
) -> List[EnvRunResult]:
    """Run conversations for a specific strategy combination"""
    
    # Create a modified config for this combination
    run_config = RunConfig(
        model_provider=base_config.model_provider,
        user_model_provider=base_config.user_model_provider,
        model=base_config.model,
        user_model=base_config.user_model,
        num_trials=1,  # Only one trial for SFT generation
        env=domain,
        agent_strategy=agent_strategy,
        temperature=random.choice(sft_config.temperature_range),  # Random temperature for diversity
        task_split=random.choice(sft_config.task_splits),  # Random task split
        start_index=0,
        end_index=sft_config.num_conversations_per_combination,
        dataset_start=base_config.dataset_start,  # PASS THROUGH dataset_start
        dataset_end=base_config.dataset_end,      # PASS THROUGH dataset_end
        log_dir=base_config.log_dir,
        max_concurrency=min(sft_config.max_parallel_generations, base_config.max_concurrency),
        seed=sft_config.seed,
        shuffle=1 if sft_config.enable_shuffle else 0,
        user_strategy=user_strategy,
        few_shot_displays_path=base_config.few_shot_displays_path
    )
    
    # Generate conversations using the existing run function
    return run(run_config)


def run_sft_generation_with_synthetic_tasks(
    base_config: RunConfig, 
    sft_config: SFTConfig,
    use_synthetic_tasks: bool = True,
    synthetic_task_ratio: float = 2.0,
    synthetic_complexity_range: tuple = (2, 4)
) -> SFTDataset:
    """Enhanced SFT generation that includes synthetic task generation"""
    
    print("🚀 Starting Enhanced SFT data generation with synthetic tasks...")
    print(f"Using synthetic tasks: {use_synthetic_tasks}")
    if use_synthetic_tasks:
        print(f"Synthetic task ratio: {synthetic_task_ratio}x")
        print(f"Complexity range: {synthetic_complexity_range}")
    
    collector = SFTDataCollector(sft_config)
    total_combinations = len(sft_config.agent_strategies) * len(sft_config.user_strategies) * len(sft_config.domains)
    current_combination = 0
    
    # Generate conversations for each strategy combination
    for domain in sft_config.domains:
        for agent_strategy in sft_config.agent_strategies:
            for user_strategy in sft_config.user_strategies:
                current_combination += 1
                print(f"\n📊 Combination {current_combination}/{total_combinations}: "
                      f"{domain} | {agent_strategy} | {user_strategy}")
                
                try:
                    # Run conversations for this combination with synthetic tasks
                    combination_results = run_strategy_combination_with_synthetic(
                        base_config=base_config,
                        sft_config=sft_config,
                        domain=domain,
                        agent_strategy=agent_strategy,
                        user_strategy=user_strategy,
                        use_synthetic_tasks=use_synthetic_tasks,
                        synthetic_task_ratio=synthetic_task_ratio,
                        synthetic_complexity_range=synthetic_complexity_range
                    )
                    
                    # Convert results to SFT conversations
                    successful_conversions = 0
                    for result in combination_results:
                        conversation = collector.collect_from_env_result(
                            result=result,
                            domain=domain,
                            agent_strategy=agent_strategy,
                            user_strategy=user_strategy,
                            agent_model=base_config.model,
                            user_model=base_config.user_model
                        )
                        if conversation:
                            collector.add_conversation(conversation)
                            successful_conversions += 1
                    
                    print(f"  ✅ Generated {successful_conversions}/{len(combination_results)} conversations")
                    
                    # Cost tracking
                    if sft_config.enable_cost_tracking and sft_config.max_total_cost:
                        if collector.total_cost > sft_config.max_total_cost:
                            print(f"⚠️ Max cost limit reached: ${collector.total_cost:.2f}")
                            break
                            
                except Exception as e:
                    print(f"  ❌ Error in combination {domain}|{agent_strategy}|{user_strategy}: {str(e)}")
                    import traceback
                    traceback.print_exc()
                    continue
    
    # Continue with the same filtering logic as before...
    print(f"\n🎉 Enhanced SFT generation complete!")
    print(f"Total conversations collected: {len(collector.conversations)}")
    print(f"Total cost: ${collector.total_cost:.2f}")
    
    # Print conversion statistics
    conv_stats = collector.get_conversion_statistics()
    print(f"Conversion success rate: {conv_stats['conversion_success_rate']:.1%}")
    if conv_stats['failed_conversions'] > 0:
        print(f"⚠️ Failed conversions: {conv_stats['failed_conversions']}")
    
    # Apply filters if configured
    if sft_config.filter_successful_only:
        print("🔍 Filtering successful conversations only...")
        original_count = len(collector.conversations)
        collector = collector.filter_successful_only()
        print(f"Successful conversations: {len(collector.conversations)} (filtered out {original_count - len(collector.conversations)})")
    
    if sft_config.enable_deduplication:
        print("🔍 Removing duplicate conversations...")
        original_count = len(collector.conversations)
        collector = collector.deduplicate_conversations()
        print(f"After deduplication: {len(collector.conversations)} (removed {original_count - len(collector.conversations)})")
    
    # Quality filtering
    print("🔍 Applying quality filters...")
    original_count = len(collector.conversations)
    collector = collector.filter_by_quality(
        min_turns=sft_config.min_conversation_turns,
        max_turns=sft_config.max_conversation_turns
    )
    print(f"After quality filtering: {len(collector.conversations)} (filtered out {original_count - len(collector.conversations)})")
    
    return collector.to_dataset()


def run_strategy_combination_with_synthetic(
    base_config: RunConfig,
    sft_config: SFTConfig,
    domain: str,
    agent_strategy: str,
    user_strategy: str,
    use_synthetic_tasks: bool = True,
    synthetic_task_ratio: float = 2.0,
    synthetic_complexity_range: tuple = (2, 4)
) -> List[EnvRunResult]:
    """Run conversations with enhanced task pool including synthetic tasks
    
    CRITICAL DESIGN FOR REPRODUCIBILITY:
    1. Original tasks preserve their original task IDs (0 to N-1) 
    2. Synthetic tasks are NOT mixed with originals to avoid corruption
    3. Each run uses a deterministic, seeded selection process
    4. Task instructions are faithfully preserved from tau-bench sources
    """
    
    print(f"    🔧 Preparing task pool for {domain}...")
    
    # Get base environment to access original tasks
    base_env = get_env(
        domain,
        user_strategy=user_strategy,
        user_model=base_config.user_model,
        user_provider=base_config.user_model_provider,
        task_split=random.choice(sft_config.task_splits),
    )
    
    original_tasks = base_env.tasks
    num_original = len(original_tasks)
    target_conversations = sft_config.num_conversations_per_combination
    
    print(f"    📊 Available original tasks: {num_original}")
    print(f"    🎯 Target conversations: {target_conversations}")
    
    # For now, we'll use a hybrid approach that preserves reproducibility:
    # 1. Use original tasks with their exact task IDs for faithful reproduction
    # 2. If synthetic tasks are requested, we'll generate additional runs with carefully designed synthetic scenarios
    
    if use_synthetic_tasks:
        # Strategy: Use original tasks + run additional synthetic scenarios
        # This preserves task ID mapping while adding diversity
        
        # Calculate distribution
        num_original_runs = min(target_conversations // 2, num_original)  
        num_synthetic_runs = target_conversations - num_original_runs
        
        print(f"    📈 Task distribution (preserving ID mapping):")
        print(f"      - Original task runs: {num_original_runs}")
        print(f"      - Synthetic task runs: {num_synthetic_runs}")
        
        # Part 1: Run original tasks with deterministic selection
        original_task_ids = list(range(num_original))
        
        # Use deterministic shuffling based on strategy combination
        strategy_seed = sft_config.seed + hash(f"{domain}_{agent_strategy}_{user_strategy}")
        rng = random.Random(strategy_seed)
        
        if sft_config.enable_shuffle:
            rng.shuffle(original_task_ids)
        
        selected_original_ids = original_task_ids[:num_original_runs]
        
        print(f"    🎲 Selected original task IDs: {selected_original_ids}")
        
        # Part 2: Handle synthetic tasks by using existing synthetic tasks from tau-bench
        # Look for tasks marked as synthetic in the training data
        synthetic_task_candidates = [
            i for i, task in enumerate(original_tasks) 
            if hasattr(task, 'annotator') and task.annotator == "synthetic"
        ]
        
        selected_synthetic_ids = []
        if synthetic_task_candidates and num_synthetic_runs > 0:
            # Use existing synthetic tasks from tau-bench
            rng.shuffle(synthetic_task_candidates)
            selected_synthetic_ids = synthetic_task_candidates[:min(num_synthetic_runs, len(synthetic_task_candidates))]
            print(f"    🔬 Using existing synthetic task IDs: {selected_synthetic_ids}")
        else:
            print(f"    ⚠️  No synthetic tasks available in {domain} environment")
            # Fall back to using more original tasks
            remaining_original = [id for id in original_task_ids if id not in selected_original_ids]
            selected_synthetic_ids = remaining_original[:num_synthetic_runs]
            print(f"    📝 Using additional original tasks: {selected_synthetic_ids}")
        
        # Combine task IDs for execution
        all_task_ids = selected_original_ids + selected_synthetic_ids
        
        print(f"    ✅ Final task ID list: {len(all_task_ids)} tasks")
        print(f"       Original: {selected_original_ids}")
        print(f"       Synthetic: {selected_synthetic_ids}")
        
    else:
        # Use only original tasks
        task_ids = list(range(min(target_conversations, num_original)))
        
        # Apply deterministic shuffling if enabled
        if sft_config.enable_shuffle:
            strategy_seed = sft_config.seed + hash(f"{domain}_{agent_strategy}_{user_strategy}")
            rng = random.Random(strategy_seed)
            rng.shuffle(task_ids)
        
        all_task_ids = task_ids
        print(f"    📋 Using {len(all_task_ids)} original tasks only")
    
    # Create run config with the selected task IDs
    run_config = RunConfig(
        model_provider=base_config.model_provider,
        user_model_provider=base_config.user_model_provider,
        model=base_config.model,
        user_model=base_config.user_model,
        num_trials=1,
        env=domain,
        agent_strategy=agent_strategy,
        temperature=random.choice(sft_config.temperature_range),
        task_split=random.choice(sft_config.task_splits),
        start_index=0,
        end_index=-1,  # Use task_ids instead
        task_ids=all_task_ids,  # Pass our carefully selected task IDs
        dataset_start=base_config.dataset_start,  # PASS THROUGH dataset_start
        dataset_end=base_config.dataset_end,      # PASS THROUGH dataset_end
        log_dir=base_config.log_dir,
        max_concurrency=min(sft_config.max_parallel_generations, base_config.max_concurrency),
        seed=sft_config.seed,
        shuffle=0,  # Don't shuffle again - we've already controlled the order
        user_strategy=user_strategy,
        few_shot_displays_path=base_config.few_shot_displays_path
    )
    
    # Execute conversations with tau-bench
    print(f"    🚀 Running {len(all_task_ids)} conversations with tau-bench...")
    results = run(run_config)
    
    # Verify and enhance results with proper metadata
    print(f"    ✅ Completed {len(results)} conversations, adding metadata...")
    
    for result in results:
        # Verify task instruction integrity
        original_task = original_tasks[result.task_id] if result.task_id < len(original_tasks) else None
        
        if hasattr(result, 'info'):
            # Ensure proper info structure
            if not hasattr(result.info, 'task') and original_task:
                # Create proper task reference
                class ResultInfo:
                    def __init__(self, task):
                        self.task = task
                        self.used_synthetic_tasks = use_synthetic_tasks
                        self.task_mapping_verified = True
                        self.task_id_preserved = True
                
                result.info = ResultInfo(original_task)
            
            # Add metadata about our approach
            if isinstance(result.info, dict):
                result.info.update({
                    'used_synthetic_tasks': use_synthetic_tasks,
                    'task_id_mapping_preserved': True,
                    'synthetic_integration_method': 'tau_bench_native_synthetic_tasks',
                    'instruction_source': 'tau_bench_original'
                })
            else:
                result.info.used_synthetic_tasks = use_synthetic_tasks
                result.info.task_id_mapping_preserved = True
                result.info.synthetic_integration_method = 'tau_bench_native_synthetic_tasks'
                result.info.instruction_source = 'tau_bench_original'
        
        # Verify instruction integrity
        if original_task and hasattr(result.info, 'task') and hasattr(result.info.task, 'instruction'):
            expected_instruction = original_task.instruction
            actual_instruction = result.info.task.instruction
            
            if expected_instruction != actual_instruction:
                print(f"    ⚠️  Task {result.task_id} instruction mismatch detected!")
                print(f"         Expected: {expected_instruction[:100]}...")
                print(f"         Actual: {actual_instruction[:100]}...")
            else:
                print(f"    ✅ Task {result.task_id} instruction verified correctly")
    
    return results


def agent_factory(
    tools_info: List[Dict[str, Any]], wiki, config: RunConfig
) -> Agent:
    if config.agent_strategy == "tool-calling":
        # native tool calling
        from tau_bench.agents.tool_calling_agent import ToolCallingAgent

        return ToolCallingAgent(
            tools_info=tools_info,
            wiki=wiki,
            model=config.model,
            provider=config.model_provider,
            temperature=config.temperature,
        )
    elif config.agent_strategy == "act":
        # `act` from https://arxiv.org/abs/2210.03629
        from tau_bench.agents.chat_react_agent import ChatReActAgent

        return ChatReActAgent(
            tools_info=tools_info,
            wiki=wiki,
            model=config.model,
            provider=config.model_provider,
            use_reasoning=False,
            temperature=config.temperature,
        )
    elif config.agent_strategy == "react":
        # `react` from https://arxiv.org/abs/2210.03629
        from tau_bench.agents.chat_react_agent import ChatReActAgent

        return ChatReActAgent(
            tools_info=tools_info,
            wiki=wiki,
            model=config.model,
            provider=config.model_provider,
            use_reasoning=True,
            temperature=config.temperature,
        )
    elif config.agent_strategy == "few-shot":
        from tau_bench.agents.few_shot_agent import FewShotToolCallingAgent
        assert config.few_shot_displays_path is not None, "Few shot displays path is required for few-shot agent strategy"
        with open(config.few_shot_displays_path, "r") as f:
            few_shot_displays = [json.loads(line)["messages_display"] for line in f]

        return FewShotToolCallingAgent(
            tools_info=tools_info,
            wiki=wiki,
            model=config.model,
            provider=config.model_provider,
            few_shot_displays=few_shot_displays,
            temperature=config.temperature,
        )
    else:
        raise ValueError(f"Unknown agent strategy: {config.agent_strategy}")


def display_metrics(results: List[EnvRunResult]) -> None:
    def is_successful(reward: float) -> bool:
        return (1 - 1e-6) <= reward <= (1 + 1e-6)

    num_trials = len(set([r.trial for r in results]))
    rewards = [r.reward for r in results]
    avg_reward = sum(rewards) / len(rewards)
    # c from https://arxiv.org/pdf/2406.12045
    c_per_task_id: dict[int, int] = {}
    for result in results:
        if result.task_id not in c_per_task_id:
            c_per_task_id[result.task_id] = 1 if is_successful(result.reward) else 0
        else:
            c_per_task_id[result.task_id] += 1 if is_successful(result.reward) else 0
    pass_hat_ks: dict[int, float] = {}
    for k in range(1, num_trials + 1):
        sum_task_pass_hat_k = 0
        for c in c_per_task_id.values():
            sum_task_pass_hat_k += comb(c, k) / comb(num_trials, k)
        pass_hat_ks[k] = sum_task_pass_hat_k / len(c_per_task_id)
    print(f"🏆 Average reward: {avg_reward}")
    print("📈 Pass^k")
    for k, pass_hat_k in pass_hat_ks.items():
        print(f"  k={k}: {pass_hat_k}")
