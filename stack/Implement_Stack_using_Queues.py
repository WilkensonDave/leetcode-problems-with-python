# Implement a last-in-first-out (LIFO) stack using only two queues. 
# The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

# Implement the MyStack class:

# void push(int x) Pushes element x to the top of the stack.
# int pop() Removes the element on the top of the stack and returns it.
# int top() Returns the element on the top of the stack.
# boolean empty() Returns true if the stack is empty, false otherwise.
# Notes:

# You must use only standard operations of a queue, which means that only push to back, 
# peek/pop from front, size and is empty operations are valid.
# Depending on your language, the queue may not be supported natively. 
# You may simulate a queue using a list or deque (double-ended queue) 
# as long as you use only a queue's standard operations.
 
# Example 1:

# Input
# ["MyStack", "push", "push", "top", "pop", "empty"]
# [[], [1], [2], [], [], []]
# Output
# [null, null, null, 2, 2, false]

# Explanation
# MyStack myStack = new MyStack();
# myStack.push(1);
# myStack.push(2);
# myStack.top(); // return 2
# myStack.pop(); // return 2
# myStack.empty(); // return False

from collections import deque

#method 1
class implement_stack_with_queu:
    def __init__(self):
        self.q1 = deque()
    
    def push(self, val):
        self.q1.append(val)
        for _ in range(len(self.q1)-1):
            self.q1.append(self.q1.popleft())
        return self.q1
        
    def pop(self):
        return self.q1.popleft()
    
    def top(self):
        return self.q1[0]
    
    def empty(self):
        return len(self.q1) == 0

#method 2
class implement_stack_with_queu_second:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        
    def push(self, val):
        self.q1.append(val)
        
    def pop(self):
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        
        popped = self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1
        return popped
    
    def empty(self):
        return len(self.q1) == 0
    
    def top(self):
        
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        
        top = self.q1[-1]
        self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1
        return top
    
myStack = implement_stack_with_queu_second()
print(myStack.push(1))
print(myStack.push(2))
print(myStack.top())
print(myStack.pop())
myStack.empty()

