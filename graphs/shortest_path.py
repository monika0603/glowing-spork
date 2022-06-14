"""_summary_

Write a function, shortest_path, that takes in a list of edges for an undirected graph 
and two nodes (node_A, node_B). The function should return the length of the shortest path 
between A and B. Consider the length as the number of edges in the path, not the number of 
nodes. If there is no path between A and B, then return -1.

w - x - y -- z
\           /
 \         /
  \       /
   \     /
    \ v /
"""

edges = [
  ['w', 'x'],
  ['x', 'y'],
  ['z', 'y'],
  ['z', 'v'],
  ['w', 'v']
]

edges = [
  ['w', 'x'],
  ['x', 'y'],
  ['z', 'y'],
  ['z', 'v'],
  ['w', 'v']
]

import collections
def shortest_path(edges, nodeA, nodeB):

    adj = collections.defaultdict(list)

    for x, y in edges:
        adj[x].append(y)
        adj[y].append(x)

    print(adj)
    
    visited = set(nodeA)
    # starting a BFS
    queue = [[nodeA, 0]] 

    while(len(queue) > 0):
        # Following a true BFS technique, removing from the front of the queue
        # This time out queue contains a list, so unpacking it into currentNode and distance
        currentNode, distance = queue.pop(0)

        # If my current node is equal to the final node(nodeB), then I just need to return 
        # the distance. If not we need to continue searching. 
        if currentNode == nodeB:
            return distance

        for neighbor in adj[currentNode]:
            # First check if the currentNode is not in visited. 
            # and if not visited then we add to visited to prevent getting stuck in a loop
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append([neighbor, distance+1])

    return -1
        


print(shortest_path(edges, 'y', 'x'))