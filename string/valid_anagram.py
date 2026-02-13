# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false


#solution #1
# def valid_anagram(s, t):
    
#     for char in set(s):
#         if t.count(char) != s.count(char):
#             return False
    
#     return True

#solution #2

def valid_anagram(s, t):
    
    count_s = {}
    count_t = {}
    
    for char in s:
        count_s[char] = count_s.get(char, 0) + 1
    
    for char in t:
        count_t[char] = count_t.get(char, 0) + 1
    
    if count_t == count_s:
        return True
    return False
    

s = "rat"
t = "car"

print(valid_anagram(s, t))