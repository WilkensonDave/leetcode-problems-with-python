# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.
# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.


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
    
    def print_list(self):
        temp = self.head
        
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
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

    def find_middle_node(self):
        if self.head is None:
            return None
        
        curr = self.head
        fast = self.head
        
        while fast and fast.next:
            curr = curr.next
            fast = fast.next.next
        
        return curr.value
        
my_linked_list = LinkedList(1)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)
my_linked_list.append(6)
my_linked_list.append(9)
print(my_linked_list.find_middle_node())