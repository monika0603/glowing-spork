""" 
Write a function, tree_min_value, that takes in the root of a binary tree that contains 
number values. The function should return the minimum value within the tree.

You may assume that the input tree is non-empty.

#       3
#    /    \
#   11     4
#  / \      \
# 4   -2     1
"""

class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val 
        self.left = left 
        self.right = right 

def tree_min_value(root):
    # defining a minimum variable
    minimum = float("inf")
    # base case
    if not root:
        return minimum 

    queue = [root]

    # While queue is not empty
    while queue:
        # poping from the front of the queue
        current = queue.pop(0)
        # checking if we have a minimum value
        minimum = min(minimum, current.val) 
        # Appending left and right nodes to the queue if they are not none
        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)

    return minimum 
# Driver code
a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(-2)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

print(tree_min_value(a))
