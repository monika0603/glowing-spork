""" 
Write a function, lowest_common_ancestor, that takes in the root of a binary tree and two values. 
The function should return the value of the lowest common ancestor of the two values in the tree.

You may assume that the tree values are unique and the tree is non-empty.

Note that a node may be considered an ancestor of itself.
"""

class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val 
        self.left = left 
        self.right = right 

def lowest_common_ancestor(node, t1, t2):
    if node is None:
        return None 

    path_1 = tree_path(node, t1)
    path_2 = tree_path(node, t2) 

    result = [] 

    for a,b in zip(path_1, path_2):
        if a==b:
            result.append(a) 

    return result[-1]

def tree_path(node, t):
    if node is None:
        return None 

    if node.val == t:
        return [node.val] 

    left_path = tree_path(node.left, t)
    if left_path is not None:
        return [node.val, *left_path] 

    right_path = tree_path(node.right, t) 
    if right_path is not None:
        return [node.val, *right_path] 

    return None 
    

# Driver code 
# Test case 01
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

#      a
#    /    \
#   b      c
#  / \      \
# d   e      f
#    / \
#    g  h

print(lowest_common_ancestor(a, 'b', 'c'))

# Test case 02
print(lowest_common_ancestor(a, 'd', 'h'))