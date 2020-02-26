# reverse LL
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def add(self, value):
        self.next = Node(value)

    def __str__(self):
        s = ''
        current = self
        while current is not None:
            s += str(current.value) + ' '
            current = current.next
        return s

    def reverse_list(self):
        current = self
        new = self.next
        self.next = None
        # cursor two is traveling ahead, starts at node.next
        while new is not None:
            prev = current
            current = new
            new = current.next
            current.next = prev

        return current


node_one = Node(1)
i = 2
current = node_one
# create a new node with 49 other nodes attached to it  in a list
while i < 50:
    current.add(i)
    current = current.next
    i += 1

print(node_one)
node_one = node_one.reverse_list()
print(node_one)
