#!/usr/bin/env python3
"""Compare results from different model evaluations"""

import argparse
import json
from pathlib import Path
from typing import Dict, List


def load_results(results_dir: Path) -> Dict:
    """Load results from a directory"""
    # Try to find results file
    results_files = list(results_dir.glob("*_full_results.json"))
    
    if not results_files:
        raise FileNotFoundError(f"No results files found in {results_dir}")
    
    results_file = results_files[0]  # Take the first one
    
    with open(results_file, 'r') as f:
        results = json.load(f)
    
    # Also load summary if available
    summary_file = results_dir / "summary" / "evaluation_summary.json"
    summary = {}
    if summary_file.exists():
        with open(summary_file, 'r') as f:
            summary = json.load(f)
    
    return {
        "results": results,
        "summary": summary,
        "name": results_dir.name
    }


def calculate_metrics(results: List[Dict]) -> Dict:
    """Calculate evaluation metrics"""
    total_tasks = len(results)
    successful_tasks = sum(1 for r in results if r['reward'] > 0.9)
    total_reward = sum(r['reward'] for r in results)
    
    return {
        "total_tasks": total_tasks,
        "successful_tasks": successful_tasks,
        "success_rate": successful_tasks / total_tasks if total_tasks > 0 else 0,
        "average_reward": total_reward / total_tasks if total_tasks > 0 else 0,
        "failed_tasks": [r['task_id'] for r in results if r['reward'] < 0.9]
    }


def print_comparison(model_data: List[Dict]):
    """Print comparison table"""
    print("\n" + "="*80)
    print("MODEL COMPARISON RESULTS")
    print("="*80)
    
    # Header
    print(f"{'Model':<25} {'Success Rate':<15} {'Avg Reward':<12} {'Total Tasks':<12}")
    print("-" * 80)
    
    # Results for each model
    for data in model_data:
        metrics = calculate_metrics(data['results'])
        print(f"{data['name']:<25} "
              f"{metrics['success_rate']:<14.1%} "
              f"{metrics['average_reward']:<11.3f} "
              f"{metrics['total_tasks']:<12}")
    
    print("="*80)
    
    # Detailed comparison
    print("\nDETAILED BREAKDOWN:")
    print("-" * 40)
    
    for data in model_data:
        metrics = calculate_metrics(data['results'])
        print(f"\n{data['name']}:")
        print(f"  Success Rate: {metrics['success_rate']:.1%} ({metrics['successful_tasks']}/{metrics['total_tasks']})")
        print(f"  Average Reward: {metrics['average_reward']:.3f}")
        print(f"  Failed Tasks: {len(metrics['failed_tasks'])} tasks")
        
        if len(metrics['failed_tasks']) <= 10:
            print(f"  Failed Task IDs: {metrics['failed_tasks']}")
        else:
            print(f"  First 10 Failed IDs: {metrics['failed_tasks'][:10]}")


def analyze_failure_patterns(model_data: List[Dict]):
    """Analyze common failure patterns"""
    print("\n" + "="*60)
    print("FAILURE PATTERN ANALYSIS")
    print("="*60)
    
    all_failures = {}
    
    for data in model_data:
        failures = [r['task_id'] for r in data['results'] if r['reward'] < 0.9]
        all_failures[data['name']] = set(failures)
    
    # Find common failures
    if len(model_data) >= 2:
        common_failures = set.intersection(*all_failures.values())
        print(f"\nTasks that BOTH models failed: {len(common_failures)}")
        if common_failures:
            sorted_failures = sorted(list(common_failures))
            if len(sorted_failures) <= 20:
                print(f"Common failure task IDs: {sorted_failures}")
            else:
                print(f"First 20 common failures: {sorted_failures[:20]}")
        
        # Find unique failures
        for data in model_data:
            unique_failures = all_failures[data['name']] - set.union(
                *[all_failures[other['name']] for other in model_data if other['name'] != data['name']]
            )
            print(f"\nTasks that ONLY {data['name']} failed: {len(unique_failures)}")
            if unique_failures and len(unique_failures) <= 10:
                print(f"  Unique failure IDs: {sorted(list(unique_failures))}")


def save_comparison_report(model_data: List[Dict], output_file: Path):
    """Save detailed comparison report"""
    report = {
        "timestamp": "2024-01-01T00:00:00",  # You might want to use actual timestamp
        "models": []
    }
    
    for data in model_data:
        metrics = calculate_metrics(data['results'])
        
        model_report = {
            "name": data['name'],
            "metrics": metrics,
            "summary": data.get('summary', {}),
            "task_details": [
                {
                    "task_id": r['task_id'],
                    "reward": r['reward'],
                    "success": r['reward'] > 0.9
                }
                for r in data['results']
            ]
        }
        report["models"].append(model_report)
    
    with open(output_file, 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"\n📄 Detailed report saved to: {output_file}")


def main():
    parser = argparse.ArgumentParser(description="Compare tau-bench evaluation results")
    parser.add_argument("result_dirs", nargs="+", help="Result directories to compare")
    parser.add_argument("--output", type=str, help="Output file for detailed report")
    
    args = parser.parse_args()
    
    # Load all results
    model_data = []
    for result_dir in args.result_dirs:
        try:
            data = load_results(Path(result_dir))
            model_data.append(data)
            print(f"✓ Loaded {len(data['results'])} results from {data['name']}")
        except Exception as e:
            print(f"✗ Failed to load {result_dir}: {e}")
    
    if len(model_data) < 2:
        print("Need at least 2 result directories to compare")
        return
    
    # Print comparison
    print_comparison(model_data)
    analyze_failure_patterns(model_data)
    
    # Save detailed report if requested
    if args.output:
        save_comparison_report(model_data, Path(args.output))


if __name__ == "__main__":
    main()