from day3_1 import *

# Define regex patterns for the instructions
mul_pattern = r"mul\((\d+),(\d+)\)"
control_pattern = r"(do\(\)|don't\(\))"

# Find all instructions (both mul and control) in the order they appear
instructions = re.findall(f"{mul_pattern}|{control_pattern}", data)

# Initialize variables to keep track of the state and the result
mul_enabled = True  # At the start, mul instructions are enabled
total = 0

# Process the instructions sequentially
for inst in instructions:
    if inst[2] == "do()":
        mul_enabled = True
    elif inst[2] == "don't()":
        mul_enabled = False
    elif inst[0] and mul_enabled:  # Valid mul instruction and currently enabled
        x, y = int(inst[0]), int(inst[1])
        total += x * y

total