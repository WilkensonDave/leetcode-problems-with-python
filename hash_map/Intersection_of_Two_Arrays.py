# Given two integer arrays nums1 and nums2, return an array of their intersection. 
# Each element in the result must be unique and you may return the result in any order.

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Explanation: [4,9] is also accepted.

def instersection_of_two_arrays(n1, n2):
    
    res = []
    dict_1 = {}
    dict_2 = {}
    
    for num in n1:
        dict_1[num] = dict_1.get(num, 0) + 1
    
    for num in n2:
        dict_2[num] = dict_2.get(num, 0) + 1
    
    for num in dict_1:
        if dict_2.get(num, 0) >= 1:
            res.append(num)
            
    return res

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(instersection_of_two_arrays(nums1, nums2))