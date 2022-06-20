""" 
Write a function, depth_first_values, that takes in the root of a binary tree. 
The function should return a list containing all values of the tree in depth-first order.

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

pre-order: root left right
in-order: left root right 
post-order: left right root
"""
class Node:

    def __init__(self, val, left=None, right=None) -> None:
        self.val = val 
        self.left = left 
        self.right = right 

def depth_first_values(root):
    # Base case if the node is empty
    if not root:
        return [] 

    # stack for DFS, queue for BFS
    stack = [root]
    # List to store all the values
    values = []
    # while stack doesn't become empty
    while stack:
        # Pop from the end of the stack. When implementing BFS, simply pop from 
        # the front of the queue (instad) of stack
        current = stack.pop()
        values.append(current.val)
        # left node
        if current.left is not None:
            stack.append(current.left)
        # right node
        if current.right is not None:
            stack.append(current.right)

    return values 

# Driver code 

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')        
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

print(depth_first_values(a))
