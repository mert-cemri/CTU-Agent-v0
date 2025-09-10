# Simplified Reward Structure Changes

**Date**: 2025-01-10  
**Change**: Removed intermediate rewards and step-wise taxonomy feedback to eliminate length exploitation  

## Problem Identified

The previous reward system incentivized longer conversations:
```python
# PROBLEMATIC (old system):
# Step 1: reward = 0.1 (tool call) + 0.2 (taxonomy)  
# Step 2: reward = 0.1 (tool call) + 0.3 (taxonomy)
# Step 3: reward = 1.0 (completion) + 0.4 (taxonomy) 
# Total: 2.1 → Model learns to drag out conversations!
```

## Changes Made

### 1. **Removed Intermediate Reward Shaping**
**Before**: `+0.1` for each tool call (added by SkyRL wrapper, NOT tau_bench)  
**After**: `0.0` for all intermediate steps  

### 2. **Moved Taxonomy Feedback to End-of-Conversation Only**  
**Before**: LLM Judge evaluated every step → accumulated bonuses  
**After**: LLM Judge evaluates complete conversation once at the end  

### 3. **Clean Outcome-Based Learning**
```python
# NEW SIMPLIFIED SYSTEM:
# Step 1-N: reward = 0.0  # No intermediate rewards
# Final step: reward = tau_bench_outcome (0 or 1) + single_taxonomy_bonus
# Total: Clean outcome reward (no length exploitation)
```

## Implementation Details

**File Modified**: `tau_bench_env/env.py`  
**Lines**: 454-544  

**New Logic**:
```python
if done:
    # Final reward from tau_bench (0 or 1)
    reward = tau_result.reward
    
    # Single taxonomy evaluation of complete conversation
    judge_reward_bonus = llm_judge.evaluate_conversation_step(conversation_history)
    reward += judge_reward_bonus
else:
    # No intermediate rewards
    reward = 0.0
```

## Benefits

✅ **No Length Exploitation**: Same reward regardless of conversation length  
✅ **Cleaner Learning Signal**: Focus on task completion quality  
✅ **Simpler Implementation**: One reward calculation instead of step-wise accumulation  
✅ **Better GRPO Alignment**: Single outcome reward per conversation  
✅ **Preserved Functionality**: All old code commented out for easy rollback  

## GRPO Integration

This change aligns perfectly with GRPO's outcome-based advantage computation:
```python
# GRPO still works the same way:
scores = token_level_rewards.sum(dim=-1)  # Sum across tokens
# But now only final tokens have non-zero rewards
# Result: Clean single outcome score per conversation
```

## Backward Compatibility

All old functionality is preserved as commented code:
- Old intermediate reward shaping: Lines 497-508
- Old step-wise taxonomy feedback: Lines 510-544  

Can be easily re-enabled by uncommenting if needed for experimentation.

## Testing

The system should now show:
- No reward accumulation during conversation steps
- Single final reward = task_completion (0 or 1) + taxonomy_bonus
- Cleaner reward signals in training logs
- No incentive for unnecessarily long conversations