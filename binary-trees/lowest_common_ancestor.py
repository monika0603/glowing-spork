""" 
Write a function, lowest_common_ancestor, that takes in the root of a binary tree and 
two values. The function should return the value of the lowest common ancestor of the 
two values in the tree.

You may assume that the tree values are unique and the tree is non-empty.

Note that a node may be considered an ancestor of itself.

#      a
#    /    \
#   b      c
#  / \      \
# d   e      f
#    / \
#    g  h

lowest_common_ancestor(a, 'd', 'h') --> b 
"""

import re


class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val 
        self.left = left 
        self.right = right 

def match(root, target_a, target_b):

    result_a = lowest_common_ancestor(root, target_a)
    result_b = lowest_common_ancestor(root, target_b)

    result = []
    for a,b in zip(result_a, result_b):
        if a==b:
            result.append(a) 

    return result[-1]

def lowest_common_ancestor(root, target):
    if root is None:
        return None 
    
    if root.val == target:
        return [root.val] 

    left_path = lowest_common_ancestor(root.left, target)
    if left_path is not None:
        return [root.val, *left_path]

    right_path = lowest_common_ancestor(root.right, target)
    if right_path is not None:
        return [root.val, *right_path]

    return None 

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
h = Node('h')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
e.right = h
print(match(a, 'b','g'))

    