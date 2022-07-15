""" 
Write a function, depth_first_values, that takes in the root of a binary tree. The function 
should return a list containing all values of the tree in depth-first order.
"""
# Basic class Node for tree definition
class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val 
        self.left = left 
        self.right = right 

def depth_first_search(node):
    # Base case if the node itself is null
    if node is None:
        return [] 

    # Using stack for FIFO operation
    values = []
    # Adding the node to the stack
    stack = [node]
    # While stack is not empty
    while stack:
        # pop from the top of the stack
        current = stack.pop()
        # Appending the value to the stack
        values.append(current.val)
        # Similarly checking if right child is not none
        if current.right is not None:
            stack.append(current.right) 
        # Checking if the left child is not none 
        if current.left is not None:
            stack.append(current.left)
        

    return values 

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

print(depth_first_search(a))