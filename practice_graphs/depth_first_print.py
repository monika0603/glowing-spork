""" 
Depth-first-print of a graph

Time complexity for DFS/BFS is O(n) where n = number of nodes in the graph
deque or pop using O(1)/constant time complexity. O(n) time complexity comes 
from the while loop when we are interating over the stack/deque DS. 
"""

graph = { 
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": []
}

def depth_first_print(graph, start):

    stack = [start] # Current stack [a]

    while stack:
        current = stack.pop()

        print(current)
        # FIFO operation will add b and c to the stack
        # [b, c]
        # Since is the end, it gets printed first and so on
        for neighbor in graph[current]: 
            stack.append(neighbor)

# Now instead of explicitly using a stack we can use a recursive function to call an 
# underlying stack
# Notice that the output is different in the below case
def depth_first_search(graph, current):
    print(current)

    for neighbor in graph[current]:
        depth_first_search(graph, neighbor)

# Breadth-first-traversal for a graph
from collections import deque
def breadth_first_search(graph, start):
    # Using a deque DS in Python to efficiently get the first element of the list 
    # If simply chop off the first element of a simple list, then the entire list needs 
    # to be shifted to the left to reduce the length. Which makes is inefficient.
    # Whereas deque is a double-ended DS in python so we can efficiently chop off either ends.  
    queue = deque([start])

    while queue:
        # popleft runs in O(1) time
        current = queue.popleft()
        print(current)

        for neighbor in graph[current]:
            queue.append(neighbor)

print(depth_first_print(graph, "a"))
print(depth_first_search(graph, "a"))
print(breadth_first_search(graph, "a"))