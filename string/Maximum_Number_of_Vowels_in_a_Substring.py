
# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.


# Example 1:

# Input: s = "abciiidef", k = 3
# Output: 3
# Explanation: The substring "iii" contains 3 vowel letters.
# Example 2:

# Input: s = "aeiou", k = 2
# Output: 2
# Explanation: Any substring of length 2 contains 2 vowels.
# Example 3:

# Input: s = "leetcode", k = 3
# Output: 2
# Explanation: "lee", "eet" and "ode" contain 2 vowels.

def max_number_vowel_in_substring(s, k):
    count = 0
    all_vowels = ["a", "e", "i", "u", "o"]
    max_count = 0
    
    for i in range(k):
        if s[i] in all_vowels:
            count += 1
    max_count = max(max_count, count)
    
    for j in range(k, len(s)):
        
        if s[j] in all_vowels:
            count += 1
        
        if s[j-k] in all_vowels:
            count -= 1
        max_count = max(max_count, count)
        
    return max_count


s = "leetcode"
k = 3

print(max_number_vowel_in_substring(s, k))
