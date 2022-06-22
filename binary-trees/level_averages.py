""" 
Write a function, level_averages, that takes in the root of a binary tree that 
contains number values. The function should return a list containing the average value of each level.

#       3
#    /    \
#   11     4
#  / \      \
# 4   -2     1
"""
# Class to define a tree node
class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val 
        self.left = left 
        self.right = right 

def level_averages(root):
    # Base case that handles if the root in none
    # Making sure we return a consistent data type for return, so we return a list
    if not root:
        return [] 
    # Using a stack DS for iterative recursive call 
    # Adding a tuple instead of just root which consists on root and it's level starting 
    # from zero. 
    stack = [(root, 0)]
    levels = [] 
    # levels list to append nodes at each level
    result = []

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

    # Logic to calculate average for each level
    for level in levels:
        level_avg = sum(level)/len(level)
        result.append(level_avg)
    return result


# Test case I
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
#       3
#    /    \
#   11     4
#  / \      \
# 4   -2     1
# --> [ 3, 7.5, 1 ] 

# Test case II
a = Node(5)
b = Node(11)
c = Node(54)
d = Node(20)
e = Node(15)
f = Node(1)
g = Node(3)

a.left = b
a.right = c
b.left = d
b.right = e
e.left = f
e.right = g

#        5
#     /    \
#    11    54
#  /   \
# 20   15
#      / \
#     1  3
# --> [ 5, 32.5, 17.5, 2 ] 
print(level_averages(a))