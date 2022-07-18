""" 
Write a function, connected_components_count, that takes in the adjacency list of an 
undirected graph. The function should return the number of connected components within the graph.
"""

def connected_component_count(graph):

    visited = set() 
    count = 0
    for node in graph:
        if explore(graph, node, visited) == True:
            count += 1
    return count 

def explore(graph, node, visited):
    if node in visited:
        return False 

    visited.add(node)

    for neighbor in graph[node]:
        explore(graph, neighbor, visited)

    return True 

graph = {
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
}

print(connected_component_count(graph))