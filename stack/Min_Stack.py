# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.


# Example 1:

# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]

# Output
# [null,null,null,null,-3,null,0,-2]

# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2

class MinStack:
    def __init__(self):
        self.stack = []
    
    
    def push(self, val):
        minVal = self.get_minStack()
        
        if minVal is None or minVal >= val:
            minVal = val
        self.stack.append((val, minVal))
        
    def pop(self):
        return self.stack.pop()[0]
    
    def peek(self):
        return self.stack[-1][0]
    
    def empty(self):
        return len(self.stack) == 0
    
    def get_minStack(self):
        if len(self.stack) == 0:
            return None
        return self.stack[-1][1]
    
minStack = MinStack()
minStack.push(-6)
minStack.push(-2)
minStack.push(0)
minStack.push(3)


print(minStack.peek())
print(minStack.get_minStack())