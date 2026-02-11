# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false

#SOLUTION 1
def detect_anagram(s, t):
    if len(s) != len(t):
        return False

    for char in set(s):
        if t.count(char) != s.count(char):
            return False
    return True

s = "anagram"
t = "nagaram"
print(detect_anagram(s, t))

s = "anagram"
t = "nagaram"

#SOLUTION 2
def detect_anagram2(s, t):
    
    if len(s) != len(t):
        return None
    
    s_dict = {}
    t_dict  ={}
    
    for char in s:
        s_dict[char] = s_dict.get(char, 0) + 1
    
    for char in t:
        t_dict[char] = t_dict.get(char, 0) + 1
    
    if s_dict == t_dict:
        return True
    
    else:
        return False

print(detect_anagram2(s, t))
