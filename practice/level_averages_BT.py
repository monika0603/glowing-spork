""" 
Write a function, level_averages, that takes in the root of a binary tree that contains number values. 
The function should return a list containing the average value of each level.
"""

class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val 
        self.left = left 
        self.right = right 

def level_averages(node):
    if node is None:
        return [] 

    queue = [(node, 0)]
    average = [] 
    average1 = []

    while queue:
        current, level = queue.pop(0)

        if len(average) == level:
            average.append([current.val]) 
        else:
            average[level].append(current.val) 

        if current.left is not None:
            queue.append((current.left, level+1))
        if current.right is not None:
            queue.append((current.right, level+1))

    for level in average:
        average1.append(sum(level)/len(level))
    
    return average1

# Driver code
# Test case 01
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

print(level_averages(a))
