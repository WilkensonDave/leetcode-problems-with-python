# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

# Example 1:

# Input: s = "IceCreAm"

# Output: "AceCreIm"

# Explanation:

# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

# Example 2:

# Input: s = "leetcode"

# Output: "leotcede"


def reverseVowels(s):
    all_vowels = ['a', 'e', 'i', 'o', 'u']
    word = list(s)
    left, right = 0, len(word) -1
    while left < right:
        while left < right and word[left] not in all_vowels:
            left += 1
        
        while left < right and word[right] not in all_vowels:
            right -= 1
        
        
        word[right] in all_vowels and word[left] in all_vowels
        word[left], word[right] = word[right], word[left]
        right -= 1
        left += 1
    
    return "".join(word)
        
s = "wilkenson"
print(reverseVowels(s))