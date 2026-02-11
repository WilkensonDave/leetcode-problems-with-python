# Given a string s, sort it in decreasing order based on the frequency of the characters. 
# The frequency of a character is the number of times it appears in the string.

# Return the sorted string. If there are multiple answers, return any of them.

 
# Example 1:

# Input: s = "tree"
# Output: "eert"
# Explanation: 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
# Example 2:

# Input: s = "cccaaa"
# Output: "aaaccc"
# Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
# Note that "cacaca" is incorrect, as the same characters must be together.
# Example 3:

# Input: s = "Aabb"
# Output: "bbAa"
# Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
# Note that 'A' and 'a' are treated as two different characters.

def sort_by_characters_by_frequency(s):
    
    if len(s) == 0:
        return None
    
    dict_items = {}
    list_char = []
    
    for char in s:
        dict_items[char] = dict_items.get(char, 0) + 1
    
    sorted_chars = sorted(dict_items, key=dict_items.get, reverse=True)
    
    for char in sorted_chars:
        list_char.append(char * dict_items[char])
    
    return "".join(list_char)

s = "Aabb"
print(sort_by_characters_by_frequency(s))
