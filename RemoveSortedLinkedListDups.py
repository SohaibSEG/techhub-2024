class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
        

def removeDups(head):
    if head is None:
        return head
    current = head
    while current.next is not None:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next
    return head

def printList(head):
    current = head
    while current is not None:
        print(current.data, end = ' ')
        current = current.next
    print()
    
head = Node(1)
head.next = Node(1)
head.next.next = Node(2)
head.next.next.next = Node(3)
head.next.next.next.next = Node(3)

printList(head)

removeDups(head)

printList(head)