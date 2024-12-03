from day2_1 import *

# Define a function to check if a report is safe after removing one level
def is_safe_with_dampener(report):
    levels = list(map(int, report.strip().split()))
    n = len(levels)
    
    # Check if the original report is already safe
    if is_safe_report(report):
        return True
    
    # Check each possible removal of a single level
    for i in range(n):
        modified_levels = levels[:i] + levels[i+1:]
        differences = [modified_levels[j+1] - modified_levels[j] for j in range(len(modified_levels) - 1)]
        
        if all(-3 <= diff <= -1 for diff in differences) or all(1 <= diff <= 3 for diff in differences):
            return True
    return False

# Count safe reports considering the Problem Dampener
safe_reports_with_dampener_count = sum(1 for report in data if is_safe_with_dampener(report))

safe_reports_with_dampener_count