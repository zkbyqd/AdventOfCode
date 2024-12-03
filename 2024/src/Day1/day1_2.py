from day1_1 import *
from collections import Counter

# Counting occurrences of each number in the right list
right_counter = Counter(right_list)

# Calculating the similarity score for the left list
similarity_score = sum(left * right_counter[left] for left in left_list)

similarity_score
