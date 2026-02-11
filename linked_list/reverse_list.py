
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
        if self.head is None:
            return None
        
        else:
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
    
    def reverseList(self):
        
        if self.head is None:
            return None
        
        prev = None
        temp = self.head
        
        while temp is not None:
            after = temp.next
            temp.next = prev
            prev = temp
            temp = after
        self.head = prev
        return self.head
        
        
my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.print_list()
my_linked_list.reverseList()
my_linked_list.print_list()


    
    


    
        