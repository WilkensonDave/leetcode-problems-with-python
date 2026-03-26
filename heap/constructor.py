
"""A head looks very simialr to a binary search tree"""
"""A head is a binary seach tree, the only difference is the fact that the numbers in the BST
are not distributed in the same way with head"""

"""With a head each node has a number that is higher than all of its descendants
which means the highest value will always be at the top"""

"""A head is a complete binary search tree and when it's a perfect tree, its height is logn """

"""One of the things that make a head different from a head is the fact that you can have 
duplicate in the head"""

"""We can have a max head with the max value at the top and a min head with the min value at the top"""

"""heap are not good for searching."""

"""The only thing you can use a head for is being able to keep track of a largest item at the top
and be able to quickly remove it"""

"""There's a huge difference in how we store this tree versus how we stored our binary search tree"""

"""We are going to store this tree in a list, and we will not be creating a node class"""

"""The only thing the list will store is integers"""

"""There are two commons ways of storing the  head in a list"""

#The first way is to store the first item at the index of zero

"""From the perspective of storing the head in a list, the head supposed to be a complete tree
In order to avoid any cap in the list"""
#All the values in the list will be a contiguous range of numbers

#Good to know
"""If we want to find the children of the root starting from the left child
the equation will be the following; left_child = 2 * parent_index
[,99,72, 61, 58, 55, 27, 18]
the index zero(0) does not have any number in this situation
###
If we want to find the children of te root starting from the right child,
the equation will be the following; right = 2 * parent_index + 1
"""

#Good to know
#the list start at index 1
"""The equation for finding the parent of a particular node is the following;
The index of the child node // 2  
"""

#Insert a value into a head
"""To insert a node into a head, we will always start out by inserting the value into the next open space
the reason for this is because the tree needs to remain complete.
##############################################
We need to bubble up the value to be inserted to the appropriate spot
we will start out by comparing it to its parent, let say we want to insert 100
and its parent is 72, since 100 is greater than 72 we're going to swap these, 
once we do that we will compare it again to its parent again i mean up to the root.
let say its parent now is 99 since 100 is greater than 99, we will swap it again.
#################################################
We will move that new value to be inserted using a while loop and there are 
two conditionals that can break us out of the while loop.
1) The first one is, if we reach the top of the head,
once we reach the top, we want to stop running the while
loop and then we'll have a valid head

###There's another conditional that can break us out of a while loop as well
2)if the value to be inserted is less than its parent we will break out of the loop
"""

#insert or remove in a head is always going to be O(log n)
class MaxHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        #now the list start at zero, the first index is zero
        return 2 * index + 1
    
    def _right_child(self, index):
        return 2 * index + 2
    
    def _parent(self, index):
        #the list start at index zero
        return (index -1) // 2
    
    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]
    
    
    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1
        
        while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)
    
    def _sink_down(self, index):
        max_index = index
        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)
            
            if(left_index < len(self.heap) and self.heap[left_index] > self.heap[max_index]):
                    max_index = left_index
                
            if (right_index < len(self.heap)) and self.heap[right_index] > self.heap[max_index]:
                max_index = right_index
            
            if max_index != index:
                self._swap(index, max_index)
                index = max_index
                
            else:
                return
            
    def remove(self):
        if len(self.heap) == 0:
            return None
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)
        return max_value
    
myheap = MaxHeap()
myheap.insert(95)
myheap.insert(75)
myheap.insert(80)
myheap.insert(55)
myheap.insert(60)
myheap.insert(50)
myheap.insert(65)
print(myheap.heap)
myheap.remove()
print(myheap.heap)
myheap.remove()
print(myheap.heap)
# print(myheap.heap)
# myheap.insert(100)
# print(myheap.heap)
# myheap.insert(75)
# print(myheap.heap)
