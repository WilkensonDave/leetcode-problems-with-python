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

nums = [2,2,1,1,1,2,2]
print(check_majority(nums))

#solution 2
def majority_element(nums):
    if nums is None:
        return None
    
    visited = {}
    
    for num in nums:
        visited[num] = visited.get(num, 0) + 1
    
    max_index = max(visited, key=visited.get)
    return max_index

nums = [2,2,1,1,1,2,2]
print(majority_element(nums))

