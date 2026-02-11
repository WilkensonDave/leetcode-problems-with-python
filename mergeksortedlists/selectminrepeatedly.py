class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


def getMinNode(arr):
    mini = None
    index = - 1

    for i in range(len(arr)):
        
        if arr[i] is None:
            continue
        
        if mini is None or arr[i].data < mini.data:
            index = i
            mini = arr[i]
            
    if index != -1:
        arr[index] = arr[index].next
    
    return mini
    
    
def mergeKlists(arr):
    
    dummy = Node(0)
    curr = dummy
    
    mini = getMinNode(arr)

    while mini:
        curr.next = mini
        curr = mini
        mini = getMinNode(arr)
    
    return dummy.next


def printList(node):
    
    while node:
        print(node.data)
        node = node.next

if __name__=="__main__":
    arr = [None] * 3
    
    arr[0] = Node(1)
    arr[0].next = Node(3)
    arr[0].next.next = Node(5)
    arr[0].next.next.next = Node(7)
    
    
    arr[1] = Node(2)
    arr[1].next = Node(4)
    arr[1].next.next = Node(6)
    arr[1].next.next.next = Node(8)
    
    
    arr[2] = Node(0)
    arr[2].next = Node(9)
    arr[2].next.next = Node(10)
    arr[2].next.next.next = Node(11)
    
    head = mergeKlists(arr)
    printList(head)

