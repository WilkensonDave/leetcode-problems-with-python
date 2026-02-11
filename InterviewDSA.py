
# DSA Interview Questions on Linked List

#**********Reverse a Linked List**********

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
            self.head  = new_node
            self.tail = new_node
        
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def pop_last(self):
        if self.head is None:
            return None
        
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
            return temp
        
        prev = self.head
        while temp.next:
            prev = temp
            temp = temp.next
            
        prev.next = None
        self.tail = prev
        self.length -= 1
        return temp
    
    def reverse_list(self):
        
        temp = self.head
        self.head = self.tail 
        self.tail = temp
        before = None
        
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        return self.head
    
    
    def has_loop(self):
        
        fast = self.head
        slow = self.head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
            if fast == slow:
                return True
        return False
            
    def print_list(self):
        if self.head is None:
            return None
        
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

list = LinkedList(1)
# list.append(2)
# list.append(3)
# list.append(6)
# list.append(4)
# list.append(5)
# list.append(6)
# list.has_loop()
# list.reverse_list()
# # list.pop_last()
# list.print_list()

#merge two sorted Linked list
def merge_two_sorted_list(head1, head2):
    
    #using a pointer
    dummy = Node(0)
    curr = dummy
    
    while head1  and  head2:
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
            
    
def printList(curr):
    
    while curr is not None:
        print(curr.value)
        curr = curr.next
    print()
    
    
if __name__ == "__main__":
    
    head1 = Node(1)
    head1.next = Node(3)
    head1.next.next = Node(5)


    head2 = Node(7)
    head2.next = Node(9)
    head2.next.next = Node(11)

    list_node = merge_two_sorted_list(head2, head1)
    printList(list_node)