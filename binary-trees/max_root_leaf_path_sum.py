""" 
Write a function, max_path_sum, that takes in the root of a binary tree that contains 
number values. The function should return the maximum sum of any root to leaf path within the tree.

You may assume that the input tree is non-empty.

#       3
#    /    \
#   11     4
#  / \      \
# 4   -2     1
"""
class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val 
        self.left = left 
        self.right = right 

def max_path_sum(root):
    # If one of the child is None then assign it a negative infinity
    # Otherwise our code will throw an error that it can add a none type value
    if root is None:
        return float("-inf")

    # Logic to find a leaf node
    if root.left is None and root.right is None:
        return root.val 

    # Pick higher nade value between the left or the right
    max_left = max_path_sum(root.left)
    max_right = max_path_sum(root.right)
    # Increment the value 
    return root.val + max(max_left, max_right)  
        
# Driver code 
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


    

