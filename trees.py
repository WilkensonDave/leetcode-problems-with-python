
#A linked list is just a tree that does not fork.

#bellow is a node for a Binary Tree, this is how it will present.

"""
{
    value:4,
    "left": None,
    "right": None   
}
"""

"""In a binary search tree we don't really need the length"""

"""
    We're going to make the assumption when we build this binary search tree
    that we're going to create this with the first node at the time that we build the tree
    and you don't have to do it that way.
    We've done it that way on all of the data structures so far.
    But you could just create this where root is equal to None.
    in case case you create an empty tree, and when you add the first item,
    you add it with the insert method.
    You don't add it at the time that you create the tree or the linked list or
    whatever you're building
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        # self.value = value
        # new_node = Node(value)
        # self.root = new_node
        self.root = None


my_tree = BinarySearchTree()
print(my_tree.root)