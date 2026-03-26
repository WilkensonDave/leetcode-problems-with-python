# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

# Example 1:

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:

# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false

def Permutation_in_String(s1, s2):
    if len(s1) > len(s2): return False
    
    s1_count = {}
    window = {}
    left = 0
    
    for char in s1:
        s1_count[char] = s1_count.get(char, 0) + 1
    
    for right in range(len(s2)):
        char = s2[right]
        window[char] = window.get(char, 0) +1 
        
        if right - left + 1 > len(s1):
            window[s2[left]] -= 1
            
            if window[s2[left]] == 0:
                del window[s2[left]]
            
            left += 1
            
        if s1_count == window:
            return True
    return False
        
        
    

s1 = "ab"
s2 = "eidbaooo"
print(Permutation_in_String(s1, s2))

