# Given the head of a linked list, rotate the list to the right by k places.
#example 1
# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]

#example 2
# Input: head = [0,1,2], k = 4
# Output: [2,0,1]

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

def rotate_list(head, k):
    if head is None:
        return head

    curr = head
    length = 1
    while curr.next:
        curr = curr.next
        length += 1
    
    k = k%length
    
    if k == 0:
        return head
    
    temp=head
    for _ in range(length-k-1):
        temp = temp.next
    new_head = temp.next
    temp.next = None
    curr.next = head
    return new_head

def print_new_head_list(new_head):
    while new_head:
        print(new_head.value)
        new_head = new_head.next

mylist = LinkedList(1)
mylist.append(2)
mylist.append(3)
mylist.append(4)



head = [1,2,3,4,5]
k = 2


if __name__=="__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    
    new_head = rotate_list(head, k)
    print_new_head_list(new_head)
    
    print("**********************************")
    k = 4
    another_head = Node(0)
    another_head.next = Node(1)
    another_head.next.next = Node(2)
    new = rotate_list(another_head, k)
    print_new_head_list(new)