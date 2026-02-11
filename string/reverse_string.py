
s = ["h","e","l","l","o"]

def reverse_string(s):
    left, right = 0, len(s) - 1
    
    while right > left:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -=1
        
    return s

print(reverse_string(s))
