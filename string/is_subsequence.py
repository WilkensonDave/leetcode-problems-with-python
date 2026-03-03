# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original
# string by deleting some (can be none) of the characters without disturbing 
# the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

# Example 1:

# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:

# Input: s = "axc", t = "ahbgdc"
# Output: false
 

def is_subsequence(s, t):
    
    it = iter(t)
    
    for char in s:
        if char not in it:
            return False
    return True

s = "abc"
t = "ahbgdc"
print(is_subsequence(s, t))