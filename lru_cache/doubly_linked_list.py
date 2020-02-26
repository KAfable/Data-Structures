
class ListNode:
    def __init__(self, value, prev=None, next=None):
        """Node takes in a value, and optional pointers to the previous and next node."""
        self.value = value
        self.prev = prev
        self.next = next

    def insert_after(self, value):
        """Inserts a ListNode with the given value after the provided Node."""
        # create the new node with the correct pointers
        new_node = ListNode(value, self, self.next)
        # if the next node exists (edge case for when DLL size is 1)
        if self.next:
            # adjust the next node's backwards direction
            self.next.prev = new_node
        # adjust current node pointers to point to the new node
        self.next = new_node

    def insert_before(self, value):
        """Inserts a ListNode with the given value before the provided Node."""
        new_node = ListNode(value, self.prev, self)
        # if the prev node exists (edge case for when DLL size is 1)
        if self.prev:
            # set the OLD previous node's next pointer to the new node
            self.prev.next = new_node
            # sets the current node's prev pointer to new node
        self.prev = new_node

    def delete(self):
        """Removes the node from the linked list by adjusting pointers. Effectively deletes Node but doesn't really delete it from memory."""
        # important to note that a node cannot delete itself
        # the special edge case of when a node is the only thing in the list is reserved for the list, because a node itself doesn't have knowledge
        # it's almost a better idea to just rename this to 'remove' instead
        # a node has no control over a list, so it cannot remove itself, the list has to
        if self.next:
            self.next.prev = self.prev
        if self.prev:
            self.prev.next = self.next


class DoublyLinkedList:
    """Our doubly-linked list class. It holds references to the list's head and tail nodes."""

    def __init__(self, initial=None):
        self.head = self.tail = initial
        self.length = 0 if initial is None else 1

    def __len__(self):
        return self.length

    def __str__(self):
        s = ''
        current = self.head
        while current is not None:
            s += str(current.value) + ' '
            current = current.next
        return s

    def add_to_head(self, value):
        # important that this is 'and' because for a brief period in add_to_head, either head/tail can be None
        if self.head is None and self.tail is None:
            self.head = self.tail = ListNode(value)
        else:
            self.head.insert_before(value)
            self.head = self.head.prev
        self.length += 1

    def remove_from_head(self):
        """Removes current head of list and sets the new head to the appropriate node, if any."""
        value = self.head.value
        self.delete(self.head)
        return value

    def add_to_tail(self, value):
        """Adds a new node with the given value after the tail"""
        if self.length == 0:
            self.head = self.tail = ListNode(value)
        else:
            self.tail.insert_after(value)
            self.tail = self.tail.next
        self.length += 1

    def remove_from_tail(self):
        """Removes the tail node, makes the previous node the new tail and returns the removed value. DLL's"""
        value = self.tail.value
        # DLL's delete method already accounts for re-assigning new tails.
        self.delete(self.tail)
        return value

    def move_to_front(self, node):
        value = node.value
        self.delete(node)
        self.add_to_head(value)

    def move_to_end(self, node):
        value = node.value
        self.delete(node)
        self.add_to_tail(value)

    def delete(self, node):
        """Deletes current node from the list."""
        # if there is only one node in the list
        if self.length == 1:
            # manually set the headl/tail to none
            self.head = self.tail = None
        elif self.length == 0:
            print("ERROR: Trying to delete from an empty list.")
            return
        elif node == self.head:
            # node's delete method has no knowledge of what's the head of the DLL
            self.head = self.head.next
            node.delete()
        elif node == self.tail:
            # node's delete method has no knowledge of what's the tail of the DLL
            self.tail = self.head.prev
            node.delete()
        else:
            node.delete()

        self.length -= 1

    def get_max(self):
        current = self.head
        highest = self.head.value
        while current is not None:
            if highest < current.value:
                highest = current.value
            current = current.next
        return highest
