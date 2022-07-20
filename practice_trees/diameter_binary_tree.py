""" 
Problem: Calculate the diameter of a binary tree. Diameter of a binary tree is defined as the 
number of nodes on the longest path between two leaf nodes. 
"""

class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val 
        self.left = left 
        self.right = right 

def height(node):
    if node is None:
        return 0 

    # if the node is not none then recursively call the function to get the max height 
    return 1 + max(height(node.left), height(node.right))

def diameter(root):
    if root is None:
        return 0 

    lheight = height(root.left)
    rheight = height(root.right) 

    ldiameter = diameter(root.left)
    rdiameter = diameter(root.right) 

    # Return the max of the left subtree
    # 1) Diameter of the left subtree
    # 2) Diameter of the right subtree
    # 3) Height of the left subtree + height of the rightsubtree + 1

    return max(lheight + rheight + 1, max(ldiameter, rdiameter))

# Driver Code
"""
Constructed binary tree is
            1
          /   \
        2      3
      /  \
    4     5
"""
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
 
# Function Call
print(diameter(root))
