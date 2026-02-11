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
            
            
def merge_two_sorted_list(head1, head2):
    dummy = Node(0)
    curr = dummy
    
    while head1 and head2:
        if head1.value <= head2.value:
            curr.next = head1
            head1 = head1.next

        else:
            curr.next = head2
            head2 = head2.next
            
        curr = curr.next
    
    if head1 is None:
        curr.next = head2
    
    else:
        curr.next = head1
        
    return dummy.next

def print_merge_list(curr):
    while curr is not None:
        print(curr.value)
        curr = curr.next
    
    print()

if __name__=="__main__":
    
    node1 = Node(3)
    node1.next = Node(5)
    node1.next.next = Node(6)
    node1.next.next.next = Node(9)

    node2 = Node(0)
    node2.next = Node(1)
    node2.next.next = Node(2)
    node2.next.next.next = Node(4)

    
    listnode = merge_two_sorted_list(node1, node2)
    print_merge_list(listnode)

