import random
from binary_search_tree import BinarySearchTree

test_bst = BinarySearchTree(1)

for i in range(50):
    value = random.randint(1, 100)
    test_bst.insert(value)

test_bst.in_order_print_recursively(test_bst)
