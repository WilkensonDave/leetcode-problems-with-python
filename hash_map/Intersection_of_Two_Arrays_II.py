# Given two integer arrays nums1 and nums2, return an array of their intersection. 
# Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.


def instersection_of_two_arrayII(n1, n2):
    
    count = {}
    rest = []
    
    for num in n1:
        count[num] = count.get(num, 0) + 1
    
    for num in n2:
        if num in count and count[num] > 0:
            rest.append(num)
            count[num] -= 1
    return rest

nums1 = [1,2,2,1]
nums2 = [2,2]

print(instersection_of_two_arrayII(nums1, nums2))
