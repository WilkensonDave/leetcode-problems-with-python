# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. 
# You may assume that the majority element always exists in the array.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

#solution 1
def check_majority(nums):
    nums.sort()
    n = len(nums)
    middle =  n // 2
    return nums[middle]

nums = [3,2,3]
print(check_majority(nums))

#solution 2
def majority_element(nums):
    if len(nums) == 0:
        return None
    seen = {}
    
    for num in nums:
        seen[num] = seen.get(num, 0) + 1
    
    max_el = max(seen, key=seen.get)
    return max_el

nums = [3,2,3]
print(majority_element(nums))

