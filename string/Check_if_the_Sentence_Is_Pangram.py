# A pangram is a sentence where every letter of the English alphabet appears at least once.

# Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

 
# Example 1:

# Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
# Output: true
# Explanation: sentence contains at least one of every letter of the English alphabet.
# Example 2:

# Input: sentence = "leetcode"
# Output: false

def check_pangram(sentence):
    
    count = {}
    all_alphabets = "abcdefghijklmnopqrstuvwxyz"

    for char in sentence:
        count[char] = count.get(char, 0) + 1
    
    for char in all_alphabets:
        if count.get(char, 0) == 0:
            return False
    return True


sentence = "leetcode"
print(check_pangram(sentence))