# Given a 2D integer array nums where nums[i] is a non-empty array of distinct positive integers, 
# return the list of integers that are present in each array of nums sorted in ascending order.

# Example 1:

# Input: nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
# Output: [3,4]
# Explanation: 
# The only integers present in each of nums[0] = [3,1,2,4,5], nums[1] = [1,2,3,4], 
# and nums[2] = [3,4,5,6] are 3 and 4, so we return [3,4].
# Example 2:

# Input: nums = [[1,2,3],[4,5,6]]
# Output: []
# Explanation: 
# There does not exist any integer present both in nums[0] and nums[1], so we return an empty list [].

def intersection_of_multiple_arrays(nums):
    
    dict = {}
    res = []
    
    for i in range(len(nums)):
        for num in nums[i]:
            dict[num] = dict.get(num, 0) + 1
    
    for k in range(1, 1001):
        if dict.get(k, 0) == len(nums):
            res.append(k)
    return res

nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
print(intersection_of_multiple_arrays(nums))