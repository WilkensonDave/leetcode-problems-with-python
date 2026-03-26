# First: What are we really doing?

# We are treating the array like a linked list:

# nums = [1, 3, 4, 2, 2]

# index:  0  1  2  3  4
# value:  1  3  4  2  2

# Think:

# 0 → 1 → 3 → 2 → 4 → 2 → 4 → 2 ...

# 👉 See it?
# There is a cycle at 2

# 🐢🐇 First while loop (WHY it exists)
# while True:
#     slow = nums[slow]
#     fast = nums[nums[fast]]
#     if slow == fast:
#         break
# ❓ What is this doing?

# It’s answering:

# “Is there a cycle?”

# slow moves 1 step

# fast moves 2 steps

# 👉 If there is a cycle → they MUST meet inside it

# 💡 Why they meet

# Inside a cycle:

# Fast is “chasing” slow

# Since fast is faster → it will eventually catch slow

# 👉 This guarantees:

# They meet somewhere in the cycle, not necessarily at the duplicate

# ⚠️ Important

# After this loop:

# You are inside the cycle

# But you DON’T know where the cycle starts yet

# 🔁 Second while loop (WHY we need it)
# slow = nums[0]

# while slow != fast:
#     slow = nums[slow]
#     fast = nums[fast]

# This is the part that confuses everyone.

# ❓ Why reset slow = nums[0]?

# Because:

# 👉 We want to find the start of the cycle (the duplicate)

# Right now:

# fast is somewhere inside the cycle

# slow is also inside the cycle

# We need:

# One pointer at the start

# One pointer inside the cycle

############################################################################################################
# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem without modifying the array nums and using only constant extra space.


# Example 1:

# Input: nums = [1,3,4,2,2]
# Output: 2
# Example 2:

# Input: nums = [3,1,3,4,2]
# Output: 3
# Example 3:

# Input: nums = [3,3,3,3,3]
# Output: 3

def find_diplicate_number(nums):
    
    slow = nums[0]
    fast = nums[0]
    
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        
        if slow == fast:
            break
    
    slow = nums[0]
    
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
        
    return slow

nums = [3,1,3,4,2]
print(find_diplicate_number(nums))

