"Building stack using a linked list"


class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1
    
    def print_stack(self):
        
        if self.top is None:
            return None
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next
    
    def push_to_stack(self, value):
        new_node = Node(value)
        
        if self.height == 0:
            self.top = new_node
            
        else:
            new_node.next = self.top
            self.top = new_node
    
        self.height += 1
    
    def pop_from_stack(self):
        if self.height == 0:
            return None
        
        else:
            temp = self.top
            self.top = self.top.next
            temp.next = None
            self.height -= 1
                
        return temp
    

my_stack = Stack(4)
my_stack.push_to_stack(5)
my_stack.push_to_stack(6)
my_stack.push_to_stack(7)
print("The popped node is", my_stack.pop_from_stack())
my_stack.print_stack()