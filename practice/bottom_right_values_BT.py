""" 
Write a function, bottom_right_value, that takes in the root of a binary tree. The 
function should return the right-most value in the bottom-most level of the tree.

You may assume that the input tree is non-empty.
"""

class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val 
        self.left = left 
        self.right = right

def bottom_right_value(node):
    if node is None:
        return -1 

    queue = [node]
    value = 0 

    while queue:
        current = queue.pop(0)
        
        value = current.val 

        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)

    return value 

# Driver code
# Test case 01 
a = Node(3)
b = Node(11)
c = Node(10)
d = Node(4)
e = Node(-2)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#       3
#    /    \
#   11     10
#  / \      \
# 4   -2     1

print(bottom_right_value(a)) # -> 1

# Test case 02 
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

#        -1
#      /   \
#    -6    -5
#   /  \     \
# -3   -4   -13
#     / \       
#    -2  6

print(bottom_right_value(a)) # -> 6

# Test case 3
a = Node(-1)
b = Node(-6)
c = Node(-5)
d = Node(-3)
e = Node(-4)
f = Node(-13)
g = Node(-2)
h = Node(6)
i = Node(7)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
e.right = h
f.left = i

#        -1
#      /   \
#    -6    -5
#   /  \     \
# -3   -4   -13
#     / \    /   
#    -2  6  7 

print(bottom_right_value(a)) # -> 7