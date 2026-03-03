# Given the head of a sorted linked list, delete all nodes that have duplicate numbers, 
# leaving only distinct numbers from the original list. 
# Return the linked list sorted as well.
# Input: head = [1,2,3,3,4,4,5]
# Output: [1,2,5]


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
    
    def remove_duplicate(self):
        
        dummy = Node(0)
        dummy.next = self.head
        curr = dummy
        temp = self.head
        
        while temp and temp.next:
            if temp.value == temp.next.value:
                while temp.value and temp.next == temp.next.value:
                    temp = temp.next
                curr.next = temp.next
                
            else:
                curr = curr.next
            temp = temp.next
            
        return curr.next


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(4)
my_linked_list.append(5)
my_linked_list.remove_duplicate()
my_linked_list.print_list()