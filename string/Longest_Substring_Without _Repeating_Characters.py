# Given a string s, find the length of the longest substring without duplicate characters.

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

def find_longest_substring(s):
    s_dict = {}
    left = 0
    max_count = 0
    for right, char in enumerate(s):
        s_dict[char] = s_dict.get(char, 0) + 1
       
        while s_dict[char] > 1:
           s_dict[s[left]] -=1
           left += 1
        max_count = max(max_count, right-left+1)
        
    return max_count

s = "bbbbb"
print(find_longest_substring(s))

        
        