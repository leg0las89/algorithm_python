class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

node1 = Node(1)
node2 = Node(2)
singlell = SingleLinkedList()

singlell.head = node1
singlell.head.next = node2
singlell.tail = node2