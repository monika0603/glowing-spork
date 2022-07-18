""" 
Write a function, shortest_path, that takes in a list of edges for an undirected graph and 
two nodes (node_A, node_B). The function should return the length of the shortest path between 
A and B. Consider the length as the number of edges in the path, not the number of nodes. 
If there is no path between A and B, then return -1.

BFS starts traversal equally in all directions, which is why it gives us the shorted path between 
source and destination
"""

import collections
from re import I

def shortest_path(edges, start, end):

    graph = collections.defaultdict(list)

    for x,y in edges:
        graph[x].append(y)
        graph[y].append(x) 

    visited = set()
    queue = []
    queue.append([start, 0])

    while queue:
        current, distance = queue.pop(0)

        if current == end:
            return distance

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append([neighbor, distance+1])

    return -1 

       
edges = [
  ['w', 'x'],
  ['x', 'y'],
  ['z', 'y'],
  ['z', 'v'],
  ['w', 'v']
]
print(shortest_path(edges, 'w', 'z')) # --> 2


