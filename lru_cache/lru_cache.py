from doubly_linked_list import DoublyLinkedList


class LRUCache:
    """Our LRUCache class keeps track of the max number of nodes it can hold, the current number of nodes it is holding, a doubly-linked list that holds the key-value entries in the correct order, as well as a storage dict that provides fast access to every node stored in the cache."""

    def __init__(self, limit=10):
        self.limit = limit
        self.list = DoublyLinkedList()
        self.storage = {}
        # why does size not
        self.size = self.list.length

    def get(self, key):
        """Retrieves the value associated with the given key. Also needs to move the key-value pair to the end of the order such that the pair is considered most-recently used. Returns the value associated with the key or None if the key-value pair doesn't exist in the cache."""
        if self.list.head is None:
            return None
        else:
            current = self.list.head

        while current.next is not None and not key == current.value[0]:
            current = current.next

        if key == current.value[0]:
            self.list.move_to_end(current)
        if key in self.storage:
            return self.storage[key]
        else:
            return None

    def set(self, key, value):
        """Adds the given key-value pair to the cache. The newly- added pair should be considered the most-recently used entry in the cache. If the cache is already at max capacity before this entry is added, then the oldest entry in the cache needs to be removed to make room. Additionally, in the case that the key already exists in the cache, we simply want to overwrite the old value associated with the key with the newly-specified value. """
        # overwrite (it already exists)
        if key in self.storage:
            self.storage[key] = value
            # move that node to the tail
            current = self.list.head
            # print(f'current: {current.value}')
            while current.next is not None and not key == current.value[0]:
                # print(f'current: {current.value}')
                current = current.next
            if key == current.value[0]:
                self.list.move_to_end(current)
        # cache is full, delete first and then add it
        elif self.size == self.limit:
            # remove the oldest from storage (head of linked list)
            self.storage.pop(self.list.head.value[0])
            self.list.remove_from_head()
            self.storage[key] = value
            self.list.add_to_tail((key, value))
        # add it
        else:
            self.storage[key] = value
            self.size += 1
            self.list.add_to_tail((key, value))
