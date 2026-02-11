

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
    
    def pop_last(self):
        temp = self.head
        after = self.head
        
        if self.length == 0:
            return None
        
        while temp.next is not None:
            after = temp
            temp = temp.next
            
        self.tail = after
        self.tail.next = None
        self.length -= 1
        
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
        
    def prepend(self, val):
        new_node = Node(val)
        
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        
        if self.length == 0:
            return None
        
        else:
            prev = self.head
            temp = self.head.next
            prev.next = None
            self.head = temp
            self.length -= 1
            
            if self.length == 0:
                self.head = None
                self.tail = None
        return prev
    
    def get(self, index):
        
        if index < 0 or index >= self.length:
            return None
        
        temp = self.head
        for _ in range(index):
            temp = temp.next
            
        return temp
    
    def set_value(self, index, val):
        
        temp = self.get(index)
        if temp:
            temp.value = val
            return True
        return False
    
    def insert_value(self, index, val):
        if index < 0 or index > self.length:
            return False
        
        if index == 0:
            self.prepend(val)
        
        if index == self.length:
            self.append(val)
            
        new_node = Node(val)
        temp = self.get(index - 1)
        
        if temp:
            new_node.next = temp.next
            temp.next = new_node
            self.length += 1
        return None
    
    def detect_cycle(self):
        
        if self.head is None:
            return None
        
        slow = self.head
        fast = self.head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
        return False

my_linked_list = LinkedList(1)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)
my_linked_list.append(6)
print(my_linked_list.detect_cycle())
my_linked_list.insert_value(2, 15)


# print("Pop item is:", my_linked_list.pop_first())
# print("Pop item is:", my_linked_list.pop_first())
# print("Pop item is:", my_linked_list.pop_first())
# print("Removed Node:", my_linked_list.pop())
# my_linked_list.print_list()
# my_linked_list.set_value(2, 10)
my_linked_list.print_list()

