# Implement a first in first out (FIFO) queue using only two stacks. 
# The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

# Implement the MyQueue class:

# void push(int x) Pushes element x to the back of the queue.
# int pop() Removes the element from the front of the queue and returns it.
# int peek() Returns the element at the front of the queue.
# boolean empty() Returns true if the queue is empty, false otherwise.
# Notes:

# You must use only standard operations of a stack, which means only push to top, 
# peek/pop from top, size, and is empty operations are valid.
# Depending on your language, the stack may not be supported natively. 
# You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.
 

# Example 1:

# Input
# ["MyQueue", "push", "push", "peek", "pop", "empty"]
# [[], [1], [2], [], [], []]
# Output
# [null, null, null, 1, 1, false]

# Explanation
# MyQueue myQueue = new MyQueue();
# myQueue.push(1); // queue is: [1]
# myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
# myQueue.peek(); // return 1
# myQueue.pop(); // return 1, queue is [2]
# myQueue.empty(); // return false

class Implement_queue_with_stack:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    def queue_with_stack(self, val):
        while self.stack1:
            self.stack2.append(self.stack1.pop())
            
        else:
            self.stack1.append(val)
            while self.stack2:
                self.stack1.append(self.stack2.pop())
        
    def peek(self):
        if len(self.stack1) == 0:
            return None
        return self.stack1[-1]
    
    def pop(self):
        if len(self.stack1) == 0:
            return None
        
        return self.stack1.pop()
    
    def empty(self):
        return len(self.stack1) == 0

my_queue = Implement_queue_with_stack()
my_queue.queue_with_stack(1)
my_queue.queue_with_stack(5)
my_queue.queue_with_stack(8)
my_queue.queue_with_stack(10)
my_queue.queue_with_stack(12)
print(my_queue.peek())
