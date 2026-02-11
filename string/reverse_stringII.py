# Given a string s, reverse the order of characters in each word within a sentence 
# while still preserving whitespace and initial word order.

# Example 1:

# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
# Example 2:

# Input: s = "Mr Ding"
# Output: "rM gniD"

def reverse_word_character(input):
    
    words = input.split()
    
    for index, word in enumerate(words):
        words[index] = word[::-1]
    
    return " ".join(words)

s = "Let's take LeetCode contest"
print(reverse_word_character(s))

