#!/usr/bin/env python3
"""
Verify that all model references have been updated to Qwen3-8B
"""

import os

def check_file_for_model(filepath, filename):
    """Check a file for model references"""
    try:
        with open(filepath, 'r') as f:
            content = f.read()
        
        has_qwen3_8b = "Qwen/Qwen3-8B" in content or "Qwen3-8B" in content
        has_old_model = "Qwen2.5-1.5B" in content or "qwen1_5b" in content
        
        print(f"\n📁 {filename}:")
        if has_qwen3_8b:
            print("  ✅ Contains Qwen3-8B references")
        if has_old_model:
            print("  ⚠️  Still contains old model references")
        if not has_qwen3_8b and not has_old_model:
            print("  ℹ️  No model references found")
            
        return has_qwen3_8b, has_old_model
        
    except Exception as e:
        print(f"  ❌ Error reading {filename}: {e}")
        return False, False

def main():
    print("🔍 VERIFYING QWEN3-8B MODEL UPDATE")
    print("=" * 50)
    
    files_to_check = [
        ("training/configs/tau_bench_config.yaml", "Main config file"),
        ("training/run_tau_bench.sh", "Training script"),
        ("CLAUDE.md", "Documentation"),
    ]
    
    total_files = 0
    updated_files = 0
    files_with_old_refs = 0
    
    for filepath, description in files_to_check:
        full_path = f"/Users/mertcemri/Desktop/initials/CTU-Agent-v0/{filepath}"
        if os.path.exists(full_path):
            total_files += 1
            has_new, has_old = check_file_for_model(full_path, description)
            
            if has_new:
                updated_files += 1
            if has_old:
                files_with_old_refs += 1
        else:
            print(f"\n📁 {description}:")
            print(f"  ❌ File not found: {filepath}")
    
    print("\n" + "=" * 50)
    print("📊 SUMMARY")
    print("=" * 50)
    print(f"Total files checked: {total_files}")
    print(f"Files with Qwen3-8B: {updated_files}")
    print(f"Files with old references: {files_with_old_refs}")
    
    if updated_files == total_files and files_with_old_refs == 0:
        print("\n🎉 SUCCESS: All files updated to Qwen3-8B!")
    elif files_with_old_refs > 0:
        print(f"\n⚠️  WARNING: {files_with_old_refs} files still contain old model references")
    else:
        print(f"\n📝 INFO: {updated_files}/{total_files} files contain Qwen3-8B references")
    
    print("\n" + "=" * 50)
    print("🚀 EXPECTED TRAINING OUTPUT")
    print("=" * 50)
    print("""
When you run training, you should now see:
  policy:
    model:
      path: Qwen/Qwen3-8B
  ref:
    model:
      path: Qwen/Qwen3-8B

Key changes for the 8B model:
✅ Reduced batch sizes for memory efficiency
✅ Increased GPU memory utilization to 0.8
✅ Updated run names to include "qwen3_8b"

The larger model should provide:
🧠 Better instruction following
🔧 Improved tool calling capabilities  
📈 Higher success rates on complex tasks
""")

if __name__ == "__main__":
    main()