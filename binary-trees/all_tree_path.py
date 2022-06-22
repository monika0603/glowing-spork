""" 
Write a function, all_tree_paths, that takes in the node of a binary tree. The function 
should return a 2-Dimensional list where each subarray represents a node-to-leaf path in 
the tree.

The order within an individual path must start at the node and end at the leaf, but the 
relative order among paths in the outer list does not matter.

You may assume that the input tree is non-empty.

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

# [ 
#   [ 'a', 'b', 'd' ], 
#   [ 'a', 'b', 'e' ], 
#   [ 'a', 'c', 'f' ] 
# ]
"""
# Class to define a tree node
class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val 
        self.left = left 
        self.right = right

def all_tree_paths(root):
    # Base case that handles if the root in none
    if root is None:
        return []
    # Base case if we've reached a leaf node the return a 2d list containing the 
    # root value
    if root.left is None and root.right is None:
        return [ [root.val] ]
    # Defining a list that will contain individual paths 
    paths = [] 

    # From the left_sub_path variable we expect the following 
    # [
    # ['b','d]
    # ['b','e']
    # ] 
    left_sub_path = all_tree_paths(root.left)
    # So we need to iterate over individual lists to append the root value
    for sub_path_left in left_sub_path:
        paths.append([root.val, *sub_path_left])
    # Similarly for right sub path
    right_sub_path = all_tree_paths(root.right)
    for sub_path_right in right_sub_path:
        paths.append([root.val, *sub_path_right])

    return paths
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

print(all_tree_paths(a))