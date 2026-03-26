# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between
# a letter in pattern and a non-empty word in s. Specifically:

# Each letter in pattern maps to exactly one unique word in s.
# Each unique word in s maps to exactly one letter in pattern.
# No two letters map to the same word, and no two words map to the same letter.
 
 
# Example 1:

# Input: pattern = "abba", s = "dog cat cat dog"

# Output: true

# Explanation:

# The bijection can be established as:

# 'a' maps to "dog".
# 'b' maps to "cat".
# Example 2:

# Input: pattern = "abba", s = "dog cat cat fish"

# Output: false

# Example 3:

# Input: pattern = "aaaa", s = "dog cat cat dog"

# Output: false

def word_pattern(pattern, s):
    words = s.split()
    
    word_dict = {}
    char_dict = {}
    
    for letter, word in zip(pattern, words):
        if letter in char_dict:
            if char_dict[letter] != word:
                return False
        else:
            char_dict[letter] = word
        
        
        if word in word_dict:
            if word_dict[word] != letter:
                return False
        
        else:
            word_dict[word] = letter
    
    return True
    
    
pattern = "abba"
s = "dog cat cat dog"
print(word_pattern(pattern, s))