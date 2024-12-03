# Read the input file
file_path = "/home/z/Documents/Projects/AdventOfCode/2024/Day2/"
with open(file_path, "r") as file:
    data = file.readlines()

# Define a function to determine if a report is safe
def is_safe_report(report):
    levels = list(map(int, report.strip().split()))
    differences = [levels[i+1] - levels[i] for i in range(len(levels) - 1)]
    
    # Check if differences are within -3 and 3 and are consistent (either all positive or all negative)
    if all(-3 <= diff <= -1 for diff in differences) or all(1 <= diff <= 3 for diff in differences):
        return True
    return False

# Count safe reports
safe_reports_count = sum(1 for report in data if is_safe_report(report))

safe_reports_count
