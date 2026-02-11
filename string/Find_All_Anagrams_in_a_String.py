# Given two strings s and p, return an array of all the start indices of
# p's anagrams in s. You may return the answer in any order.


# Example 1:

# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# Example 2:

# Input: s = "abab", p = "ab"
# Output: [0,1,2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
from collections import Counter

def find_all_anagram(s, p):
    
    res = []
    k = len(p)
    p_count = Counter(p)
    window = Counter()
    
    for i in range(len(s)):
        
        window[s[i]] += 1
        
        if i >= k:
            left_char = s[i-k]
            window[left_char] -=1
            
            if window[left_char] == 0:
                del window[left_char]
            
        if p_count == window:
            res.append(i-k + 1)
    
    return res

s = "cbaebabacd"  
p = "abc"

print(find_all_anagram(s, p))