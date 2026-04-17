# Given an array of integers nums and a target integer target, write a Python function called subarray_sum
# that finds the indices of a contiguous subarray in nums that add up to the target sum using a hash table (dictionary).

# Your function should take two arguments:

# nums: a list of integers representing the input array

# target: an integer representing the target sum


# Your function should return a list of two integers representing the starting and ending indices of the subarray
# that adds up to the target sum. If there is no such subarray, your function should return an empty list.

# For example:
# nums = [1, 2, 3, 4, 5]
# target = 9
# print(subarray_sum(nums, target))  # should print [1, 3]

# example 2
# nums = [-1, 2, 3, -4, 5]
# target = 0

# example 3
# nums = [2, 3, 4, 5, 6]
# target = 3

# example 4
# nums = []
# target = 0


def subarray_sum(nums, target):
    dict = {0:-1}
    curr_sum = 0
    for index, num in enumerate(nums):
        curr_sum += num
        
        if curr_sum - target in dict:
            curr_index = curr_sum - target
            return [dict[curr_index] + 1, index]

        else:
            dict[curr_sum] = index
    return []

nums = [2, 3, 4, 5, 6]
target = 3
print(subarray_sum(nums, target))
