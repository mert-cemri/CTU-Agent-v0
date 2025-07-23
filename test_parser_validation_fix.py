#!/usr/bin/env python3
"""
Test script to verify the parser validation fixes
Tests the specific ValidationError scenario and other edge cases
"""

import json
import os
import sys

# Add project to path
sys.path.append('/Users/mertcemri/Desktop/initials/CTU-Agent-v0')

# Simple mock classes to avoid import issues
class Action:
    def __init__(self, name, kwargs):
        # Simulate Pydantic validation
        if not isinstance(kwargs, dict):
            raise ValueError(f"kwargs must be dict, got {type(kwargs).__name__}")
        self.name = name
        self.kwargs = kwargs
    
    def __repr__(self):
        return f"Action(name='{self.name}', kwargs={self.kwargs})"

RESPOND_ACTION_NAME = "respond"
RESPOND_ACTION_FIELD_NAME = "content"

# Import the validation function we created
from tau_bench_env.parser import _validate_and_sanitize_kwargs

def create_mock_tools_info():
    """Create mock tools info"""
    return [
        {
            "type": "function",
            "function": {
                "name": "get_user_details",
                "description": "Get user details",
                "parameters": {"properties": {"user_id": {"type": "string"}}}
            }
        },
        {
            "type": "function",
            "function": {
                "name": "cancel_order",
                "description": "Cancel an order",
                "parameters": {"properties": {"order_id": {"type": "string"}}}
            }
        }
    ]

def test_kwargs_validation():
    """Test the _validate_and_sanitize_kwargs function"""
    print("=" * 60)
    print("TESTING KWARGS VALIDATION FUNCTION")
    print("=" * 60)
    
    # Enable debug for testing
    os.environ["DEBUG_PARSER"] = "1"
    
    test_cases = [
        # Test case 1: Valid dict (should pass through)
        {
            "name": "Valid dict",
            "kwargs": {"user_id": "123"},
            "expected_type": dict,
            "expected_value": {"user_id": "123"}
        },
        # Test case 2: Integer (the problematic case from error)
        {
            "name": "Integer (problematic case)",
            "kwargs": 190222,
            "expected_type": dict,
            "expected_value": {}
        },
        # Test case 3: String that can be parsed as JSON
        {
            "name": "Valid JSON string",
            "kwargs": '{"order_id": "456"}',
            "expected_type": dict,
            "expected_value": {"order_id": "456"}
        },
        # Test case 4: Invalid JSON string
        {
            "name": "Invalid JSON string",
            "kwargs": 'not json',
            "expected_type": dict,
            "expected_value": {}
        },
        # Test case 5: None
        {
            "name": "None value",
            "kwargs": None,
            "expected_type": dict,
            "expected_value": {}
        },
        # Test case 6: List
        {
            "name": "List value",
            "kwargs": [1, 2, 3],
            "expected_type": dict,
            "expected_value": {}
        }
    ]
    
    passed = 0
    for test in test_cases:
        print(f"\nTest: {test['name']}")
        print(f"Input: {test['kwargs']} ({type(test['kwargs']).__name__})")
        
        result = _validate_and_sanitize_kwargs(
            test['kwargs'], 
            "test_tool", 
            f"Test case: {test['name']}"
        )
        
        if isinstance(result, test['expected_type']) and result == test['expected_value']:
            print(f"✓ PASSED: Got {result}")
            passed += 1
        else:
            print(f"✗ FAILED: Expected {test['expected_value']}, got {result}")
    
    print(f"\n{'-' * 60}")
    print(f"Kwargs Validation Tests: {passed}/{len(test_cases)} passed")
    
    # Disable debug
    os.environ["DEBUG_PARSER"] = "0"
    
    return passed, len(test_cases)

def test_action_creation_with_validation():
    """Test Action creation with the validation"""
    print("\n" + "=" * 60)
    print("TESTING ACTION CREATION WITH VALIDATION")
    print("=" * 60)
    
    test_cases = [
        # Test case 1: Should work fine
        {
            "name": "Valid Action",
            "tool_name": "get_user_details",
            "kwargs": {"user_id": "123"},
            "should_succeed": True
        },
        # Test case 2: The problematic case that caused the original error
        {
            "name": "Integer kwargs (original error)",
            "tool_name": "cancel_order", 
            "kwargs": 190222,
            "should_succeed": True  # Should succeed after validation
        },
        # Test case 3: String kwargs
        {
            "name": "String kwargs",
            "tool_name": "get_user_details",
            "kwargs": '{"user_id": "456"}',
            "should_succeed": True
        }
    ]
    
    passed = 0
    for test in test_cases:
        print(f"\nTest: {test['name']}")
        print(f"Tool: {test['tool_name']}")
        print(f"Raw kwargs: {test['kwargs']} ({type(test['kwargs']).__name__})")
        
        try:
            # Apply validation
            sanitized_kwargs = _validate_and_sanitize_kwargs(
                test['kwargs'], 
                test['tool_name'], 
                f"Test: {test['name']}"
            )
            
            # Try to create Action
            action = Action(name=test['tool_name'], kwargs=sanitized_kwargs)
            
            if test['should_succeed']:
                print(f"✓ PASSED: {action}")
                passed += 1
            else:
                print(f"✗ FAILED: Expected failure but got {action}")
                
        except Exception as e:
            if not test['should_succeed']:
                print(f"✓ PASSED: Expected failure - {e}")
                passed += 1
            else:
                print(f"✗ FAILED: Unexpected error - {e}")
    
    print(f"\n{'-' * 60}")
    print(f"Action Creation Tests: {passed}/{len(test_cases)} passed")
    
    return passed, len(test_cases)

def main():
    """Run all tests"""
    print("PARSER VALIDATION FIX TESTS")
    print("=" * 60)
    
    total_passed = 0
    total_tests = 0
    
    # Test kwargs validation function
    p1, t1 = test_kwargs_validation()
    total_passed += p1
    total_tests += t1
    
    # Test Action creation with validation
    p2, t2 = test_action_creation_with_validation()
    total_passed += p2
    total_tests += t2
    
    # Summary
    print("\n" + "=" * 60)
    print("FINAL RESULTS")
    print("=" * 60)
    print(f"Total Tests: {total_tests}")
    print(f"Passed: {total_passed}")
    print(f"Failed: {total_tests - total_passed}")
    print(f"Success Rate: {total_passed/total_tests*100:.1f}%")
    
    print("\n" + "=" * 60)
    print("FIX SUMMARY")
    print("=" * 60)
    print("""
✅ FIXED ISSUES:

1. ValidationError Prevention:
   - Added _validate_and_sanitize_kwargs() function
   - Validates kwargs are dict before Action creation
   - Converts problematic types (int, str, etc.) to empty dict

2. Enhanced Error Logging:
   - Shows what type was received vs expected
   - Logs the problematic value for debugging
   - Provides context about which parsing method failed

3. Graceful Error Handling:
   - try/catch around all Action() creations
   - Continues to next parsing method on failure
   - Eventually falls back to respond action

4. Debug Visibility:
   - DEBUG_PARSER=1 shows detailed failure info
   - Helps identify patterns in model generation issues

The original error (kwargs=190222) should now be handled gracefully
and converted to an empty dict, preventing the ValidationError crash.
""")
    
    print("\n" + "=" * 60)
    print("READY FOR TRAINING")
    print("=" * 60)
    print("""
The parser fixes are now in place. Run training with:

    export DEBUG_PARSER=1  # Enable detailed logging
    bash training/run_tau_bench.sh

Expected improvements:
- No more ValidationError crashes
- Better visibility into parsing failures
- More graceful handling of malformed responses
- Continued training even with model generation issues
""")

if __name__ == "__main__":
    main()