#!/usr/bin/env python3
"""
Tau-Bench to LLaMA-Factory Converter
Converts tau_bench conversations from OpenAI to ShareGPT format.
"""

import argparse
import json
import logging
from pathlib import Path
from typing import Dict, List, Any
import pandas as pd

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)


def convert_tool_calls(tool_calls: List[Dict]) -> List[Dict[str, str]]:
    """Convert OpenAI tool calls to function_call format."""
    function_calls = []
    for tool_call in tool_calls:
        function = tool_call.get("function", {})
        arguments = function.get("arguments", "{}")
        
        if isinstance(arguments, str):
            try:
                arguments = json.loads(arguments)
            except json.JSONDecodeError:
                arguments = {"raw": arguments}
        
        function_calls.append({
            "from": "function_call",
            "value": json.dumps({
                "name": function.get("name", "unknown"),
                "arguments": arguments
            }, ensure_ascii=False)
        })
    
    return function_calls


def convert_conversation(item: Dict[str, Any]) -> Dict[str, Any]:
    """Convert a single conversation to ShareGPT format."""
    result = {"conversations": [], "system": None, "tools": None}
    
    if item.get("tools"):
        result["tools"] = json.dumps(item["tools"], ensure_ascii=False)
    
    for msg in item.get("messages", []):
        role = msg.get("role")
        content = msg.get("content", "")
        
        if role == "system":
            result["system"] = content
        elif role == "user" and content != "###STOP###":
            result["conversations"].append({"from": "human", "value": content})
        elif role == "assistant":
            if msg.get("tool_calls"):
                result["conversations"].extend(convert_tool_calls(msg["tool_calls"]))
            if content:
                result["conversations"].append({"from": "gpt", "value": content})
        elif role == "tool":
            result["conversations"].append({"from": "observation", "value": content})
    
    # Ensure conversation ends with gpt response
    if result["conversations"] and result["conversations"][-1]["from"] != "gpt":
        result["conversations"].append({"from": "gpt", "value": "Task completed."})
    
    return result


def process_file(file_path: Path) -> List[Dict[str, Any]]:
    """Process a single data file."""
    logger.info(f"Processing {file_path}")
    
    if file_path.suffix == ".parquet":
        df = pd.read_parquet(file_path)
        data = []
        for _, row in df.iterrows():
            messages = row.get("messages", [])
            if isinstance(messages, str):
                messages = json.loads(messages)
            tools = row.get("tools", [])
            if isinstance(tools, str):
                tools = json.loads(tools)
            
            item = {
                "id": row.get("id", f"conv_{len(data)}"),
                "messages": messages,
                "tools": tools
            }
            data.append(convert_conversation(item))
    elif file_path.suffix == ".jsonl":
        data = []
        with open(file_path, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    item = json.loads(line)
                    data.append(convert_conversation(item))
                except json.JSONDecodeError as e:
                    logger.warning(f"Skipping invalid JSON on line {line_num}: {e}")
    else:  # .json
        with open(file_path, 'r', encoding='utf-8') as f:
            raw_data = json.load(f)
        if not isinstance(raw_data, list):
            raw_data = [raw_data]
        data = [convert_conversation(item) for item in raw_data]
    
    logger.info(f"Converted {len(data)} conversations from {file_path}")
    return data


def create_balanced_dataset(domain_data: Dict[str, List]) -> List[Dict]:
    """Create balanced dataset with equal samples per domain."""
    if not domain_data:
        return []
    
    min_size = min(len(data) for data in domain_data.values())
    balanced = []
    for data in domain_data.values():
        balanced.extend(data[:min_size])
    
    logger.info(f"Created balanced dataset: {min_size} samples per domain")
    return balanced


def main():
    parser = argparse.ArgumentParser(description="Convert tau_bench data to LLaMA-Factory format")
    parser.add_argument("--input_dir", required=True, help="Input file or directory with tau_bench data")
    parser.add_argument("--output_dir", default="tau_bench/processed", help="Output directory")
    parser.add_argument("--domain", choices=["airline", "retail", "healthcare", "telecom", "doordash"], 
                       help="Process specific domain only")
    
    args = parser.parse_args()
    
    input_path = Path(args.input_dir)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    if not input_path.exists():
        logger.error(f"Input path {input_path} does not exist")
        return
    
    # Find files to process
    if input_path.is_file():
        if input_path.suffix in [".parquet", ".json", ".jsonl"]:
            files = [input_path]
        else:
            logger.error(f"Unsupported file type: {input_path.suffix}")
            return
    else:
        files = list(input_path.glob("*.parquet")) + list(input_path.glob("*.json")) + list(input_path.glob("*.jsonl"))
    
    if args.domain:
        files = [f for f in files if args.domain in f.stem]
    
    all_data = []
    domain_data = {}
    
    for file_path in files:
        data = process_file(file_path)
        domain = file_path.stem.split('_')[0] if '_' in file_path.stem else "general"
        domain_data[domain] = data
        all_data.extend(data)
    
    # Save datasets
    if all_data:
        # Full dataset
        with open(output_dir / "tau_bench_full.json", 'w', encoding='utf-8') as f:
            json.dump(all_data, f, ensure_ascii=False, indent=2)
        logger.info(f"Saved {len(all_data)} conversations to tau_bench_full.json")
        
        # Balanced dataset
        if len(domain_data) > 1:
            balanced = create_balanced_dataset(domain_data)
            with open(output_dir / "tau_bench_balanced.json", 'w', encoding='utf-8') as f:
                json.dump(balanced, f, ensure_ascii=False, indent=2)
            logger.info(f"Saved {len(balanced)} balanced conversations")
        
        # Tool-focused dataset
        tool_data = [conv for conv in all_data 
                    if any(msg["from"] == "function_call" for msg in conv.get("conversations", []))]
        if tool_data:
            with open(output_dir / "tau_bench_tools.json", 'w', encoding='utf-8') as f:
                json.dump(tool_data, f, ensure_ascii=False, indent=2)
            logger.info(f"Saved {len(tool_data)} tool-focused conversations")
    
    # Domain-specific files
    for domain, data in domain_data.items():
        if data:
            with open(output_dir / f"tau_bench_{domain}.json", 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            logger.info(f"Saved {len(data)} {domain} conversations")
    
    logger.info("Conversion complete!")


if __name__ == "__main__":
    main()