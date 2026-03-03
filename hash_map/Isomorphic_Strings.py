# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. 
# No two characters may map to the same character, but a character may map to itself.

# Example 1:

# Input: s = "egg", t = "add"

# Output: true

# Explanation:

# The strings s and t can be made identical by:

# Mapping 'e' to 'a'.
# Mapping 'g' to 'd'.
# Example 2:

# Input: s = "f11", t = "b23"

# Output: false

# Explanation:

# The strings s and t can not be made identical as '1' needs to be mapped to both '2' and '3'.

# Example 3:

# Input: s = "paper", t = "title"

# Output: true

#solution #1
# def isomorphic(s, t):
    
#     map_s = []
#     map_t = []
    
#     for char in s:
#         map_s.append(s.index(char))
    
#     for char in t:
#         map_t.append(t.index(char))
    
#     if map_s == map_t:
#         return True
    
#     else:
#         return False


#solution #2

def isomorphic(s, t):
    map_s = []
    map_t = []
    seen_s = {}
    seen_t = {}
    
    for index, char in enumerate(s):
        if char in seen_s:
            map_s.append(seen_s[char])
        seen_s[char] = index
    
    for index, char in enumerate(t):
        if char in seen_t:
            map_t.append(seen_t[char])
        seen_t[char] = index
        
    if map_s == map_t:
        return True
    else:
        return False

s = "f11"
t = "b23"
print(isomorphic(s, t))
