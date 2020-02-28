from binary_search_tree import BinarySearchTree

test = BinarySearchTree(100)

for i in range(51, 153, 2):
    test.insert(i)

testarr1 = []

testarr2 = []

testarr3 = []


def cb1(x): return testarr1.append(x)


def cb2(x): return testarr2.append(x)


def cb3(x): return testarr3.append(x)


test.for_each_before(cb1)
test.for_each_middle(cb2)
test.for_each_after(cb3)
print(f"For Each Before\n", testarr1)
print(f"For Each Middle\n", testarr2)
print(f"For Each After\n", testarr3)
