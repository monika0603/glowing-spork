""" 
Write a function, all_tree_paths, that takes in the root of a binary tree. The function 
should return a 2-Dimensional list where each subarray represents a root-to-leaf path in the tree.

The order within an individual path must start at the root and end at the leaf, but the relative 
order among paths in the outer list does not matter.

You may assume that the input tree is non-empty.
"""

from unittest.mock import NonCallableMagicMock


class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val 
        self.left = left 
        self.right = right 

def all_tree_paths(node):
    if node is None:
        return []

    if node.left is None and node.right is None: 
        return [[node.val]] 

    path = []

    left_sub_path = all_tree_paths(node.left)
    for left in left_sub_path:
        path.append([node.val, *left])

    right_sub_path = all_tree_paths(node.right)
    for right in right_sub_path:
        path.append([node.val, *right])

    return path 

# Driver code 
# Test case 01
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

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

print(all_tree_paths(a)) # ->
# [ 
#   [ 'a', 'b', 'd' ], 
#   [ 'a', 'b', 'e' ], 
#   [ 'a', 'c', 'f' ] 
# ] 

# Test case 02
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
h = Node('h')
i = Node('i')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
e.right = h
f.left = i

#         a
#      /    \
#     b      c
#   /  \      \
#  d    e      f
#      / \    /   
#     g  h   i 

print(all_tree_paths(a)) # ->
# [ 
#   [ 'a', 'b', 'd' ], 
#   [ 'a', 'b', 'e', 'g' ], 
#   [ 'a', 'b', 'e', 'h' ], 
#   [ 'a', 'c', 'f', 'i' ] 
# ] 