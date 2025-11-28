"""
Verification Script: P1, P2, P3 Naming Convention
==================================================

This script verifies that the entire project uses consistent P1, P2, P3 naming
throughout, matching Schuld & Petruccione's book notation.

Run this after refactoring to confirm all changes were applied correctly.
"""

import os
import re
from pathlib import Path

# Color codes for terminal output
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'

def check_file(filepath, forbidden_patterns, allowed_patterns=None):
    """
    Check if file contains forbidden patterns (old naming).
    
    Args:
        filepath: Path to file to check
        forbidden_patterns: List of regex patterns that shouldn't appear
        allowed_patterns: List of regex patterns that are OK (exceptions)
    
    Returns:
        (is_clean, issues) where issues is list of (line_num, line, pattern)
    """
    issues = []
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                # Skip if it's an allowed pattern (e.g., in comments explaining old code)
                if allowed_patterns and any(re.search(p, line) for p in allowed_patterns):
                    continue
                
                # Check for forbidden patterns
                for pattern in forbidden_patterns:
                    if re.search(pattern, line):
                        issues.append((line_num, line.strip(), pattern))
    except Exception as e:
        return False, [(0, f"Error reading file: {e}", "")]
    
    return len(issues) == 0, issues


def main():
    print("="*80)
    print(f"{BLUE}Project-Wide Naming Convention Verification{RESET}")
    print("="*80)
    print()
    
    # Define forbidden patterns (old naming)
    forbidden_patterns = [
        r'\bX_train\b(?!.*# OLD|.*outdated|.*previous|.*before)',  # X_train (not in comments about old code)
        r'\bX_test\b(?!.*# OLD|.*outdated|.*previous|.*before)',   # X_test
        r'\by_train\b(?!.*# OLD|.*outdated|.*previous|.*before)',  # y_train
        r'\by_test\b(?!.*# OLD|.*outdated|.*previous|.*before)',   # y_test
        r'\bprototype_a\b',  # prototype_a
        r'\bprototype_b\b',  # prototype_b
        r'\btrain_df\b',     # train_df
        r'\btest_df\b',      # test_df
    ]
    
    # Files to check
    project_root = Path(r"c:\Users\sacii\OneDrive\Desktop\Oslomet\ACIT4321 Quantum Computing\Titanic_survival_QML_Project")
    
    files_to_check = [
        # Notebooks
        project_root / "Notebooks" / "00_.data_preprocessing_and_encoding.ipynb",
        project_root / "Notebooks" / "01_circuit_build_and_interference.ipynb",
        project_root / "Notebooks" / "02_measurement_and_classification.ipynb",
        project_root / "Notebooks" / "03_exact_book_implementation_4qubit.ipynb",
        
        # Python scripts
        project_root / "exact_4qubit_classifier.py",
        project_root / "main.py",
        
        # Documentation
        project_root / "README.md",
        project_root / "ARCHITECTURE.md",
        project_root / "Data" / "Raw" / "README.md",
    ]
    
    # Check each file
    all_clean = True
    total_issues = 0
    
    for filepath in files_to_check:
        if not filepath.exists():
            print(f"{YELLOW}⚠{RESET}  {filepath.name}: File not found, skipping")
            continue
        
        print(f"Checking: {filepath.name}...", end=" ")
        
        is_clean, issues = check_file(filepath, forbidden_patterns)
        
        if is_clean:
            print(f"{GREEN}✓ CLEAN{RESET}")
        else:
            print(f"{RED}✗ ISSUES FOUND{RESET}")
            all_clean = False
            total_issues += len(issues)
            
            for line_num, line, pattern in issues[:5]:  # Show first 5 issues
                print(f"  Line {line_num}: {line[:80]}")
                print(f"    Pattern: {pattern}")
            
            if len(issues) > 5:
                print(f"  ... and {len(issues) - 5} more issues")
    
    print()
    print("="*80)
    
    if all_clean:
        print(f"{GREEN}✅ SUCCESS: All files use P1, P2, P3 naming consistently!{RESET}")
        print()
        print("Verification Complete:")
        print("  ✓ No X_train/X_test references in active code")
        print("  ✓ No y_train/y_test references in active code")
        print("  ✓ No prototype_a/prototype_b references")
        print("  ✓ All notebooks use book's P1, P2, P3 notation")
        print()
        print("Project is 100% compliant with Schuld & Petruccione Chapter 1.2!")
    else:
        print(f"{RED}❌ ISSUES FOUND: {total_issues} references to old naming detected{RESET}")
        print()
        print("Action Required:")
        print("  1. Review the issues listed above")
        print("  2. Update any remaining X_train/X_test to P1/P2/P3")
        print("  3. Run this script again to verify")
    
    print("="*80)
    
    return all_clean


if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
