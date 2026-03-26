# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

# Input: head = [1,2,3,4]
# Output: [1,4,2,3]

# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]

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

    def reorder_list(self):
        
        if self.head is None:
            return None
        
        slow =self.head
        fast = self.head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second_half = slow.next
        slow.next = None
        new_head = None

        while second_half:
            last = second_half.next
            second_half.next = new_head
            new_head = second_half
            second_half = last
        
        first = self.head
        second_half = new_head
        
        while first and second_half:
            temp1 = first.next
            temp2 = second_half.next
            first.next, second_half.next = second_half, temp1
            first, second_half = temp1, temp2

mylist = LinkedList(1)
mylist.append(2)
mylist.append(3)
mylist.append(4)
mylist.append(5)
mylist.reorder_list()
mylist.print_list()
        