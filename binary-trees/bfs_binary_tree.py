""" 
Write a function, breadth_first_values, that takes in the root of a binary tree. The 
function should return a list containing all values of the tree in breadth-first order.

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

"""
# Base class for tree definition
class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val 
        self.left = left 
        self.right = right 
        
def breadth_first_values(node):
    # Base case if the node is none
    if node is None:
        return [] 

    values = []
    # Using queue data structure for BFS instead of stack
    queue = [node]

    while queue:
        # Popping from the front of the queue for LIFO operation
        current = queue.pop(0)
        # Appending the values to values
        values.append(current.val)
        # Check if left is not none
        if current.left is not None:
            queue.append(current.left)
        # Check if right is not none
        if current.right is not None:
            queue.append(current.right)

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

print(breadth_first_values(a))