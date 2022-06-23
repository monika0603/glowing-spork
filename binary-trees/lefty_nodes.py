""" 
Write a function, lefty_nodes, that takes in the root of a binary tree. The function 
should return a list containing the left-most value on every level of the tree. The 
list must be ordered in a top-down fashion where the root is the first item.

#      a
#    /    \
#   b      c
#  / \      \
# d   e      f
#    / \
#    g  h

lefty_nodes(a) # [ 'a', 'b', 'd', 'g' ]
"""
# Class to define a tree node
class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val 
        self.left = left 
        self.right = right 

def lefty_nodes(root):
    # Base case that handles if the root in none
    if root is None:
        return None 
    # stack variable for LIFO operation
    stack = [(root, 0)] 
    levels = []

    # While stack is not empty
    while stack:
        # popping from the stack
        current, level = stack.pop()
        # if the level matches with the length of levels, then append current node's value
        if len(levels) == level:
            levels.append(current.val) 

        # Start with the right node first for appending, that way we pop the left node first
        # Which is what we want to add
        if current.right is not None:
            stack.append((current.right, level+1))
        if current.left is not None:
            stack.append((current.left, level+1))
        

    return levels
# Driver code
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
h = Node('h')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
e.right = h

print(lefty_nodes(a))
