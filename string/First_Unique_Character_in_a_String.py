# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 
# Example 1:

# Input: s = "leetcode"

# Output: 0

# Explanation:

# The character 'l' at index 0 is the first character that does not occur at any other index.

# Example 2:

# Input: s = "loveleetcode"

# Output: 2

# Example 3:

# Input: s = "aabb"

# Output: -1

def find_unique_character(s):
    
    if (len(s)) == 0:
        return None
    
    unique_char = {}
    
    for char in s:
        unique_char[char] = unique_char.get(char, 0) + 1
    
    for index, c in enumerate(s):
        if unique_char.get(c, 0) <= 1:
            return index
        
    return -1
        
    
s = "leetcode"
print(find_unique_character(s))

