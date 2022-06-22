""" 
Write a function, tree_levels, that takes in the root of a binary tree. The function 
should return a 2-Dimensional list where each sublist represents a level of the tree.

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

Output: 
# [
#   ['a'],
#   ['b', 'c'],
#   ['d', 'e', 'f']
# ]
"""

# Class to define a tree node
class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val 
        self.left = left 
        self.right = right 

def tree_levels(root):
    # Base case that handles if the root in none
    # Making sure we return a consistent data type for return, so we return a list
    if root is None:
        return [] 

    # Using a stack DS for iterative recursive call 
    # Adding a tuple instead of just root which consists on root and it's level starting 
    # from zero. 
    stack = [(root, 0)] 
    # levels list to append nodes at each level
    levels = []

    while stack:
        # Popping from the end of the stack for LIFO operation
        current, level_num = stack.pop() 

        # If the length of previously defined list is equal to the level number popped from the tuple
        # then I want to add the value of the node
        if len(levels) == level_num:
            levels.append([current.val]) 
        # otherwise the level already exists in levels list, I simple want to append node value to it
        else:
            levels[level_num].append(current.val)
        # Finally incrementing level number for right node and left node
        if current.right is not None:
            stack.append((current.right, level_num+1)) 
        if current.left is not None:
            stack.append((current.left, level_num+1))

    return levels
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

print(tree_levels(a))