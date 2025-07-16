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
from tau_bench.dataset_loader import load_custom_dataset, filter_tasks_by_domain
from tau_bench.envs.user import UserStrategy
from tau_bench.sft_collector import SFTDataCollector
from tau_bench.sft_types import SFTConfig, SFTDataset


def run(config: RunConfig) -> List[EnvRunResult]:
    """Core function to run conversations for a specific configuration"""
    assert config.env in ["retail", "airline", "telecom", "doordash", "healthcare"], f"Unsupported environment: {config.env}"
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

    # Load custom tasks if provided
    custom_tasks = None
    if config.custom_dataset_path:
        all_tasks = load_custom_dataset(config.custom_dataset_path)
        custom_tasks = filter_tasks_by_domain(all_tasks, config.env)
        print(f"Loaded {len(custom_tasks)} tasks for domain: {config.env}")
    
    env = get_env(
        config.env,
        user_strategy=config.user_strategy,
        user_model=config.user_model,
        user_provider=config.user_model_provider,
        task_split=config.task_split,
        custom_tasks=custom_tasks,
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
    
    # Determine task indices to run
    if config.dataset_start is not None and config.dataset_end is not None:
        idxs = list(range(config.dataset_start, config.dataset_end + 1))
        print(f"Running tasks from dataset range {config.dataset_start} to {config.dataset_end}")
    elif config.task_ids and len(config.task_ids) > 0:
        idxs = config.task_ids
        print(f"Running tasks {config.task_ids}")
    else:
        idxs = list(range(config.start_index, end_index))
        print(f"Running tasks {config.start_index} to {end_index}")
    
    if config.shuffle:
        random.shuffle(idxs)

    def _run(idx: int) -> EnvRunResult:
        isolated_env = get_env(
            config.env,
            user_strategy=config.user_strategy,
            user_model=config.user_model,
            task_split=config.task_split,
            custom_tasks=custom_tasks,
            user_provider=config.user_model_provider,
            task_index=idx,
        )

        try:
            res = agent.solve(env=isolated_env, task_index=idx)
            result = EnvRunResult(
                task_id=idx,
                reward=res.reward,
                info=res.info,
                traj=res.messages,
                trial=0,
            )
        except Exception as e:
            result = EnvRunResult(
                task_id=idx,
                reward=0.0,
                info={"error": str(e), "traceback": traceback.format_exc()},
                traj=[],
                trial=0,
            )
        
        print("✅" if result.reward == 1 else "❌", f"task_id={idx}", result.info)
        
        with lock:
            data = []
            if os.path.exists(ckpt_path):
                with open(ckpt_path, "r") as f:
                    data = json.load(f)
            with open(ckpt_path, "w") as f:
                json.dump(data + [result.model_dump()], f, indent=2)
        
        return result

    with ThreadPoolExecutor(max_workers=config.max_concurrency) as executor:
        results = list(executor.map(_run, idxs))

    display_metrics(results)
    
    with open(ckpt_path, "w") as f:
        json.dump([result.model_dump() for result in results], f, indent=2)
        print(f"\n📄 Results saved to {ckpt_path}")
    
    return results


def _generate_single_conversation(job: dict, base_config: RunConfig, domain: str, agent_strategy: str, user_strategy: str):
    """Generate a single conversation with optimized configuration."""
    
    # Create minimal config for this conversation
    conv_config = RunConfig(
        model_provider=base_config.model_provider,
        user_model_provider=base_config.user_model_provider,
        model=base_config.model,
        user_model=base_config.user_model,
        num_trials=1,
        env=domain,
        agent_strategy=agent_strategy,
        temperature=job['temperature'],
        task_split="train",  # Use fixed value instead of accessing sft_config
        start_index=job['task_id'],
        end_index=job['task_id'] + 1,
        dataset_start=None,
        dataset_end=None,
        log_dir=base_config.log_dir,
        max_concurrency=4,  # Enable internal parallelism
        seed=job['seed'],
        shuffle=0,
        user_strategy=user_strategy,
        few_shot_displays_path=base_config.few_shot_displays_path,
        custom_dataset_path=base_config.custom_dataset_path
    )
    
    # Generate conversation
    try:
        results = run(conv_config)
        return results[0] if results else None
    except Exception as e:
        print(f"    ⚠️ Conversation generation failed for task {job['task_id']}: {str(e)[:50]}...")
        return None

def run_sft_generation(base_config: RunConfig, sft_config: SFTConfig) -> SFTDataset:
    """CLEAN VERSION: Generate SFT dataset by running conversations per task across domains"""
    
    print("🚀 Starting SFT data generation...")
    print(f"Agent strategy: {sft_config.agent_strategies[0]}")
    print(f"User strategy: {sft_config.user_strategies[0]}")
    print(f"Domains: {sft_config.domains}")
    print(f"Conversations per task: {sft_config.conversations_per_task}")
    
    collector = SFTDataCollector(sft_config)
    
    # Use the first (and typically only) strategy from each list
    agent_strategy = sft_config.agent_strategies[0]
    user_strategy = sft_config.user_strategies[0]
    
    # Process each domain
    for domain_idx, domain in enumerate(sft_config.domains):
        print(f"\n📊 Processing domain {domain_idx+1}/{len(sft_config.domains)}: {domain}")
        
        try:
            # Load custom tasks for this domain
            custom_tasks = None
            if base_config.custom_dataset_path:
                all_tasks = load_custom_dataset(base_config.custom_dataset_path)
                custom_tasks = filter_tasks_by_domain(all_tasks, domain)
                print(f"  📋 Loaded {len(custom_tasks)} tasks for domain: {domain}")
            
            # Get environment to determine available tasks
            env = get_env(
                domain,
                user_strategy=user_strategy,
                user_model=base_config.user_model,
                user_provider=base_config.user_model_provider,
                task_split=sft_config.task_splits[0],
                custom_tasks=custom_tasks,
            )
            
            total_tasks = len(env.tasks)
            if total_tasks == 0:
                print(f"  ⚠️ No tasks available for domain {domain}, skipping")
                continue
            
            # Determine task range
            if base_config.dataset_start is not None and base_config.dataset_end is not None:
                start_task = max(0, base_config.dataset_start)
                end_task = min(base_config.dataset_end, total_tasks - 1)
                task_range = list(range(start_task, end_task + 1))
            else:
                task_range = list(range(total_tasks))
            
            expected_conversations = len(task_range) * sft_config.conversations_per_task
            print(f"  🎯 Processing {len(task_range)} tasks × {sft_config.conversations_per_task} conversations = {expected_conversations} total conversations")
            
            # Generate conversations with parallel processing
            successful_conversions = 0
            total_conversations = 0
            
            # Create all conversation jobs upfront
            conversation_jobs = []
            for task_idx, task_id in enumerate(task_range):
                for conv_idx in range(sft_config.conversations_per_task):
                    conversation_jobs.append({
                        'task_id': task_id,
                        'task_idx': task_idx,
                        'conv_idx': conv_idx,
                        'temperature': random.choice(sft_config.temperature_range),
                        'seed': base_config.seed + task_id * 1000 + conv_idx
                    })
            
            print(f"  🚀 Processing {len(conversation_jobs)} conversations in parallel batches")
            
            # Process conversations in parallel batches
            from concurrent.futures import ThreadPoolExecutor, as_completed
            import time
            
            batch_size = min(sft_config.max_parallel_generations, 8)  # Limit for API rate limiting
            batches = [conversation_jobs[i:i+batch_size] for i in range(0, len(conversation_jobs), batch_size)]
            
            start_time = time.time()
            
            for batch_num, batch in enumerate(batches, 1):
                print(f"    📦 Processing batch {batch_num}/{len(batches)} ({len(batch)} conversations)")
                
                with ThreadPoolExecutor(max_workers=len(batch)) as executor:
                    # Submit batch jobs
                    futures = []
                    for job in batch:
                        future = executor.submit(_generate_single_conversation, 
                                               job, base_config, domain, agent_strategy, user_strategy)
                        futures.append((future, job))
                    
                    # Collect batch results
                    batch_successful = 0
                    for future, job in futures:
                        try:
                            result = future.result(timeout=120)  # 2 min timeout per conversation
                            if result:
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
                                    batch_successful += 1
                                    total_conversations += 1
                        except Exception as e:
                            print(f"      ❌ Error in task {job['task_id']}, conv {job['conv_idx']+1}: {str(e)[:50]}...")
                
                # Progress reporting
                elapsed = time.time() - start_time
                rate = successful_conversions / elapsed if elapsed > 0 else 0
                print(f"    ✅ Batch {batch_num} completed: {batch_successful}/{len(batch)} successful ({rate:.2f} conv/sec)")
                
                # Cost tracking
                if sft_config.enable_cost_tracking and sft_config.max_total_cost:
                    if collector.total_cost > sft_config.max_total_cost:
                        print(f"  ⚠️ Max cost limit reached: ${collector.total_cost:.2f}")
                        break
            
            print(f"  ✅ Domain {domain} completed: {successful_conversions}/{total_conversations} conversations successfully converted")
            
        except Exception as e:
            print(f"  ❌ Error processing domain {domain}: {str(e)}")
            import traceback
            traceback.print_exc()
            continue
    
    print(f"\n🎉 SFT generation complete!")
    print(f"Total conversations collected: {len(collector.conversations)}")
    print(f"Total cost: ${collector.total_cost:.2f}")
    
    # Print conversion statistics
    conv_stats = collector.get_conversion_statistics()
    print(f"Conversion success rate: {conv_stats['conversion_success_rate']:.1%}")
    
    # Apply filters
    print("🔍 Applying quality filters...")
    original_count = len(collector.conversations)
    collector = collector.filter_by_quality(
        min_turns=sft_config.min_conversation_turns,
        max_turns=sft_config.max_conversation_turns
    )
    print(f"After quality filtering: {len(collector.conversations)} (filtered out {original_count - len(collector.conversations)})")
    
    return collector.to_dataset()


def agent_factory(tools_info: List[Dict[str, Any]], wiki, config: RunConfig) -> Agent:
    """Factory function to create agents based on strategy"""
    if config.agent_strategy == "tool-calling":
        from tau_bench.agents.tool_calling_agent import ToolCallingAgent
        return ToolCallingAgent(
            tools_info=tools_info,
            wiki=wiki,
            model=config.model,
            provider=config.model_provider,
            temperature=config.temperature,
        )
    elif config.agent_strategy == "act":
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
        assert config.few_shot_displays_path is not None, "Few shot displays path is required"
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
    """Display performance metrics for results"""
    if not results:
        print("No results to display")
        return
        
    def is_successful(reward: float) -> bool:
        return (1 - 1e-6) <= reward <= (1 + 1e-6)

    rewards = [r.reward for r in results]
    avg_reward = sum(rewards) / len(rewards)
    success_count = sum(1 for r in results if is_successful(r.reward))
    
    print(f"🏆 Average reward: {avg_reward:.3f}")
    print(f"✅ Success rate: {success_count}/{len(results)} ({success_count/len(results)*100:.1f}%)") 

def run_sft_generation_with_synthetic_tasks(
    base_config: RunConfig, 
    sft_config: SFTConfig,
    use_synthetic_tasks: bool = True,
    synthetic_task_ratio: float = 2.0,
    synthetic_complexity_range: tuple = (2, 4)
) -> SFTDataset:
    """Legacy function for compatibility - redirects to main function"""
    print("⚠️ Note: run_sft_generation_with_synthetic_tasks is deprecated. Using run_sft_generation instead.")
    return run_sft_generation(base_config, sft_config)
