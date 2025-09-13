# Copyright Sierra

import argparse
import os
from tau_bench.tau_types import RunConfig
from tau_bench.sft_types import SFTConfig
from tau_bench.run import run_sft_generation, run_sft_generation_with_synthetic_tasks
from litellm import provider_list
from tau_bench.envs.user import UserStrategy


def parse_args():
    parser = argparse.ArgumentParser(description="Generate SFT dataset from tau-bench conversations")
    
    # Output configuration
    parser.add_argument("--output-path", required=True, help="Path to save the generated SFT dataset")
    parser.add_argument("--output-format", default="openai", choices=["openai", "alpaca"], 
                       help="Output format for the dataset")
    parser.add_argument("--save-raw", action="store_true", 
                       help="Also save raw dataset with full metadata")
    
    # Generation configuration
    parser.add_argument("--num-conversations", type=int, default=20, 
                       help="Number of conversations per strategy combination")
    parser.add_argument("--dataset-start", type=int, 
                       help="Start index for dataset task range (overrides num-conversations)")
    parser.add_argument("--dataset-end", type=int, 
                       help="End index for dataset task range (overrides num-conversations)")
    parser.add_argument("--domains", nargs="+", choices=["retail", "airline"], 
                       default=["retail", "airline"], help="Domains to generate data for")
    parser.add_argument("--task-splits", nargs="+", choices=["train", "test", "dev"], 
                       default=["train"], help="Task splits to use")
    
    # Agent configuration
    parser.add_argument("--agent-model", type=str, default="gpt-4", 
                       help="Model to use for the agent. "
                            "OpenAI: gpt-4o, gpt-4o-mini, gpt-4-turbo, gpt-4, gpt-3.5-turbo | "
                            "Anthropic: claude-3-5-sonnet-latest, claude-sonnet-4-20250514, claude-3-7-sonnet-latest, claude-3-5-sonnet-20240620, claude-3-opus-20240229, claude-3-sonnet-20240229, claude-3-haiku-20240307")
    parser.add_argument("--agent-model-provider", type=str, choices=provider_list, 
                       default="openai", help="Model provider for the agent (openai, anthropic, etc.)")
    parser.add_argument("--agent-strategies", nargs="+", 
                       choices=["tool-calling", "act", "react", "few-shot"], 
                       default=["tool-calling", "react"], help="Agent strategies to use")
    
    # User simulation configuration
    parser.add_argument("--user-model", type=str, default="gpt-4o", 
                       help="Model to use for user simulation. "
                            "OpenAI: gpt-4o, gpt-4o-mini, gpt-4-turbo, gpt-4, gpt-3.5-turbo | "
                            "Anthropic: claude-3-5-sonnet-latest, claude-sonnet-4-20250514, claude-3-7-sonnet-latest, claude-3-5-sonnet-20240620, claude-3-opus-20240229, claude-3-sonnet-20240229, claude-3-haiku-20240307")
    parser.add_argument("--user-model-provider", type=str, choices=provider_list, 
                       default="openai", help="Model provider for user simulation (openai, anthropic, etc.)")
    parser.add_argument("--user-strategies", nargs="+", 
                       choices=[item.value for item in UserStrategy], 
                       default=["llm", "react"], help="User simulation strategies to use")
    
    # Quality control
    parser.add_argument("--filter-successful", action="store_true", 
                       help="Keep only successful conversations (reward >= 0.99)")
    parser.add_argument("--min-turns", type=int, default=3, 
                       help="Minimum number of turns per conversation")
    parser.add_argument("--max-turns", type=int, default=50, 
                       help="Maximum number of turns per conversation")
    parser.add_argument("--enable-deduplication", action="store_true", 
                       help="Remove duplicate conversations")
    
    # Synthetic task generation
    parser.add_argument("--use-synthetic-tasks", action="store_true",
                       help="Generate synthetic tasks to enhance diversity")
    parser.add_argument("--synthetic-task-ratio", type=float, default=2.0,
                       help="Ratio of synthetic to original tasks (e.g., 2.0 = 2x synthetic tasks)")
    parser.add_argument("--synthetic-complexity-min", type=int, default=2,
                       help="Minimum complexity level for synthetic tasks (1-5)")
    parser.add_argument("--synthetic-complexity-max", type=int, default=4,
                       help="Maximum complexity level for synthetic tasks (1-5)")
    
    # Model configuration
    parser.add_argument("--temperature-range", nargs="+", type=float, 
                       default=[0.0, 0.3, 0.7], help="Temperature values to use for diversity")
    
    # Generation control
    parser.add_argument("--max-parallel", type=int, default=4, 
                       help="Maximum parallel conversation generations")
    parser.add_argument("--max-cost", type=float, help="Maximum total cost limit")
    parser.add_argument("--log-dir", type=str, default="sft_logs", 
                       help="Directory to save generation logs")
    parser.add_argument("--seed", type=int, default=42,
                       help="Random seed for reproducible generation")
    parser.add_argument("--disable-shuffle", action="store_true",
                       help="Disable task shuffling (run tasks in sequential order)")
    
    # Optional paths
    parser.add_argument("--few-shot-displays-path", type=str, 
                       help="Path to few-shot displays file (required for few-shot strategy)")
    
    # Error handling and reporting
    parser.add_argument("--save-errors", action="store_true",
                       help="Save detailed error reports for failed conversions")
    
    args = parser.parse_args()
    
    # Validation
    if "few-shot" in args.agent_strategies and not args.few_shot_displays_path:
        parser.error("--few-shot-displays-path is required when using few-shot agent strategy")
    
    if args.synthetic_complexity_min < 1 or args.synthetic_complexity_min > 5:
        parser.error("--synthetic-complexity-min must be between 1 and 5")
    
    if args.synthetic_complexity_max < 1 or args.synthetic_complexity_max > 5:
        parser.error("--synthetic-complexity-max must be between 1 and 5")
    
    if args.synthetic_complexity_min > args.synthetic_complexity_max:
        parser.error("--synthetic-complexity-min must be <= --synthetic-complexity-max")
    
    # Validate dataset range arguments
    if (args.dataset_start is not None) != (args.dataset_end is not None):
        parser.error("Both --dataset-start and --dataset-end must be provided together")
    
    if args.dataset_start is not None and args.dataset_end is not None:
        if args.dataset_start > args.dataset_end:
            parser.error("--dataset-start must be <= --dataset-end")
        if args.dataset_start < 0:
            parser.error("--dataset-start must be >= 0")
    
    # Validate model and provider compatibility
    openai_models = ["gpt-4o", "gpt-4o-mini", "gpt-4-turbo", "gpt-4", "gpt-3.5-turbo", 
                     "gpt-4o-2024-08-06", "gpt-4o-2024-05-13", "gpt-4-turbo-2024-04-09", 
                     "gpt-4o-mini-2024-07-18", "gpt-3.5-turbo-0125", "gpt-3.5-turbo-instruct"]
    anthropic_models = ["claude-3-5-sonnet-latest", "claude-sonnet-4-20250514", "claude-3-7-sonnet-latest",
                        "claude-3-5-sonnet-20240620", "claude-3-opus-20240229", 
                        "claude-3-sonnet-20240229", "claude-3-haiku-20240307"]
    
    # Validate agent model/provider compatibility
    if args.agent_model_provider == "openai" and args.agent_model not in openai_models:
        if args.agent_model in anthropic_models:
            parser.error(f"Model '{args.agent_model}' is an Anthropic model but provider is set to 'openai'. Use --agent-model-provider anthropic")
        else:
            parser.error(f"Model '{args.agent_model}' is not a recognized OpenAI model. Available: {', '.join(openai_models)}")
    
    if args.agent_model_provider == "anthropic" and args.agent_model not in anthropic_models:
        if args.agent_model in openai_models:
            parser.error(f"Model '{args.agent_model}' is an OpenAI model but provider is set to 'anthropic'. Use --agent-model-provider openai")
        else:
            parser.error(f"Model '{args.agent_model}' is not a recognized Anthropic model. Available: {', '.join(anthropic_models)}")
    
    # Validate user model/provider compatibility
    if args.user_model_provider == "openai" and args.user_model not in openai_models:
        if args.user_model in anthropic_models:
            parser.error(f"User model '{args.user_model}' is an Anthropic model but provider is set to 'openai'. Use --user-model-provider anthropic")
        else:
            parser.error(f"User model '{args.user_model}' is not a recognized OpenAI model. Available: {', '.join(openai_models)}")
    
    if args.user_model_provider == "anthropic" and args.user_model not in anthropic_models:
        if args.user_model in openai_models:
            parser.error(f"User model '{args.user_model}' is an OpenAI model but provider is set to 'anthropic'. Use --user-model-provider openai")
        else:
            parser.error(f"User model '{args.user_model}' is not a recognized Anthropic model. Available: {', '.join(anthropic_models)}")
    
    return args


def main():
    args = parse_args()
    
    print("🤖 Tau-Bench SFT Data Generation Pipeline")
    print("=" * 50)
    print(f"Output path: {args.output_path}")
    print(f"Agent Model: {args.agent_model} (provider: {args.agent_model_provider})")
    print(f"User Model: {args.user_model} (provider: {args.user_model_provider})")
    print(f"Agent strategies: {args.agent_strategies}")
    print(f"User strategies: {args.user_strategies}")
    print(f"Domains: {args.domains}")
    if args.dataset_start is not None and args.dataset_end is not None:
        print(f"Dataset range: {args.dataset_start} to {args.dataset_end} (total: {args.dataset_end - args.dataset_start + 1} tasks)")
    else:
        print(f"Conversations per combination: {args.num_conversations}")
    if args.use_synthetic_tasks:
        print(f"🎲 Synthetic tasks enabled:")
        print(f"  - Task ratio: {args.synthetic_task_ratio}x")
        print(f"  - Complexity range: {args.synthetic_complexity_min}-{args.synthetic_complexity_max}")
        print(f"  - Method: Using tau-bench native synthetic tasks")
    
    # Model compatibility note
    print(f"\n🔧 Model Configuration:")
    if args.agent_model_provider == "openai":
        print(f"  🔵 OpenAI Agent: Requires OPENAI_API_KEY environment variable")
    elif args.agent_model_provider == "anthropic":
        print(f"  🟠 Anthropic Agent: Requires ANTHROPIC_API_KEY environment variable")
    
    if args.user_model_provider == "openai":
        print(f"  🔵 OpenAI User: Requires OPENAI_API_KEY environment variable")
    elif args.user_model_provider == "anthropic":
        print(f"  🟠 Anthropic User: Requires ANTHROPIC_API_KEY environment variable")
    
    print(f"\n💡 Tip: Use --help to see all available model options for each provider")
    
    # Reproducibility information
    print(f"\n🔒 Reproducibility Settings:")
    print(f"  - Seed: {args.seed}")
    print(f"  - Shuffle enabled: {not args.disable_shuffle}")
    print(f"  - Task ID mapping: PRESERVED (task 0 = same instruction)")
    print("=" * 50)
    
    # Validation warning for existing datasets
    if os.path.exists(args.output_path):
        print("⚠️  Output file already exists. New generation will use corrected task ID mapping.")
        print("   Previous datasets may have corrupted task instructions.")
        print("   See TASK_INSTRUCTION_INTEGRITY_REPORT.md for details.")
        print()
    
    # Create output directory
    os.makedirs(os.path.dirname(args.output_path), exist_ok=True)
    os.makedirs(args.log_dir, exist_ok=True)
    
    # Create base run configuration
    base_config = RunConfig(
        model_provider=args.agent_model_provider,
        user_model_provider=args.user_model_provider,
        model=args.agent_model,
        user_model=args.user_model,
        num_trials=1,
        env="retail",  # Will be overridden per combination
        agent_strategy="tool-calling",  # Will be overridden per combination
        temperature=0.0,  # Will be randomized per combination
        task_split="train",  # Will be randomized per combination
        dataset_start=args.dataset_start,
        dataset_end=args.dataset_end,
        log_dir=args.log_dir,
        max_concurrency=args.max_parallel,
        seed=args.seed,
        shuffle=not args.disable_shuffle,
        user_strategy="llm",  # Will be overridden per combination
        few_shot_displays_path=args.few_shot_displays_path
    )
    
    # Create SFT configuration
    # Calculate the number of conversations based on dataset range if provided
    if args.dataset_start is not None and args.dataset_end is not None:
        num_conversations_per_combination = args.dataset_end - args.dataset_start + 1
    else:
        num_conversations_per_combination = args.num_conversations
    
    sft_config = SFTConfig(
        agent_strategies=args.agent_strategies,
        user_strategies=args.user_strategies,
        num_conversations_per_combination=num_conversations_per_combination,
        domains=args.domains,
        task_splits=args.task_splits,
        filter_successful_only=args.filter_successful,
        min_conversation_turns=args.min_turns,
        max_conversation_turns=args.max_turns,
        enable_deduplication=args.enable_deduplication,
        temperature_range=args.temperature_range,
        output_formats=[args.output_format],
        max_parallel_generations=args.max_parallel,
        enable_cost_tracking=bool(args.max_cost),
        max_total_cost=args.max_cost,
        enable_quality_scoring=True,
        quality_threshold=0.7,
        seed=args.seed,
        enable_shuffle=not args.disable_shuffle
    )
    
    try:
        # Generate SFT dataset
        print("\n🚀 Starting SFT data generation...")
        
        if args.use_synthetic_tasks:
            dataset = run_sft_generation_with_synthetic_tasks(
                base_config=base_config, 
                sft_config=sft_config,
                use_synthetic_tasks=True,
                synthetic_task_ratio=args.synthetic_task_ratio,
                synthetic_complexity_range=(args.synthetic_complexity_min, args.synthetic_complexity_max)
            )
        else:
            dataset = run_sft_generation(base_config, sft_config)
        
        # Print final statistics
        print("\n📊 Final Dataset Statistics:")
        stats = dataset.statistics
        print(f"  Total conversations: {stats.get('total_conversations', 0)}")
        print(f"  Successful conversations: {stats.get('successful_conversations', 0)}")
        print(f"  Success rate: {stats.get('success_rate', 0):.2%}")
        print(f"  Avg turns per conversation: {stats.get('avg_turns_per_conversation', 0):.1f}")
        print(f"  Avg tool calls per conversation: {stats.get('avg_tool_calls_per_conversation', 0):.1f}")
        print(f"  Total generation cost: ${stats.get('total_generation_cost', 0):.2f}")
        
        # Print conversion statistics if available
        if 'conversion_success_rate' in stats:
            print(f"  Conversion success rate: {stats.get('conversion_success_rate', 0):.2%}")
            if stats.get('failed_conversions', 0) > 0:
                print(f"  Failed conversions: {stats.get('failed_conversions', 0)}")
        
        # Print strategy distribution
        if 'agent_strategy_distribution' in stats:
            print(f"\n📈 Strategy Distribution:")
            print(f"  Agent strategies: {stats['agent_strategy_distribution']}")
            print(f"  User strategies: {stats['user_strategy_distribution']}")
            print(f"  Domains: {stats['domain_distribution']}")
        
        # Export dataset
        print(f"\n💾 Exporting dataset to {args.output_path}...")
        if args.output_format == "openai":
            dataset.export_openai_format(args.output_path)
        elif args.output_format == "alpaca":
            dataset.export_alpaca_format(args.output_path)
        
        # Save raw dataset if requested
        if args.save_raw:
            raw_path = args.output_path.replace(".jsonl", "_raw.json").replace(".json", "_raw.json")
            print(f"💾 Saving raw dataset to {raw_path}...")
            with open(raw_path, 'w') as f:
                f.write(dataset.model_dump_json(indent=2))
        
        # Save error report if requested and there were errors
        if args.save_errors and stats.get('failed_conversions', 0) > 0:
            error_path = args.output_path.replace(".jsonl", "_errors.json").replace(".json", "_errors.json")
            print(f"⚠️ Saving error report to {error_path}...")
            # This would require access to the collector, which we don't have here
            # In a full implementation, we'd need to refactor to access the collector's error report
            print("   (Error report functionality requires collector access - to be implemented)")
        
        print("\n✅ SFT data generation completed successfully!")
        print(f"📄 Dataset saved to: {args.output_path}")
        if args.save_raw:
            print(f"📄 Raw dataset saved to: {raw_path}")
        
        # Summary recommendations
        print(f"\n💡 Quick Quality Assessment:")
        success_rate = stats.get('success_rate', 0)
        if success_rate > 0.8:
            print("   ✅ High success rate - excellent dataset quality")
        elif success_rate > 0.6:
            print("   🟡 Moderate success rate - consider filtering or reviewing generation parameters")
        else:
            print("   🔴 Low success rate - recommend reviewing task difficulty and agent capabilities")
        
        avg_turns = stats.get('avg_turns_per_conversation', 0)
        if 5 <= avg_turns <= 15:
            print("   ✅ Good conversation length distribution")
        elif avg_turns < 5:
            print("   🟡 Short conversations - consider encouraging longer interactions")
        else:
            print("   🟡 Long conversations - consider setting stricter turn limits")
            
    except Exception as e:
        print(f"\n❌ Error during SFT data generation: {str(e)}")
        import traceback
        traceback.print_exc()
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())