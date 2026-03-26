
"""Recursion is a function that calls itself until it does not"""

#Example of a recusion with a gift-box

"""The fucntion below will not run it just for pseudo code purposes"""
def open_gift_box(ball):
    #the base will be our base case
    #when using recusion we should have a base case
    #The base case suppose to be True or false at some point depends on the base case
    #In a recusive function we should have a return statement because the print will not break the 
    #recursive function and we will have a stack overflow
    if ball:
        return ball
    
    open_gift_box(ball)

##example
def functionThree():
    print("Three")
    
def functionTwo():
    functionThree()
    print("Two")

def functionOne():
    functionTwo()
    print("One")

# functionOne()

##example of recursion with factorial

def factorial(n):
    if n == 1:
        return 1
    
    return n * factorial(n-1)

print(factorial(5))

#call stack
["5!", "4!", "3!", "2!", "1!"]

#the operation
"1! = 1"
"2! => 2!*1! => 2*1 => 2"
"3! => 3!*2! => 3*2 => 6"
"4! => 4!*3! => 4*6 => 24"
"5! => 5!*4! => 5*24 => 120"



