#CONSTRUCTOR FOR LINKED LIST

"""
#the value in this case will be used in that case to create the first node at
#the time that we initialize the linked list.  
The first thing all of these have in common is that we pass a value to all of these.
"""

"""
What each of the method below does?
1) the init one is going to create a node and it's also going to initialize the new linked list
but it's just going to create a node.

2)The append method is going to create a node and add that node
to the end 

3)The prepend method is going to crate a node and add that node to the beginning

4)The insert method is going to create a node and insert it at whatever index where you want that.

TO SUM UP 
All of these create a new node
so we don't want o write the code for creating a new node each time.
In that case we can create a class that does nothing other than create the nodes for us
so we can give  that class a name
"""


"""
The node is something like this;
{
    "value":4,
    "next":None
}
so the node is going to contain value and next
EXAMPLE OF A CONSTRUCTOR FOR THE NODE

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
"""

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
            # self.new_node = new_item
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1
        return True
    
    def prepend(self, value):
        new_node = Node(value)
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
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.length -= 1
            if self.length == 0:
                self.tail = None
            return temp
                     
    def pop(self):
        ##*****if we have 1 item in the linked-list*******
        # if self.head is None:
        #     return False
        # elif self.length == 1:
        #     self.value = ""
        #     self.next = None
        #********if we have zero item in the linked list*************
        # if self.length == 0:
        #     return None
        #*************if we have 2 or more items in the linked -list********************
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
    
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set_value(self, index, value):
        #*******the first way we can do that*******
        # if index < 0 or index >= self.length:
        #     return None
        # temp = self.head
        # for _ in range(index):
        #     temp = temp.next
        # temp.value = value
        # return temp.value
        #**********the second way we can do that**************
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
        
    def insert_value(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
         
        if index == self.length:
            return self.append(value)
        
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True
        
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
            
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None            
        self.length -= 1
        return temp
        
    def reverse(self):
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
    
    def find_middle(self):
        
        slow = self.head
        fast = self.head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow     
    
    def has_loop(self):
        slow = self.head
        fast = self.head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
            if fast == slow:
                return True
            
        return False
    
    #using nested loops O(n^2)
    def remove_duplicates(self):
        current = self.head
        
        while current is not None:
            runner = current
            while runner.next is not None:
                if runner.next.value == current.value:
                    runner.next = runner.next.next
                    self.length -= 1
                
                else:
                    runner = runner.next
            current = current.next
    
    #with a set o(n)
    def remove_duplicates(self):
        values = set()
        previous = None
        current = self.head
        
        while current:
            if current.value in values:
                previous.next = current.next
                self.length -= 1
            else:
                values.add(current.value) 
                previous = current
            current = current.next        
          
    def print_list(self):
        temp = self.head
        while temp is not None: 
            print(temp.value)
            temp = temp.next
    
     #Binary to Decimal
    def binary_to_decimal(self):
        num = 0
        current = self.head
        
        while current:
            num = num * 2 + current.value
            current = current.next
        return num
    
    def partition_list(self, x):
        
        if self.head == None:
            return None
        
        D1 = Node(0)
        D2 = Node(0)
        
        prev1 = D1
        prev2 = D2
        
        current = self.head
        
        while current:
            if current.value < x:
                prev1.next = current
                prev1 = current
            else:
                prev2.next = current
                prev2 = current
            current = current.next

        prev1.next = D2.next
        prev2.next = None
        self.head = D1.next
    
    def reverse_between(self, start_index, end_index):
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy
        
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
        
        
        
    def swap_nodes_in_pairs(self):
        if self.length == 0 or self.length == 1:
            return None
        
        D1 = Node(0)
        D1.next = self.head
        prev = D1
        first = prev.next
        
        while first and first.next:
            second = first.next
            prev.next = second
            first.next = second.next
            second.next = first
            prev = first
            first = first.next
        self.head = D1.next
            
            
                     
def find_kth_node_from_end(LinkedList, k):
        list = LinkedList
        fast = list.head
        slow = list.head
        
        for _ in range(k):
            
            if fast is None:
                return None
            else:
                fast = fast.next
        
        while fast:   
            slow = slow.next
            fast = fast.next
        
        return  slow

def removed_kth_node_from_end(LinkedList, n):
        
        new_linked_list = LinkedList
        dummy = Node(0)
        dummy.next = new_linked_list.head
        
        slow = dummy
        fast = dummy
        
        for _ in range(n+1):
            if fast is None:
                return None
            fast = fast.next
            
        while fast:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        new_linked_list.head = dummy.next
        return new_linked_list.head

def add_two_numbers(L1, L2):
    dummy = Node(0)
    D1 = dummy
    
    total = remainder = 0
    
    while L1 or L2 or remainder:
        total = remainder
        
        if L1:
            total += L1.value
            L1 = L1.next
        
        if L2:
            total += L2.value
            L2 = L2.next
        
        num = total % 10
        remainder = total // 10
        dummy.next = Node(num)
        dummy = dummy.next
    return D1.next      
    

my_linked_list = LinkedList(1)
my_linked_list.append(6)
my_linked_list.append(4)

LinkedList1 = LinkedList(5)
LinkedList1.append(8)
LinkedList1.append(3)
LinkedList1.append(2)

add_two_numbers(my_linked_list, LinkedList1)

# my_linked_list.reverse()
# print(my_linked_list.find_middle())
# print(my_linked_list.binary_to_decimal())
# my_linked_list.print_list()
# my_linked_list.swap_nodes_in_pairs()
# my_linked_list.partition_list(4)
# my_linked_list.reverse_between(2, 4)

#*************************************************************
# print(my_linked_list.head.value)
# print(my_linked_list.tail.value)
# print(my_linked_list.length)
# print(my_linked_list.pop())
# print(my_linked_list.pop())
# print(my_linked_list.pop())
#**************************************************************


# print(my_linked_list.pop_first())
# print(my_linked_list.pop_first())
# print(my_linked_list.pop_first())
# print(my_linked_list.append(0))
# print(my_linked_list.append(2))
# print(my_linked_list.set_value(1, 1))
# print(my_linked_list.print_list())

# print('nth node from end is: ', find_kth_node_from_end( my_linked_list, 2).value)

removed_kth_node_from_end(my_linked_list, 1)

my_linked_list.print_list()



# Two Sum
# Roman to Integer
# Palindrome Number
# Maximum Subarray
# Remove Element
# Contains Duplicate
# Add Two Numbers
# Majority Element
# Remove Duplicates from Sorted Array


            
        
        

        
            



