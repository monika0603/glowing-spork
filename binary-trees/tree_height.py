""" 
Write a function, how_high, that takes in the root of a binary tree. The function 
should return a number representing the height of the tree.

The height of a binary tree is defined as the maximal number of edges from the root 
node to any leaf node.

If the tree is empty, return -1.

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

height = 2
"""
# Class to define a tree node
class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val 
        self.left = left 
        self.right = right 

def how_high(root):
    # Base case that handles if the root in none
    if not root:
        return -1 
    # Getting the height of left sub-tree
    left_value = how_high(root.left)
    # Getting the height of right sub tree
    right_value = how_high(root.right)
    # From the parent node, there is one edge that separetes me from my child 
    # So for that we add 1 to the maximum value of the left and right sub-tree
    return 1 + max(left_value, right_value)

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g

print(how_high(a))