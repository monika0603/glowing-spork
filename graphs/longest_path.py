""" 
Problem: Write a function, longest_path, that takes in an adjacency list for a 
directed acyclic graph. The function should return the length of the longest path 
within the graph. A path may start and end at any two nodes. The length of a path is 
considered the number of edges in the path, not the number of nodes.

     a
   /   \
  c  <-  b

Number of edges in this case is 2.

Key to solving this problem is to find a terminal and work our way up from there to 
count the number of edges. 
"""

def longest_path(graph):
    # Defining a dictionary to store distances (as nodes) from the terminal nodes
    distance = {}
    # First loop is to identify every single terminal node in a given graph
    for node in graph:
        # if the length of the node is zero, that means it is a terminal node
        if len(graph[node]) == 0:
            # Terminal nodes are zero distance from themselves
            distance[node] = 0

    for node in graph:
        traverse_distance(graph, node, distance)

    return max(distance.values())

def traverse_distance(graph, node, distance):
    # Base case if the node exists in the dictionary, then I simply want to return it's 
    # distance from the terminal node 
    if node in distance:
        return distance[node] 

    max_length = 0
    for neighbor in graph[node]:
        attempt = traverse_distance(graph, neighbor, distance) 
        max_length = max(attempt, max_length)

    distance[node] = 1 + max_length

    return distance[node]

graph = {
  'a': ['c', 'b'],
  'b': ['c'],
  'c': []
}

print(longest_path(graph))