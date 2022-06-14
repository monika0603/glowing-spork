"""_summary_
Write a function, largest_component, that takes in the adjacency list of an undirected graph. 
The function should return the size of the largest connected component in the graph.
"""

graph = {
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
}

def longest_component(graph):

    # varibale visited as a set variable to keep track of visited nodes 
    visited = set()
    # Variable to check for the largest connected component
    longest = 0

    # loop over all the nodes in a graph
    for nei in graph:
        # Explore each node and recursively call the explore function 
        # explore function returns the size of the connected component
        size = explore(graph, nei, visited)
        # pick maximum between longest and size 
        longest = max(longest, size)

    return longest 

def explore(graph, current, visited):
    # base case if the current node is already in visited, then return 0 
    if current in visited:
        return 0 

    # Add node in the set variable. This helps to prevent an infinite loop for undirected graphs
    visited.add(current)
    # size must start from 1 instead of 0
    size = 1
    # looping over each neighbor in a node and incrementing the size 
    for neighbor in graph[current]:
        size += explore(graph, neighbor, visited)

    # return the size 
    return size 

print(longest_component(graph))