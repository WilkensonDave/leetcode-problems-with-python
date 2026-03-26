# Given two strings s and t of lengths m and n respectively, 
# return the minimum window substring of s such that every character in t (including duplicates) is included in the window.
# If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

# Example 1:

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
# Example 2:

# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
# Example 3:

# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.

def min_window_substring(s, t):
    if t == "": return ""
    s_dict = {}
    t_dict = {}
    
    res = [-1, -1]
    left = 0
    reslen = float("infinity")
    
    for char in t:
        t_dict[char] = t_dict.get(char, 0) + 1
    
    need, have = len(t_dict), 0
    
    for right in range(len(s)):
        character = s[right]
        s_dict[character] = s_dict.get(character, 0) + 1

        if character in t_dict and s_dict[character] == t_dict[character]:
            have += 1
            
        while have == need:
            if(right -left+1) < reslen:
                res = [left, right]
                reslen = (right-left+1)
            s_dict[s[left]] -= 1
            
            if s[left] in t_dict and s_dict[s[left]] < t_dict[s[left]]:
                have -= 1
            left += 1
    left, right = res
    return s[left:right+1] if reslen != float("infinity") else ""

s = "a"
t = "aa"
print(min_window_substring(s, t))
                
            
        
    