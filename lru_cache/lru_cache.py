from doubly_linked_list import DoublyLinkedList


class LRUCache:
    """Our LRUCache class keeps track of the max number of nodes it can hold, the current number of nodes it is holding, a doubly-linked list that holds the key-value entries in the correct order, as well as a storage dict that provides fast access to every node stored in the cache."""

    def __init__(self, limit=10):
        self.limit = limit
        self.cache = DoublyLinkedList()
        self.storage = {}
        self.size = self.cache.length

    def get(self, key):
        """Retrieves the value associated with the given key. Also needs to move the key-value pair to the end of the order such that the pair is considered most-recently used. Returns the value associated with the key or None if the key-value pair doesn't exist in the cache."""
        if key in self.storage:
            node = self.storage[key]
            self.cache.move_to_end(node)
            return node.value[1]
        else:
            return None

    def set(self, key, value):
        """Adds the given key-value pair to the cache. The newly- added pair should be considered the most-recently used entry in the cache. If the cache is already at max capacity before this entry is added, then the oldest entry in the cache needs to be removed to make room. Additionally, in the case that the key already exists in the cache, we simply want to overwrite the old value associated with the key with the newly-specified value. """
        if key in self.storage:  # if key exists, just overwrite tuple, and move to end
            node = self.storage[key]
            node.value = (key, value)
            self.cache.move_to_end(node)
        else:   # otherwise we care about the size
            if self.size == self.limit:   # make room by removing old
                self.storage.pop(self.cache.head.value[0])
                self.cache.remove_from_head()    # no need to adjust size, since new gets added
            else:
                self.size += 1
            # create a new node?
            self.cache.add_to_tail((key, value))
            self.storage[key] = self.cache.tail
