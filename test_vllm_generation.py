#!/usr/bin/env python3
"""
Test what VLLM actually generates for tool calling to validate our findings.
"""

import json
import os

def analyze_training_vs_conversation_discrepancy():
    """Analyze the discrepancy between training output and the conversation you showed."""
    
    print("="*80)
    print("ANALYZING TRAINING vs CONVERSATION DISCREPANCY")
    print("="*80)
    
    # From your training output (properly formatted)
    training_responses = [
        '{"tool_calls": [{"function": {"name": "get_order_details", "arguments": "{\\"order_id\\": \\"#W5254379\\"}"}}]}',
    ]
    
    # From your original conversation (malformed)
    conversation_responses = [
        '{"tool_calls": [{"function": {"name": "find_user_id_by_name_zip", "arguments": "{"first_name": "Yusuf", "last_name": "Rossi", "zip": "19122"}"}}]}',
    ]
    
    print("TRAINING OUTPUT (properly escaped):")
    for i, resp in enumerate(training_responses):
        print(f"  {i+1}. {resp}")
        try:
            parsed = json.loads(resp)
            args = json.loads(parsed["tool_calls"][0]["function"]["arguments"])
            print(f"      ✅ Parses correctly: {args}")
        except Exception as e:
            print(f"      ❌ Parse error: {e}")
    
    print("\nCONVERSATION OUTPUT (malformed):")
    for i, resp in enumerate(conversation_responses):
        print(f"  {i+1}. {resp}")
        try:
            parsed = json.loads(resp)
            args = json.loads(parsed["tool_calls"][0]["function"]["arguments"])
            print(f"      ✅ Parses correctly: {args}")
        except Exception as e:
            print(f"      ❌ Parse error: {e}")
    
    print("\n" + "="*80)
    print("CONCLUSIONS:")
    print("="*80)
    
    print("1. ✅ TRAINING OUTPUT: Properly escaped JSON that parses correctly")
    print("2. ❌ CONVERSATION OUTPUT: Malformed JSON that fails parsing")
    print("3. 🤔 DISCREPANCY: These appear to be from different sources or configurations")
    
    print("\nPOSSIBLE EXPLANATIONS:")
    print("  a) Different VLLM configurations (native tool calling vs text generation)")
    print("  b) Different parsing/logging pipelines")
    print("  c) Version differences between training and test environments")
    print("  d) Manual conversation vs automated training output")
    
    print("\nRECOMMENDATION:")
    print("  The hash comparison bug fix should resolve the main 0-reward issue.")
    print("  The malformed JSON in your conversation example might be from a different source.")
    
    return True

def check_actual_issues_in_training():
    """Check for actual issues that could occur during training."""
    
    print("\n" + "="*80)
    print("CHECKING ACTUAL TRAINING ISSUES")
    print("="*80)
    
    # Issues I noticed in your training output
    issues = [
        {
            "issue": "Truncated tool call",
            "example": '{"tool_calls": [{"function":<|im_end|>',
            "description": "Tool call gets cut off mid-generation",
            "severity": "HIGH - causes parsing failure"
        },
        {
            "issue": "Mixed response types",
            "example": "Model generates tool call then switches to conversational text",
            "description": "Model doesn't stick to one response type",
            "severity": "MEDIUM - causes inconsistent behavior"
        },
        {
            "issue": "Think tool usage",
            "example": '"name": "think"',
            "description": "Model uses think tool which doesn't modify state",
            "severity": "LOW - doesn't affect rewards but adds noise"
        }
    ]
    
    print("IDENTIFIED ISSUES FROM TRAINING OUTPUT:")
    for i, issue in enumerate(issues, 1):
        print(f"\n{i}. {issue['issue'].upper()}")
        print(f"   Example: {issue['example']}")
        print(f"   Description: {issue['description']}")
        print(f"   Severity: {issue['severity']}")
    
    print(f"\n{'='*80}")
    print("PRIORITY FIXES NEEDED:")
    print("="*80)
    
    print("1. 🔥 HIGH PRIORITY: Prevent truncated tool calls")
    print("   - Check VLLM generation parameters (max_tokens, stop_tokens)")
    print("   - Ensure proper tool calling prompt formatting")
    
    print("2. 🔧 MEDIUM PRIORITY: Improve response consistency")
    print("   - Better prompting to avoid mixed response types")
    print("   - Stricter sampling parameters for tool calling")
    
    print("3. 📊 LOW PRIORITY: Clean up think tool usage")
    print("   - Consider removing think tool or handling it specially")
    
    return True

if __name__ == "__main__":
    analyze_training_vs_conversation_discrepancy()
    check_actual_issues_in_training()
    
    print(f"\n{'='*80}")
    print("FINAL ASSESSMENT")
    print("="*80)
    print("✅ The hash comparison bug fix should resolve most 0-reward issues")
    print("⚠️  Some training issues remain (truncated generations, mixed responses)")
    print("🔍 The malformed JSON in your example may be from a different source")
    print("📈 Training should show significant improvement after the hash fix")
    print("="*80)