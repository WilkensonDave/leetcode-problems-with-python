
my_arr = [0, -1, 2, -3, 1]
target = -2

#brute force solution 1

for i in range(len(my_arr)):
    for j in range(i+1, len(my_arr)):
        if my_arr[i] + my_arr[j] == target:
            print([i, j])

#BEST case and best solution process
def twoSum():
    seen = {}
    for index, num in enumerate(my_arr):
        complement = target - num
        if complement in seen:
            return [seen[complement], index]
        
        seen[num] = index

# print(twoSum())

#*************************************************************************************
# Given an integer array nums and an integer k, return true if there are two distinct
# indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
# Example 1:

# Input: nums = [1,2,3,1], k = 3
# Output: true
# Example 2:

# Input: nums = [1,0,1,1], k = 1
# Output: true

def twoDictinct():
    nums = [1,2,3,1,2,3]
    k = 2
    seen = {}
    
    for index, num in enumerate(nums):
        if num in seen and abs(seen[num] - index) <= k:
            return True
        seen[num] = index
    return False

print(twoDictinct())
#*************************************************************************************