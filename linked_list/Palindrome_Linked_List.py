# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
# Input: head = [1,2,2,1]
# Output: true

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


def palindrom_linked_list(head):
    
    slow, fast, prev = head, head, None
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    prev, slow, prev.next = slow, slow.next, None
    
    while slow:
        slow.next, prev, slow  = prev, slow, slow.next
    
    fast, slow = head, prev
    
    while slow:
        if slow.value != fast.value:
            return False
        slow, fast = slow.next, fast.next
    
    return True
    
my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(2)
my_linked_list.append(1)

if __name__=="__main__":
    linkedList = Node(1)
    linkedList.next = Node(2)
    linkedList.next.next = Node(3)
    linkedList.next.next.next = Node(2)
    linkedList.next.next.next.next = Node(1)
    list = palindrom_linked_list(linkedList)
    print(list)
