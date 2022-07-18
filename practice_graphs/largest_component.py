""" 
Write a function, largest_component, that takes in the adjacency list of an undirected graph. 
The function should return the size of the largest connected component in the graph.
"""

def largest_component(graph):

    visited = set()
    max_size = 0
    for node in graph:
        size = explore(graph, node, visited)
        max_size = max(size, max_size)

    return max_size

def explore(graph, node, visited):
    if node in visited:
        return 0

    visited.add(node)
    size = 1

    for neighbor in graph[node]:
        size += explore(graph, neighbor, visited)

    return size 

# Driver code
# Test case 01
graph = {
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
}

print(largest_component(graph))

# Test case 02
print(largest_component({
  1: [2],
  2: [1,8],
  6: [7],
  9: [8],
  7: [6, 8],
  8: [9, 7, 2]
})) # -> 6

# Test case 03
print(largest_component({
  3: [],
  4: [6],
  6: [4, 5, 7, 8],
  8: [6],
  7: [6],
  5: [6],
  1: [2],
  2: [1]
}))

# Test case 04
print(largest_component({}))

# Test case 05
print(largest_component({
  0: [4,7],
  1: [],
  2: [],
  3: [6],
  4: [0],
  6: [3],
  7: [0],
  8: []
}))