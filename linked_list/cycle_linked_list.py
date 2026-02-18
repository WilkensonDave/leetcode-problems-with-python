# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be reached
# again by continuously following the next pointer. Internally, pos is used to denote
# the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.

# Example 1:

# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).


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
    
    def create_cycle(self, pos):
        
        if pos == -1:
            return
        
        cycle_node = None
        curr = self.head
        index = 0
        
        while curr.next:
            if index == pos:
                cycle_node = curr
            curr = curr.next
            index +=1
        curr.next = cycle_node
        
        
    def detect_cycle(self):
        
        slow = self.head
        fast = self.head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
            
        return False

        
if __name__=="__main__":
    my_linked_list = LinkedList(3)
    for v in ([2,0,-4]):
        my_linked_list.append(v)
        
    my_linked_list.create_cycle(1)
    print(my_linked_list.detect_cycle())