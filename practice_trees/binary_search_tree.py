""" 
Problem: Check if a given tree is a BST

            3
        /       \ 
      2           5
    /   \
   1     4

Tree given above is not a BST as 4 is to the left of 3. 
"""

class Node:

    def __init__(self, val, left=None, right=None) -> None:
        self.val = val 
        self.left = left 
        self.right = right 

def isBST(node, left, right):

    if not node:
        return True 

    if not node.val < right and node.val > left:
        return False 

    return (isBST(node.left, left, node.val) and isBST(node.right, node.val, right))

def checkForBST(root):

    return isBST(root, float("-inf"), float("inf"))
        

root = Node(3)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(4)

print(checkForBST(root))