# Given an integer array nums and an integer k, return true 
# if there are two distinct indices i and j in the array such that
# nums[i] == nums[j] and abs(i - j) <= k.


# Example 1:

# Input: nums = [1,2,3,1], k = 3
# Output: true
# Example 2:

# Input: nums = [1,0,1,1], k = 1
# Output: true
# Example 3:

# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false
from collections import Counter
def check_duplicateII(input, k):
    if len(input) == 0:
        return None
    
    seen = {}
    
    for index, value in enumerate(input):
        if value in seen and abs(seen[value] - index) <= k:
            return True

        seen[value] = index
    
    return False
    
    
nums = [1,2,3,1] 
k = 3

print(check_duplicateII(nums, k))
    