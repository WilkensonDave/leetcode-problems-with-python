# Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.

# Example 1:
# Input: s = "Hello"
# Output: "hello"
# Example 2:

# Input: s = "here"
# Output: "here"
# Example 3:

# Input: s = "LOVELY"
# Output: "lovely"

def to_lower_string(s):
    if len(s) == 0:
        return None
    
    lower_letters = [char.lower() for char in s]
    return "".join(lower_letters)

s = "Hello"
print(to_lower_string(s))