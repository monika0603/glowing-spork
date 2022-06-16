""" 
Problem: Write a function, has_path, that takes in a dictionary representing the 
adjacency list of a directed acyclic graph and two nodes (src, dst). The function 
should return a boolean indicating whether or not there exists a directed path 
between the source and destination nodes.
"""

graph = {
  'f': ['g', 'i'],
  'g': ['h'],
  'h': [],
  'i': ['g', 'k'],
  'j': ['i'],
  'k': []
}

def has_path(graph, nodeA, nodeB):

    # Base case: if source is equal to the destination, then return True
    if nodeA == nodeB:
        return True 

    # Otherwise check for current nodes neighbors
    for neighbor in graph[nodeA]:
        if has_path(graph, neighbor, nodeB) == True:
            return True 

    # return False by default
    return False 


print(has_path(graph, 'f', 'k'))

    

