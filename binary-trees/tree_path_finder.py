""" 
Write a function, path_finder, that takes in the root of a binary tree and a 
target value. The function should return an array representing a path to the 
target value. If the target value is not found in the tree, then return None.

You may assume that the tree contains unique values.

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
"""
# Class to define a tree node
class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val 
        self.left = left 
        self.right = right 

def tree_includes(root, target):
    # Base case that handles if the root in none
    if root is None:
        return None 
    # Base case if root is equal to the target
    if root.val == target:
        return [root.val] 

    # recursive call to execute the first two base cases for root.left
    left_path = tree_includes(root.left, target)
    if left_path is not None:
        # Create a new list literal, put root.val in the front and *left_path puts 
        # all the original elements from the left_path into the new list
        return [root.val, *left_path]
    # recursive call to execute the first two base cases for root.right
    right_path = tree_includes(root.right, target)
    if right_path is not None:
        return [root.val, *right_path]

    return None


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
print(tree_includes(a, "d"))
        