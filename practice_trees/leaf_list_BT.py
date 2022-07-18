""" 
Write a function, leaf_list, that takes in the root of a binary tree and returns a list 
containing the values of all leaf nodes in left-to-right order.
"""

class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val 
        self.left = left 
        self.right = right 

result = []
def leaf_list(node):
    if node is None:
        return [] 

    if node.left is None and node.right is None:
        result.append(node.val)

    right = leaf_list(node.right)
    left = leaf_list(node.left) 
    

    return result  

# Driver code
# Test case 01  

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

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

print(leaf_list(a)) # -> [ 'd', 'e', 'f' ] 