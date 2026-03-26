# Given two strings ransomNote and magazine, 
# return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

# Example 1:

# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:

# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:

# Input: ransomNote = "aa", magazine = "aab"
# Output: true

def check_ransomNote(ransomNote, magazine):
    
    dict_magazine = {}
    
    for char in magazine:
        dict_magazine[char] = dict_magazine.get(char, 0) + 1
    
    
    for c in ransomNote:
        if dict_magazine.get(c, 0) == 0:
            return False
        dict_magazine[c] -= 1
    
    return True
    
ransomNote = "aa"
magazine = "ab"

print(check_ransomNote(ransomNote, magazine))
