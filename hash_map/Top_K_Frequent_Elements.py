# Given an integer array nums and an integer k, 
# return the k most frequent elements. You may return the answer in any order.

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2

# Output: [1,2]

# Example 2:

# Input: nums = [1], k = 1

# Output: [1]

# Example 3:

# Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2

# Output: [1,2]

from collections import Counter
def top_k_frequent_elements(nums, k):
    
    counter = Counter(nums)
    
    frequent = [[] for _ in range(len(nums) + 1)]
    
    for num, c in counter.items():
        frequent[c].append(num)
    
    res = []
    
    for i in range(len(frequent) -1, -1, -1):
        for num in frequent[i]:
            res.append(num)
            
            if len(res) == k:
                return res

nums = [1,1,1,2,2,3, 3, 3, 3] 
k = 2
print(top_k_frequent_elements(nums, k))