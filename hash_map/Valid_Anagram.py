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
    
    if len(t) != len(s) or len(t) == 0 or len(s) == 0:
       return False
    
    s_count = {}
    t_count = {}
    
    for char in s:
        s_count[char] = s_count.get(char, 0) + 1
    
    for char in t:
        t_count[char] = t_count.get(char, 0) + 1
    
    if s_count == t_count:
        return True
    
    else:
        return False

print(detect_anagram2(s, t))
