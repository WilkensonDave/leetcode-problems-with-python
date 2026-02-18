# Given the head of a linked list and an integer val, remove all the nodes of the 
# linked list that has Node.val == val, and return the new head.

 
# Example 1:

# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]
# Example 2:

# Input: head = [], val = 1
# Output: []
# Example 3:

# Input: head = [7,7,7,7], val = 7
# Output: []

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def append(self, value):
        new_node = Node(value)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def print_list(self):
        temp = self.head
        
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def remove_element(self, val):
        
        if self.head is None:
            return None
        
        dummy = Node(0)
        dummy.next = self.head
        curr = dummy
        
        while curr.next:
            if curr.next.value == val:
                curr.next = curr.next.next
                
            else:
                curr = curr.next
        
        self.head = dummy.next
        return self.head
        
        


my_linked_list = LinkedList(6)
my_linked_list.append(6)
my_linked_list.append(2)
my_linked_list.append(6)
my_linked_list.append(3)
my_linked_list.append(6)
my_linked_list.append(7)
my_linked_list.remove_element(6)
my_linked_list.print_list()