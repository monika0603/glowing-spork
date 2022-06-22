""" 
Write a function, bottom_right_value, that takes in the root of a binary tree. 
The function should return the right-most value in the bottom-most level of the tree.

You may assume that the input tree is non-empty.

#       A
#    /    \
#   B      C
#  / \      
# D   E     

Bottom-right value = E 

Various iterations of the BFS is annotated below. 
queue = A: current 
queue = : current = A
queue = C B current = A
queue = E D C current = B
queue = E D current = C 
queue = E current = D 
queue = empty current = E
"""
# Class to define a tree node
class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val 
        self.left = left 
        self.right = right 

def bottom_right(node):
    # Base case that handles if the root in none
    if not node:
        return -1
    # queue variable for FIFO operation
    queue = [node]
    # variable to store the bottom-right value
    value = 0
    while queue:
        # popping from the front of the queue
        current = queue.pop(0)
        # storing root.val in value, when the queue gets empty, last value is what we want
        value = current.val
        # IMPORTANT: appending from the left of the node
        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)

    return value
    
# Driver code
a = Node(-1)
b = Node(-6)
c = Node(-5)
d = Node(-3)
e = Node(-4)
f = Node(-13)
g = Node(-2)
h = Node(6)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
e.right = h

print(bottom_right(a))