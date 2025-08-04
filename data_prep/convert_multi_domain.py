#!/usr/bin/env python3
"""Convert multiple domain task files to SkyRL format."""

import os
import re
import argparse
from .convert_tau_data import load_tau_bench_data, convert_tau_bench_data
from .prompts import get_all_domains


def detect_domain(filepath: str) -> str:
    """Extract domain from filename like train_tasks_telecom.py -> telecom"""
    filename = os.path.basename(filepath).lower()
    for domain in get_all_domains():
        if domain in filename:
            return domain
    raise ValueError(f"Cannot detect domain from: {filepath}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_files", nargs='+', required=True)
    parser.add_argument("--output_dir", required=True)
    parser.add_argument("--train_ratio", type=float, default=0.9)
    args = parser.parse_args()
    
    # Load and combine all tasks with correct domain
    all_tasks = []
    for filepath in args.input_files:
        domain = detect_domain(filepath)
        tasks = load_tau_bench_data(filepath)
        
        # Add domain to each task
        for task in tasks:
            task['domain'] = domain
        
        all_tasks.extend(tasks)
        print(f"Loaded {len(tasks)} {domain} tasks from {filepath}")
    
    # Convert using existing function
    convert_tau_bench_data(all_tasks, args.output_dir, args.train_ratio)


if __name__ == "__main__":
    main()