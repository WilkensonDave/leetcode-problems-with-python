
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
        
        current= self.head
        if self.length <= 0:
            return None
        
        while current is  not None:
            print(current.value)
            current = current.next
    
    
    def append_value(self, value):
        
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def prepend_value(self, value):
        new_node = Node(value)
        if self.head is None or self.length == 0:
            self.head = new_node
            self.tail = new_node
            
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def get_value(self, index):
        if index < 0 or index >= self.length:
            return None
        
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    
    def pop_item(self):
        
        if self.length == 0:
            return None
        
        pre = self.head       
        temp = self.head
        while temp.next is not None:
            pre = temp
            temp = temp.next
        tail = pre
        tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
    
    def pop_first_item(self):
        if self.length ==  0:
            return None
        
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.length -= 1
            if self.length == 0:
                self.tail = None
            return 
    
    def remove_item(self, index):
        if index < 0 or index >= self.length:
            return None
        
        if index == 0:
            return self.pop_first_item()
        
        if index == self.length - 1:
            return self.pop_item()
        
        else:
            prev = self.get_value(index - 1)
            temp = prev.next
            prev.next = temp.next
            temp.next = None
            self.length -= 1
            if self.length == 0:
                self.head = None
                self.tail = None
            return temp
    
    def insert_item(self, index, value):
        new_node = Node(value)
        
        if index < 0 or index > self.length:
            return None
        
        if index == 0:
            return self.prepend_value(value)
        
        if index == self.length:
            return self.append_value(value)
        
        prev = self.get_value(index - 1)
        temp = prev.next
        prev.next = new_node
        new_node.next = temp
        self.length += 1
        return True
            
    
    def set_value(self, index, value):
        curr = self.get_value(index)
        if curr:
            curr.value = value
            return True
        return False
       
    def reverse_list(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
    
    def find_middle_node(self):
        
        curr = self.head
        after = self.head
        
        while after and after.next:
            after = after.next.next
            curr = curr.next
        return curr
    
    
    #to review 
    def reverse_between(self, start_index, end_index):
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy
        
        current = self.head
        if self.length <= 1:
            return None
        
        for _ in range(start_index):
            prev = prev.next
        
        current = prev.next   
        for _ in range(0, end_index - start_index):
            to_move = current.next
            current.next = to_move.next
            to_move.next = prev.next
            prev.next = to_move
        self.head = dummy.next
        dummy.next = None
    
    
    #to review
    def remove_duplicate_with_loops(self):
        current = self.head
        while current is not None:
            after = current
            while after.next is not None:
                if after.next.value == current.value:
                    after.next = after.next.next
                    self.length -= 1
                else:
                    after = after.next
            current = current.next
            
    #to review
    def remove_duplicate_with_set(self):
        values = set()
        previous = None
        current = self.head
        
        while current is not None:
            if current.value in values:
                previous.next = current.next
                self.length -= 1
            else:
                values.add(current.value)
                previous = current
            current = current.next
    
    
    def binary_to_decimal(self):
        current = self.head
        numb = 0
        
        while current:
            numb = numb*2 + current.value
            current = current.next
        return numb
        
        
    
    #to review
    def partition_list(self, x):
        
        Dummy1 = Node(0)
        Dummy2 = Node(0)
        
        prev1 = Dummy1
        prev2 = Dummy2
        
        current = self.head
        
        while current:
            if current.value < x:
                prev1.next = current
                prev1 = current
            
            else:
                prev2.next = current
                prev2 = current
                
            current = current.next
        
        prev1.next = Dummy2.next
        prev2.next = None
        self.head = Dummy1.next
            
    
    #to review
    def swap_nodes_in_pairs(self):
        
        if self.length == 0 or self.length == 1:
            return None
        
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy
        first = prev.next
        
        while first and first.next:
            second = first.next
            prev.next = second
            first.next = second.next
            second.next = first
            
            prev = first
            first = first.next
            
        self.head = dummy.next
            
        
    #to review
    def has_loop(self):
        slow = self.head
        fast = self.head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False 
    
    
    #to review
    def reverseKGroup(self, k):
        
        if k == 1:
            return self.head

        if self.head is None:
            return None
        
        dummy = Node(0)
        dummy.next = self.head
        
        prev = dummy
        current = self.head
        
        count = 0
        
        while current:
            count += 1
            current = current.next
            
        
        while count >= k:
            current = prev.next
            after_current = current.next
            
            #reverse in kth nodes
            for _ in range(1, k):
                current.next = after_current.next
                after_current.next = prev.next
                prev.next = after_current
                
                after_current = current.next
            
            prev = current
            
            count -= k
            
        self.head = dummy.next
        return self.head
        
    
    
#to review 
def find_kth_node_from_end(LinkedList, k):
    list = LinkedList
    
    slow = list.head
    fast = list.head
    
    for _ in range(k):
        if fast is None:
            return None
        else:
            fast = fast.next
    
    while fast:
        fast = fast.next
        slow = slow.next
    
    return slow
    
           
list = LinkedList(1)
list.append_value(2)
list.append_value(3)
list.append_value(4)
list.append_value(5)
list.append_value(6)



# list.remove_duplicate_with_set()
# list.has_loop()
# list.print_list()
# list.swap_nodes_in_pairs()
# print(list.binary_to_decimal())
list.print_list()
print("*********************************")
list.reverseKGroup(3)
# print("The node is: ", find_kth_node_from_end(list, 3))
list.print_list()
              