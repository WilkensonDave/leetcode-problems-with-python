# We define the usage of capitals in a word to be right when one of the following cases holds:

# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital, like "Google".
# Given a string word, return true if the usage of capitals in it is right.

 

# Example 1:

# Input: word = "USA"
# Output: true
# Example 2:

# Input: word = "FlaG"
# Output: false

def detect_capital(word):
    
    if word[0].upper() and word[1:].lower():
        return True
    
    if word.lower():
        return True
    
    if word.upper():
        return True
    
    else:
        return False

word = "DAVE"
print(detect_capital(word))