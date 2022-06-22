""" 
Given a tree below, print the values of all the nodes in an anti-clockwise direction. 
#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
"""
# Class to define a tree node
class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val 
        self.left = left 
        self.right = right

def print_left_boundary(node):
    # Base case that handles if the root in none
    # Making sure we return a consistent data type for return, so we simply return
    if node is None:
        return 

    print(node.val) 
    # Only calling the recursive call stack for the left node
    print_left_boundary(node.left)

def print_right_boundary(node):
    # Base case that handles if the root in none
    # Making sure we return a consistent data type for return, so we simply return
    if node is None:
        return 
    # Only calling the recursive call stack for the left node
    print_right_boundary(node.right)
    print(node.val) 

def print_leaf_nodes(node):
    # Base case that handles if the root in none
    # Making sure we return a consistent data type for return, so we simply return
    if node is None:
        return 
    # Recursive call stack if both left and right nodes are null
    if node.left is None and node.right is None:
        print(node.val)
    print_leaf_nodes(node.left)
    print_leaf_nodes(node.right)

# Driver code

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
print(print_left_boundary(a))
print(print_right_boundary(a))
print_leaf_nodes(a)