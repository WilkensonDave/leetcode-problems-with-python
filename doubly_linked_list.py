

"""Th node would look like something like this:
{
    "value": 7,
    "next": None,
    "prev": None
}


"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_list(self):
        temp = self.head
        
        while temp:
            print(temp.value)
            temp = temp.next
    
    def append_node(self, value):
        new_node = Node(value)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    
    def pop_node(self):
        
        if self.length == 0:
            return None
        
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
            
        else:
            self.tail = self.tail.prev
            temp.prev = None
            self.tail.next = None
        self.length -= 1
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            
        self.length += 1
        return True
    
    def pop_first(self):
        
        temp = self.head
        if self.length == 0 or self.head is None:
            return None
        
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = temp.next
            self.head.prev = None
            temp.next = None
        self.length -=1
        return temp
    
    #to review
    def get_value(self, index):
        
        
        if index >= self.length or index < 0:
            return None
        
        temp = self.head
        
        if index < self.length / 2:
            
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev

        return temp


    def set_value(self, index, value):
        
        if self.length == 0:
            return None
        
        temp = self.get_value(index)
        
        if temp:
            temp.value = value
            return True
        return False
        
    
    #review
    def insert_value(self, index, value):
        new_node = Node(value)
        
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        
        if index < 0 or index > self.length:
            return False
        
        if  index == 0:
            return self.prepend(value)

        if index == self.length:
            return self.append_node(value)
        
        before = self.get_value(index - 1)
        after = before.next
        
        if before:
            new_node.next = after
            new_node.prev = before
            before.next = new_node
            after.prev = new_node
            self.length += 1
            return True
        return False
        
    
    #to review
    def remove_value(self, index):
        
        if index < 0 or index >= self.length:
            return None
        
        if self.length == 0:
            return None
        
        if index == 0:
            return self.pop_first()
        
        if index == self.length -1:
            return self.pop_node()
    
        temp = self.get_value(index)
        
        if temp:
            temp.next.prev = temp.prev
            temp.prev.next = temp.next
            temp.next = None
            temp.prev = None
            self.length -= 1
            return temp
        return False
    
    def is_palindrome(self):
        
        
        first = self.head
        last = self.tail
        
        for _ in range(self.length // 2):
            if first.value != last.value:
                print("no palindrom")
                return False
                
            first = first.next
            last = last.prev
        print("Super palindrom")
        return True

    def reverse(self):
        
        if not self.head or not self.head.next:
            return False
        
        current = self.head
        before = None
        
        while current:
            before = current.prev
            current.prev = current.next
            current.next = before
            current = current.prev
        
        self.tail, self.head = self.head, self.tail
    
    def partition_doubly_linked_list(self, x):
        
        dummy1 = Node(0)
        dummy2 = Node(0)
        
        D1 = dummy1
        D2 = dummy2
        current = self.head
        
        if self.head is None:
            return None
        
        while current:
            if current.value < x:
                D1.next = current
                current.prev = D1
                D1 = current
            
            else:
                D2.next = current
                current.prev = D2
                D2 = current
            
            current = current.next
        
        D1.next = dummy2.next
        if dummy2.next:
            dummy2.next.prev = D1
            
        dummy2.next = None
        self.head = dummy1.next
        self.head.prev = None
    
    def reverse_between(self, startIndex, endIndex):
        
        if self.length <= 0:
            return None
        
        if startIndex == endIndex:
            return None
        
        dummy = Node(0)
        dummy.next = self.head
        before = dummy
        
        for _ in range(startIndex):
            before = before.next
        

        current = before.next
        
        for _ in range(endIndex - startIndex):
            to_move = current.next
            current.next = to_move.next
            if to_move.next:
                to_move.next.prev = current
            
            to_move.next = before.next
            before.next.prev = to_move
            before.next = to_move
            to_move.prev = before
        self.head = dummy.next
        self.head.prev = None
    
    def swap_pairs(self):
        
        dummy = Node(0)
        dummy.next = self.head
        
        previous = dummy
        
        while self.head and self.head.next:
            first = self.head
            second = self.head.next
            
            previous.next = second
            
            first.next = second.next
            
            second.next = first
            
            first.prev = second
            second.prev = previous
            
            if first.next:
                first.next.prev = first
            
            self.head = first.next
            previous = first
        
        self.head = dummy.next
        if self.head:
            self.head.prev = None
        return self.head
    
    
my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append_node(2)
my_doubly_linked_list.append_node(3)
my_doubly_linked_list.append_node(4)
my_doubly_linked_list.append_node(5)
my_doubly_linked_list.append_node(6)


# print(my_doubly_linked_list.remove_value(1).value, '\n')
# my_doubly_linked_list.reverse()
# my_doubly_linked_list.partition_doubly_linked_list(2)
# my_doubly_linked_list.reverse_between(1, 3)
my_doubly_linked_list.swap_pairs()
my_doubly_linked_list.print_list()

# my_doubly_linked_list.is_palindrome()



