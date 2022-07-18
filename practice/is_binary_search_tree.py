""" 
Write a function, is_binary_search_tree, that takes in the root of a binary tree. The function 
should return a boolean indicating whether or not the tree satisfies the binary search tree property.

A Binary Search Tree is a binary tree where all values within a node's left subtree are smaller 
than the node's value and all values in a node's right subtree are greater than or equal to the 
node's value.
"""

import numbers


class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val 
        self.left = left 
        self.right = right 

def is_binary_search_tree(node):
    result = in_order_traversal(node, [])
    
    return is_sorted(result)
    
def is_sorted(values):

    for i in range(0, len(values)-1):
        current = values[i]
        next = values[i+1]

        if next < current:
            return False 
    return True 


def in_order_traversal(node, result):
    if node is None:
        return 

    in_order_traversal(node.left, result)
    result.append(node.val)
    in_order_traversal(node.right, result)

    return result 

# Driver code 
# Test case 01 
a = Node(12)
b = Node(5)
c = Node(18)
d = Node(3)
e = Node(9)
f = Node(19)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      12
#    /   \
#   5     18
#  / \     \
# 3   9     19

print(is_binary_search_tree(a)) # -> True

# Test case 02 
a = Node(12)
b = Node(5)
c = Node(18)
d = Node(3)
e = Node(15)
f = Node(19)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      12
#    /   \
#   5     18
#  / \     \
# 3   15     19

print(is_binary_search_tree(a)) # -> False