# You are given the head of a linked list.

# Remove every node which has a node with a greater value anywhere to the right side of it.

# Return the head of the modified linked list.

# Example 1:

# Input: head = [5,2,13,3,8]
# Output: [13,8]
# Explanation: The nodes that should be removed are 5, 2 and 3.
# - Node 13 is to the right of node 5.
# - Node 13 is to the right of node 2.
# - Node 8 is to the right of node 3.
# Example 2:

# Input: head = [1,1,1,1]
# Output: [1,1,1,1]
# Explanation: Every node has value 1, so no nodes are removed.

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

def remove_nodes_from_linked_list(head):
    
    prev, curr = None, head
    
    while curr:
        curr.next, prev, curr = prev, curr, curr.next
        
    dummy = Node(-1) 
    curr = prev
    temp = dummy
    while curr:
        if curr.value >= temp.value:
            temp.next = curr
            temp = curr
            curr = curr.next
        else:   
            curr = curr.next
    temp.next = None
    
    new_prev = None
    curr = dummy.next
    while curr:
        curr.next, new_prev, curr = new_prev, curr, curr.next
    
    return new_prev

def print_new_list_value(list):
    while list is not None:
        print(list.value)
        list = list.next

mylist = LinkedList(5)
mylist.append(2)
mylist.append(13)
mylist.append(3)
mylist.append(8)


array  = [5,2,13,3,8]
if __name__=="__main__":
    head = Node(5)
    head.next = Node(2)
    head.next.next = Node(13)
    head.next.next.next = Node(3)
    head.next.next.next.next = Node(8)
    new_list = remove_nodes_from_linked_list(head)
    print_new_list_value(new_list)
    