# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.


# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2

def Subarray_Sum_Equals_K(nums, k):
    prefix_map = {0:1}
    prefix_sum = 0
    count = 0
    
    for n in nums:
        prefix_sum += n
        if prefix_sum - k in prefix_map:
            count += 1
        prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1
    return count
        
        
nums = [1,1,1]
k = 2
print(Subarray_Sum_Equals_K(nums, k))


#brute force solution
def subarray_sum(nums, k):
    count = 0
    
    for i in range(len(nums)):
        curr_sum = 0
        for j in range(i, len(nums)):
            curr_sum += nums[j]
            if curr_sum == k:
                count += 1
    return count

print(subarray_sum(nums, k))