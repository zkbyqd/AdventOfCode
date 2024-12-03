# Reading the provided input file
file_path = "/home/z/Documents/Projects/AdventOfCode/2024/Day1/"

# Loading the data into two separate lists for left and right lists
left_list, right_list = [], []
with open(file_path, "r") as file:
    for line in file:
        left, right = map(int, line.strip().split())
        left_list.append(left)
        right_list.append(right)

# Sorting both lists
left_list.sort()
right_list.sort()

# Calculating the total distance
total_distance = sum(abs(l - r) for l, r in zip(left_list, right_list))

total_distance