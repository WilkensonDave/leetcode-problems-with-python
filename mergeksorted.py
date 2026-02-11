class Node:
    def __init__(self, value):
        self.value = value
        self.next =  None
        
 #sort the arrays one by one
def mergeKList(head1, head2):
    
    dummy = Node(0)
    curr = dummy
    
    while head1 and head2:
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
    
    
class MergeSortedList:
    def mergeLists(self, array):
        res = None
        for node in array:
            res = mergeKList(res, node)
        
        return res

def printList(node):
    while node is not None:
        print(node.value)
        node = node.next


if __name__=="__main__":
    arr = []
    
    node1 = Node(1)
    node1.next = Node(2)
    node1.next.next = Node(3)
    
    arr.append(node1)
    
    node3 = Node(7)
    node3.next = Node(8)
    node3.next.next = Node(9)
    arr.append(node3)
    
    node2 = Node(4)
    node2.next = Node(5)
    node2.next.next = Node(6)
    arr.append(node2)
    
    list = MergeSortedList()
    head = list.mergeLists(arr)
    printList(head)