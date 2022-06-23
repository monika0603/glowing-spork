""" 
Write a function, flip_tree, that takes in the root of a binary tree. The function 
should flip the binary tree, turning left subtrees into right subtrees and vice-versa. 
This flipping should occur in-place by modifying the original tree. The function should 
return the root of the tree.

#      a
#    /    \
#   b      c
#  / \      \
# d   e      f
#    / \
#    g  h

flip_tree(a) 

#       a
#    /    \
#   c      b
#  /     /   \
# f     e    d
#     /  \
#    h    g
"""
# Class to define a tree node
class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val 
        self.left = left 
        self.right = right 

def flip_tree(root):
    # Base case that handles if the root in none
    if root is None:
        return None 

    # Storing left node in a temp variable
    temp = root.left 
    # Storing right node into left node
    root.left = root.right 
    # Finally swapping right node with the temp variable
    root.right = temp 

    # Recursive call on the left node
    flip_tree(root.left)
    # Recursive call on the right node
    flip_tree(root.right) 

    return root

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")
g = Node("g")
h = Node("h")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
e.right = h

print(flip_tree(a))