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
    
    counts = {}
    
    for char in magazine:
        counts[char] = counts.get(char, 0) + 1
    
    for char in ransomNote:
        if counts.get(char, 0) == 0:
            return False
        
        else:
            counts[char] -= 1
            
    return True


ransomNote = "aa"
magazine = "aab"

print(check_ransomNote(ransomNote, magazine))

