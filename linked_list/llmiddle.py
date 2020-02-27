class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def add(self, value):
        self.next = Node(value)


def find_middle(node):
    print(f"starting at {node.value}")
    hare = node
    tortoise = node
    while hare is not None and hare.next is not None:
        print(hare.value)
        hare = hare.next.next
        print(hare.value)
        tortoise = tortoise.next
    return tortoise


node1 = Node(1)
i = 0
current = node1
while i < 50:
    current.add(i)
    current = current.next
    i += 1

print(f"the middle is: {find_middle(node1).value}")
