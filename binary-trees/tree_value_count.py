""" 
Write a function, tree_value_count, that takes in the root of a binary tree and 
a target value. The function should return the number of times that the target 
occurs in the tree.

For example:
#      12
#    /   \
#   6     6
#  / \     \
# 4   6     12

count = 3
"""
# Class to define a tree node
class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val 
        self.left = left 
        self.right = right 


def tree_value_count(root, target):
    # Base case that handles if the root in none
    if not root:
        return 0 

    # Defining a queue (list in this case) for FIFO operation
    queue = []
    # Appending root to the queue
    queue.append(root)
    count = 0
    # While size of the queue in greater than zero
    while queue:
        # Pop from the front of the queue.
        current = queue.pop(0)
        # Increment count variable if current node's value is equal to the target
        if current.val == target:
            count += 1 
        # Appending left node to the queue for processing
        if current.left is not None:
            queue.append(current.left)
        # Appending right node to the queue for processing
        if current.right is not None:
            queue.append(current.right)

    return count 
    

a = Node(7)
b = Node(5)
c = Node(1)
d = Node(1)
e = Node(8)
f = Node(7)
g = Node(1)
h = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
f.right = h

#      7
#    /   \
#   5     1
#  / \     \
# 1   8     7
#    /       \
#   1         1

print(tree_value_count(a,  1))