# Given an integer array nums, return true if 
# any value appears at least twice in the array,
# and return false if every element is distinct.
# Example 1:

# Input: nums = [1,2,3,1]

# Output: true

# Explanation:

# The element 1 occurs at the indices 0 and 3.

# Example 2:

# Input: nums = [1,2,3,4]

# Output: false
from collections import Counter
def check_diplicate(input):
    
    if len(input) == 0:
        return None
    
    dict = Counter(input)
    
    for value in dict.values():
        if value > 1:
            return True
    return False

nums = [1,2,3,1]
print(check_diplicate(nums))