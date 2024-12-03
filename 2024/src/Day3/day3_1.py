import re

# Read the input file content
with open("/home/z/Documents/Projects/AdventOfCode/2024/Day3/", "r") as file:
    data = file.read()

# Define a regex to extract valid mul(X,Y) patterns
pattern = r"mul\((\d+),(\d+)\)"

# Find all matches for the pattern
matches = re.findall(pattern, data)

# Calculate the sum of the products of the valid mul(X,Y) instructions
result = sum(int(x) * int(y) for x, y in matches)
result
