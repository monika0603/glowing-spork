""" 
Write a function, post_order, that takes in the root of a binary tree. The function should return a 
list containing the post-ordered values of the tree.

Post-order traversal is when nodes are recursively visited in the order: left child, right child, 
self.
"""

class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val 
        self.left = left 
        self.right = right 

def post_order(node):
    result = []
    values = post_order_traversal(node, result)
    return values 

def post_order_traversal(node, result):
    if node is None:
        return 

    # post-order traversal --> left right node
    post_order_traversal(node.left, result)
    post_order_traversal(node.right, result)
    result.append(node.val)

    return result 

# Driver code
# Test case 01
x = Node('x')
y = Node('y')
z = Node('z')

x.left = y
x.right = z

#       x
#    /    \
#   y      z

print(post_order(x))
# ['y', 'z', 'x']

# test case 02 
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g
  
#      a
#    /    \
#   b      c
#  / \    / \
# d   e  f   g

print(post_order(a))
# [ 'd', 'e', 'b', 'f', 'g', 'c', 'a' ] 