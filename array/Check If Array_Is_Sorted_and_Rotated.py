# Given an array nums, return true if the array was originally sorted in non-decreasing order, 
# then rotated some number of positions (including zero). Otherwise, return false.

# There may be duplicates in the original array.

# Note: An array A rotated by x positions results in 
# an array B of the same length such that B[i] == A[(i+x) % A.length] for every valid index i.

# Example 1:

# Input: nums = [3,4,5,1,2]
# Output: true
# Explanation: [1,2,3,4,5] is the original sorted array.
# You can rotate the array by x = 2 positions to begin on the element of value 3: [3,4,5,1,2].
# Example 2:

# Input: nums = [2,1,3,4]
# Output: false
# Explanation: There is no sorted array once rotated that can make nums.
# Example 3:

# Input: nums = [1,2,3]
# Output: true
# Explanation: [1,2,3] is the original sorted array.
# You can rotate the array by x = 0 positions (i.e. no rotation) to make nums.

def check_sorted_in_non_decreasing_and_rotate(nums):
    
    count = 0
    
    if len(nums) == 0:
        return None

    if nums[0] < nums[-1]:
        count += 1
        
    for i in range(1, len(nums)):
        if nums[i - 1] > nums[i]:
            count += 1
    
    if count <= 1:
        return True
    
    else:
        return False
    
nums = [3,4,5,1,2]
print(check_sorted_in_non_decreasing_and_rotate(nums))

 