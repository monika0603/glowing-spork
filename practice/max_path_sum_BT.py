""" 
Write a function, max_path_sum, that takes in the root of a binary tree that contains number values. 
The function should return the maximum sum of any root to leaf path within the tree.

You may assume that the input tree is non-empty.
Important: Tree problems with paths should be solved recurssively.
"""

class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val 
        self.left = left 
        self.right = right 

def max_path_sum(node):
    if node is None:
        return 0 

    # Base case, we've found a leaf node
    if node.left is None and node.right is None:
        return node.val 

    max_left = max_path_sum(node.left)
    max_right = max_path_sum(node.right) 

    return node.val + max(max_right, max_left)

    
# Driver code
# Test case 01
a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(-2)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

print(max_path_sum(a))

# Test case 02
a = Node(5)
b = Node(11)
c = Node(54)
d = Node(20)
e = Node(15)
f = Node(1)
g = Node(3)

a.left = b
a.right = c
b.left = d
b.right = e
e.left = f
e.right = g

#        5
#     /    \
#    11    54
#  /   \      
# 20   15
#      / \
#     1  3
print(max_path_sum(a))