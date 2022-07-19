""" 
Write a function, has_cycle, that takes in an object representing the adjacency list of a 
directed graph. The function should return a boolean indicating whether or not the graph 
contains a cycle.

Algorithm: Using the concept of white-grey-black 
White - All nodes have white color to begin with, meaning they are unexplored
Grey - means we are visiting the node
Black - means that we have fully visited the node
"""

def has_cycle(graph):

    visiting = set() # Node is in progress
    visited = set()  # Node has been fully explored

    for node in graph:
        if explore(graph, node, visiting, visited) == True:
            return True 

    return False 
            

def explore(graph, node, visiting, visited):
    # If I have marked a node as visiting previsouly and got back to it, then I have 
    # detected a cycle
    if node in visiting:
        return True 

    visiting.add(node) 

    for neighbor in graph[node]:
        if explore(graph, neighbor, visiting, visited) == True:
            return True 

    # Make sure to manage the visiting set properly, remove the node from visiting 
    # and add it to visited 
    visiting.remove(node) 
    visited.add(node)

    return False 

# Driver code
# Test case 01 
print(has_cycle({
  "a": ["b"],
  "b": ["c"],
  "c": ["a"],
})) # -> True

# Test case 02 
print(has_cycle({
  "a": ["b", "c"],
  "b": ["c"],
  "c": ["d"],
  "d": [],
})) # -> False

# Test case 03
print(has_cycle({
  "a": ["b", "c"],
  "b": [],
  "c": [],
  "e": ["f"],
  "f": ["e"],
})) # -> True

# Test case 04
print(has_cycle({
  "q": ["r", "s"],
  "r": ["t", "u"],
  "s": [],
  "t": [],
  "u": [],
  "v": ["w"],
  "w": [],
  "x": ["w"],
})) # -> False

# Test case 05
print(has_cycle({
  "a": ["b"],
  "b": ["c"],
  "c": ["a"],
  "g": [],
})) # -> True