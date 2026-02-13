# Given an integer array nums sorted in non-decreasing order, 
# return an array of the squares of each number sorted in non-decreasing order.


# Example 1:

# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
# Example 2:

# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]

def square_of_sorted_array(nums):
    n = len(nums)
    res = [0]*n
    left, right = 0, n-1
    end = n-1
    
    while left <= right:
        
        if abs(nums[left]) > abs(nums[right]):
            res[end] = nums[left]**2
            left += 1
            
        else:
            res[end] = nums[right]**2
            right -= 1
            
        end -= 1
    
    return res

nums = [-4,-1,0,3,10]
print(square_of_sorted_array(nums))