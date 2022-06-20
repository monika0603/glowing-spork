""" 
Write a function, tree_includes, that takes in the root of a binary tree and a target value. 
The function should return a boolean indicating whether or not the value is contained in the tree.

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
"""
# Base class for defining a tree
class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val 
        self.left = left 
        self.right = right 

def tree_includes(root, target):
    # base case if the node is empty, return false
    if not root:
        return False 

    # defining a queue and appending root to it
    queue = []
    queue.append(root)

    while queue:
        # Popping from the front of the queue
        current = queue.pop(0)
        # Check to see if current node is equal to the target
        if current.val == target:
            return True 
        # Otherwise keep checking to the left and right
        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)
    # base case if we never find an existing node
    return False 

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

# Driver code
print(tree_includes(a, "v"))