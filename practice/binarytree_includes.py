""" 
Write a function, tree_includes, that takes in the root of a binary tree and a target value. 
The function should return a boolean indicating whether or not the value is contained in the tree.

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
"""

class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val 
        self.left = left 
        self.right = right 

def tree_includes(node, target):
    if node is None:
        return False 

    stack = [node]

    while stack:
        current = stack.pop()

        if current.val == target:
            return True 

        if current.left is not None:
            stack.append(current.left) 
        if current.right is not None:
            stack.append(current.right)

    return False 

# Driver code
# Test case 01
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

print(tree_includes(a, "e"))

# Test case 02
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

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

print(tree_includes(a, "a"))

# Test case 03
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

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

print(tree_includes(a, "n"))