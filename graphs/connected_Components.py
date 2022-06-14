"""_summary_
Write a function that takes in the adjacency matrix of an undirected graph. The function should return 
the number of connected components within the graph 

Returns:
    _type_: _description_
    Returns an integer which is the count of the connected components. 

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


def connectedComponents(graph):
    # Defining a set() type variable which will keep track if we have already visited a node
    visited = set()
    # Variable for counting the number of connected components
    count = 0 
    # Looping over the nodes in the given graph
    for nei in graph:
        print(visited)
        # explore any given node, and incrementing count if explore returns true
        if explore(graph, nei, visited) == True:
            count += 1 

    print(count)


def explore(graph, current, visited):
    # Base case of the current node has been visited, simply return False 
    if current in visited:
        return False 
    # Otherwise add the current node into visited set variable
    visited.add(current)
    # recursively call the function to explore every neighbor
    for neighbor in graph[current]:
        explore(graph, neighbor, visited)
    # return True by default
    return True 

print(connectedComponents(graph))