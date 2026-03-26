# Given the head of a linked list, return the list after sorting it in ascending order.
#example 1
# Input: head = [4,2,1,3]
# Output: [1,2,3,4]

# example 2 
# Input: head = [-1,5,3,4,0]
# Output: [-1,0,3,4,5]

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

def reorder_list(head):
    if not head or not head.next:
        return head
    
    slow = head
    fast = head
    prev = None
    
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    prev.next = None
    
    left = reorder_list(head)
    right = reorder_list(slow)
    return merge_list(left, right)

def merge_list(l1, l2):
    dummy = Node(0)
    curr = dummy
    while l1 and l2:
        if l1.value < l2.value:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    
    if l2 is not None:
        curr.next = l2
        
    if l1 is not None:
        curr.next = l1
        
    return dummy.next

def print_reordered_list(head):
    while head:
        print(head.value)
        head = head.next


my_linked_list = LinkedList(1)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)
my_linked_list.append(6)


head = [-1,5,3,4,0]
if __name__=="__main__":
    
    list = Node(-1)
    list.next = Node(5)
    list.next.next = Node(3)
    list.next.next.next = Node(4)
    list.next.next.next.next = Node(0)
    my_list = reorder_list(list)
    print_reordered_list(my_list)


        
        