""" 
Write a function, tree_value_count, that takes in the root of a binary tree and a target value. The 
function should return the number of times that the target occurs in the tree.
"""

class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val 
        self.left = left 
        self.right = right 

def tree_value_count(node, target):
    if node is None:
        return 0  

    queue = [node]
    count = 0 

    while queue:
        current = queue.pop(0)
        if current.val == target:
            count += 1 

        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)

    return count 

a = Node(12)
b = Node(6)
c = Node(6)
d = Node(4)
e = Node(6)
f = Node(12)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
print(tree_value_count(a, 6))