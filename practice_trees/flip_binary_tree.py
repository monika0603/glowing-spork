""" 
Write a function, flip_tree, that takes in the root of a binary tree. The function should flip 
the binary tree, turning left subtrees into right subtrees and vice-versa. This flipping should 
occur in-place by modifying the original tree. The function should return the root of the tree.
"""

class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val 
        self.left = left 
        self.right = right 

def flip_tree(node):
    if node is None:
        return None 

    temp = node.left 
    node.left = node.right 
    node.right = temp  

    flip_tree(node.left)
    flip_tree(node.right)

    return node 

# Driver code
# Test case 01 
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

#      a
#    /    \
#   b      c
#  / \      \
# d   e      f
#    / \
#    g  h

print(flip_tree(a))


