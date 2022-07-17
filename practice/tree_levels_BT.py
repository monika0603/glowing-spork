""" 
Write a function, tree_levels, that takes in the root of a binary tree. The function should 
return a 2-Dimensional list where each sublist represents a level of the tree.
"""

class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val 
        self.left = left 
        self.right = right 

def tree_levels(node):
    if node is None:
       return -1 

    stack = [(node, 0)]
    path = [] 

    while stack:
        current, level_num = stack.pop()

        if len(path) == level_num:
            path.append([current.val])
        else:
            path[level_num].append(current.val)

        if current.left is not None:
            stack.append((current.left, level_num+1))
        if current.right is not None:
            stack.append((current.right, level_num+1))

    return path

# Driver code 
# Test case 01
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

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

print(tree_levels(a)) # ->
# [
#   ['a'],
#   ['b', 'c'],
#   ['d', 'e', 'f']
# ]