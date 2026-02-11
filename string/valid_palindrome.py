# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
# and removing all non-alphanumeric characters, it reads the same forward and backward. 
# Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.

def valid_palindrom(s):
    if len(s) == 0:
        return None
    
    special_char = [char.lower() for char in s if char.isalnum()]
    complete_char = "".join(special_char)
    
    if complete_char == complete_char[::-1]:
        return True
    return False

s = "A man, a plan, a canal: Panama"
s1 = "race a car"
print(valid_palindrom(s1))
