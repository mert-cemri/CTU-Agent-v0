#!/usr/bin/env python3
"""
Simple test for CTU-Agent-v0 improvements that doesn't require environment setup
"""

import json
import os

def test_model_upgrade():
    """Test that model has been upgraded to Qwen3-8B"""
    print("=" * 80)
    print("TESTING MODEL UPGRADE")
    print("=" * 80)
    
    config_path = "/Users/mertcemri/Desktop/initials/CTU-Agent-v0/training/configs/tau_bench_config.yaml"
    
    try:
        with open(config_path, 'r') as f:
            config_content = f.read()
        
        checks = [
            ("Policy model updated", "Qwen/Qwen3-8B" in config_content and "policy:" in config_content),
            ("Reference model updated", "Qwen/Qwen3-8B" in config_content and "ref:" in config_content),
            ("Old model removed", "Qwen2.5-1.5B" not in config_content)
        ]
        
        passed = 0
        for check_name, passed_check in checks:
            status = "✓ PASSED" if passed_check else "✗ FAILED"
            print(f"{status}: {check_name}")
            if passed_check:
                passed += 1
        
        print(f"\nModel Upgrade Tests: {passed}/{len(checks)} passed")
        return passed, len(checks)
        
    except Exception as e:
        print(f"✗ FAILED to read config file: {e}")
        return 0, 1

def test_system_prompt_improvements():
    """Test system prompt improvements by checking the env.py file"""
    print("\n" + "=" * 80)
    print("TESTING SYSTEM PROMPT IMPROVEMENTS")
    print("=" * 80)
    
    env_path = "/Users/mertcemri/Desktop/initials/CTU-Agent-v0/tau_bench_env/env.py"
    
    try:
        with open(env_path, 'r') as f:
            env_content = f.read()
        
        checks = [
            ("OpenAI tool_calls format", '"tool_calls":' in env_content),
            ("Specific examples", "find_user_id_by_name_zip" in env_content),
            ("JSON string format", '\\"first_name\\"' in env_content),
            ("Critical instructions", "CRITICAL INSTRUCTIONS" in env_content),
            ("Token warnings", "<|im_end|>" in env_content)
        ]
        
        passed = 0
        for check_name, passed_check in checks:
            status = "✓ PASSED" if passed_check else "✗ FAILED"
            print(f"{status}: {check_name}")
            if passed_check:
                passed += 1
        
        print(f"\nSystem Prompt Tests: {passed}/{len(checks)} passed")
        return passed, len(checks)
        
    except Exception as e:
        print(f"✗ FAILED to read env.py file: {e}")
        return 0, 1

def test_parser_improvements():
    """Test parser improvements by checking the parser.py file"""
    print("\n" + "=" * 80)
    print("TESTING PARSER IMPROVEMENTS")
    print("=" * 80)
    
    parser_path = "/Users/mertcemri/Desktop/initials/CTU-Agent-v0/tau_bench_env/parser.py"
    
    try:
        with open(parser_path, 'r') as f:
            parser_content = f.read()
        
        checks = [
            ("OpenAI tool_calls function", "_extract_openai_tool_calls" in parser_content),
            ("Debug logging", "DEBUG_PARSER" in parser_content),
            ("Tool_calls parsing", '"tool_calls"' in parser_content and "parsed" in parser_content),
            ("Token stripping", "<|im_end|>" in parser_content),
            ("Success indicators", "Successfully parsed" in parser_content)
        ]
        
        passed = 0
        for check_name, passed_check in checks:
            status = "✓ PASSED" if passed_check else "✗ FAILED"
            print(f"{status}: {check_name}")
            if passed_check:
                passed += 1
        
        print(f"\nParser Improvement Tests: {passed}/{len(checks)} passed")
        return passed, len(checks)
        
    except Exception as e:
        print(f"✗ FAILED to read parser.py file: {e}")
        return 0, 1

def test_logging_improvements():
    """Test logging improvements by checking trainer.py"""
    print("\n" + "=" * 80)
    print("TESTING LOGGING IMPROVEMENTS")
    print("=" * 80)
    
    trainer_path = "/Users/mertcemri/Desktop/initials/CTU-Agent-v0/SkyRL_mod/skyrl-train/skyrl_train/trainer.py"
    
    try:
        with open(trainer_path, 'r') as f:
            trainer_content = f.read()
        
        checks = [
            ("Generation examples logging", "GENERATION EXAMPLES" in trainer_content),
            ("Batch reward logging", "batch_reward/" in trainer_content),
            ("Batch counter", "batch_counter" in trainer_content),
            ("Example response logging", "response_text" in trainer_content and "reward" in trainer_content),
            ("Frequent logging", "global_step % 50" in trainer_content)
        ]
        
        passed = 0
        for check_name, passed_check in checks:
            status = "✓ PASSED" if passed_check else "✗ FAILED"
            print(f"{status}: {check_name}")
            if passed_check:
                passed += 1
        
        print(f"\nLogging Improvement Tests: {passed}/{len(checks)} passed")
        return passed, len(checks)
        
    except Exception as e:
        print(f"✗ FAILED to read trainer.py file: {e}")
        return 0, 1

def test_conversation_rollouts():
    """Test conversation rollout logging"""
    print("\n" + "=" * 80)
    print("TESTING CONVERSATION ROLLOUT LOGGING")
    print("=" * 80)
    
    env_path = "/Users/mertcemri/Desktop/initials/CTU-Agent-v0/tau_bench_env/env.py"
    
    try:
        with open(env_path, 'r') as f:
            env_content = f.read()
        
        checks = [
            ("Rollout logging method", "_log_conversation_rollout" in env_content),
            ("Conversation display", "CONVERSATION ROLLOUT" in env_content),
            ("User/Assistant emojis", "🧑 USER" in env_content and "🤖 ASSISTANT" in env_content),
            ("Tool call parsing", "🔧 TOOL CALL" in env_content),
            ("Turn-based logging", "turns % 5" in env_content)
        ]
        
        passed = 0
        for check_name, passed_check in checks:
            status = "✓ PASSED" if passed_check else "✗ FAILED"
            print(f"{status}: {check_name}")
            if passed_check:
                passed += 1
        
        print(f"\nConversation Rollout Tests: {passed}/{len(checks)} passed")
        return passed, len(checks)
        
    except Exception as e:
        print(f"✗ FAILED to read env.py file: {e}")
        return 0, 1

def main():
    """Run all improvement tests"""
    print("CTU-Agent-v0 IMPROVEMENT VERIFICATION")
    print("=" * 80)
    
    total_passed = 0
    total_tests = 0
    
    # Run all tests
    tests = [
        test_model_upgrade,
        test_system_prompt_improvements,
        test_parser_improvements,
        test_logging_improvements,
        test_conversation_rollouts
    ]
    
    for test_func in tests:
        try:
            passed, total = test_func()
            total_passed += passed
            total_tests += total
        except Exception as e:
            print(f"Test failed with error: {e}")
            total_tests += 1
    
    # Final summary
    print("\n" + "=" * 80)
    print("✅ VERIFICATION RESULTS")
    print("=" * 80)
    print(f"Total Tests: {total_tests}")
    print(f"Passed: {total_passed}")
    print(f"Success Rate: {total_passed/total_tests*100:.1f}%")
    
    print("\n" + "=" * 80)
    print("🚀 WHAT TO EXPECT FROM IMPROVEMENTS")
    print("=" * 80)
    print("""
The implemented improvements should address the 93.88% parse failure rate:

1. 📝 ENHANCED SYSTEM PROMPT:
   • Clear OpenAI tool_calls format examples
   • Specific retail domain examples (find_user_id_by_name_zip, etc.)
   • Explicit warnings about <|im_end|> tokens
   • Step-by-step JSON structure guidance

2. 🔧 IMPROVED PARSER:
   • New _extract_openai_tool_calls() function prioritized first
   • Better handling of {"tool_calls": [...]} format
   • Strips model tokens like <|im_end|>
   • Enhanced debug logging shows parsing attempts

3. 🤖 UPGRADED MODEL:
   • Qwen/Qwen3-8B (8B parameters vs 1.5B)
   • More capable of following complex instructions
   • Better tool calling capabilities

4. 📊 ENHANCED LOGGING:
   • Generation examples every 50 steps
   • Conversation rollouts every 5 turns
   • Batch-level reward tracking (not just step-level)
   • Parse success/failure indicators

5. 🎯 EXPECTED OUTCOMES:
   • Parse failure rate should drop from 93.88% to <20%
   • More correct tool_calls format generations
   • Better success rates in task completion
   • Improved observability of training process
""")
    
    print("\n" + "=" * 80)
    print("📋 INSTRUCTIONS FOR GPU TRAINING")
    print("=" * 80)
    print("""
Run on your GPU machine:

1. Setup:
   export OPENAI_API_KEY="your-key"
   export DEBUG_PARSER=1
   export WANDB_API_KEY="your-key"

2. Training:
   cd CTU-Agent-v0/SkyRL_mod/skyrl-train
   source .venv/bin/activate
   bash ../../training/run_tau_bench.sh

3. Monitor (in separate terminals):
   # Parse debug output:
   tail -f $HOME/ckpts/tau_bench/logs/train.log | grep -E "(PARSER|tool_calls)"
   
   # Conversation rollouts:
   tail -f $HOME/ckpts/tau_bench/logs/train.log | grep -A15 "CONVERSATION ROLLOUT"
   
   # Generation examples:  
   tail -f $HOME/ckpts/tau_bench/logs/train.log | grep -A8 "GENERATION EXAMPLES"

4. Key metrics to track in W&B:
   • reward/parse_failure_rate (should decrease)
   • batch_reward/parse_failure_rate (more frequent updates)
   • reward/avg_raw_reward (should increase)
   • batch_reward/avg_raw_reward (batch-level tracking)

Please share:
✅ Parse failure rate trends
✅ Examples of generated tool_calls
✅ Conversation rollout logs
✅ Overall success rate improvements
""")

if __name__ == "__main__":
    main()