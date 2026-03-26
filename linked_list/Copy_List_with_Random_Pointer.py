# A linked list of length n is given such that each node contains an additional random pointer, 
# which could point to any node in the list, or null.

# Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, 
# where each new node has its value set to the value of its corresponding original node. 
# Both the next and random pointer of the new nodes should point to new nodes in the copied
# list such that the pointers in the original list and copied list represent the same list state. 
# None of the pointers in the new list should point to nodes in the original list.

# For example, if there are two nodes X and Y in the original list, 
# where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

# Return the head of the copied linked list.

# The linked list is represented in the input/output as a list of n nodes. 
# Each node is represented as a pair of [val, random_index] where:

# val: an integer representing Node.val
# random_index: the index of the node (range from 0 to n-1) that the random pointer points to, 
# or null if it does not point to any node.
# Your code will only be given the head of the original linked list.

# Example 1:

# Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Example 2:

# Input: head = [[1,1],[2,1]]
# Output: [[1,1],[2,1]]
# Example 3:

# Input: head = [[3,null],[3,0],[3,null]]
# Output: [[3,null],[3,0],[3,null]]

class Node:
    def __init__(self, val, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

def build_linked_list(arr):
    if not arr:
        return None
    
    # Step 1: create all nodes
    nodes = [Node(val) for val, _ in arr]

    # Step 2: connect next and random
    for i, (_, random_index) in enumerate(arr):
        # next pointer
        if i < len(nodes) - 1:
            nodes[i].next = nodes[i + 1]

        # random pointer
        if random_index is not None:
            nodes[i].random = nodes[random_index]

    return nodes[0]  # head

def print_list(head):
    nodes = []
    current = head

    # collect nodes in order
    while current:
        nodes.append(current)
        current = current.next

    # print structure
    for i, node in enumerate(nodes):
        random_index = nodes.index(node.random) if node.random else None
        print(f"[{node.val}, {random_index}]")


def copy_list_with_random_pointer(head):
    map_list = {None:None}
    curr = head
    while curr:
        copy = Node(curr.val)
        map_list[curr] = copy
        curr = curr.next
    
    curr = head
    while curr:
        copy = map_list[curr]
        copy.next = map_list[curr.next]
        copy.random = map_list[curr.random]
        curr = curr.next
    return map_list[head]
    

# Input representation
head_data = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]

# Build the linked list
head = build_linked_list(head_data)
list = copy_list_with_random_pointer(head)
print_list(list)


