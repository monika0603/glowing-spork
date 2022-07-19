""" 
Write a function, longest_path, that takes in an adjacency list for a directed acyclic graph. 
The function should return the length of the longest path within the graph. A path may start 
and end at any two nodes. The length of a path is considered the number of edges in the path, 
not the number of nodes.

Algorithm: The trick to solving this problem is to find the terminal nodes first and assign them 
a count of zero. 
"""

def longest_path(graph):

    distance = {}
    # Looping over all the nodes in the given graph and checking if any one them is 
    # a terminal node. Meaning if they have a length of zero. If yes, we assign them a zero 
    # using a hashmap.
    for node in graph:
        if len(graph[node]) == 0:
            distance[node] = 0 

    for node in graph:
        explore(graph, node, distance) 

    # Now simply get the maximum value stored in the distance dictionary. 
    return max(distance.values())

def explore(graph, node, distance):
    # Distance dictionary is used to check if we have visited the node previously
    # As well as calculate the distance 
    if node in distance:
        return distance[node] 

    max_length = 0 
    for neighbor in graph[node]:
        attempt = explore(graph, neighbor, distance)
        max_length = max(attempt, max_length) 

    # The reason we are add a one to the maxlenth is because we are calculating the distance from 
    # neighbor instead of the node. So adding 1 to get to the node
    distance[node] = 1 + max_length
    return distance[node]

# Driver code 
# Test case 01
graph = {
  'a': ['c', 'b'],
  'b': ['c'],
  'c': []
}

print(longest_path(graph)) # -> 2

# Test case 02
graph = {
  'a': ['c', 'b'],
  'b': ['c'],
  'c': [],
  'q': ['r'],
  'r': ['s', 'u', 't'],
  's': ['t'],
  't': ['u'],
  'u': []
}

print(longest_path(graph)) # -> 4

# Test case 03
graph = {
  'h': ['i', 'j', 'k'],
  'g': ['h'],
  'i': [],
  'j': [],
  'k': [],
  'x': ['y'],
  'y': []
}

print(longest_path(graph)) # -> 2