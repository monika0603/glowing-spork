""" 
Write a function, tree_sum, that takes in the root of a binary tree that 
contains number values. The function should return the total sum of all values in the tree.

#       3
#    /    \
#   11     4
#  / \      \
# 4   -2     1

This problem is a simple extension of the previous implementation of BFS/DFS for a binary tree. 
I've just defined a variable, sum, initialized it with zero and incremented with node.val.
"""

class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val 
        self.left = left 
        self.right = right 

def tree_sum(root):
    sum = 0 
    if not root:
        return sum

    queue = []
    queue.append(root)
    
    while queue:
        current = queue.pop(0)

        sum += current.val
        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)

    return sum

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

print(tree_sum(a))
