""" 
Write a function, undirected_path, that takes in a list of edges for an undirected graph 
and two nodes (node_A, node_B). The function should return a boolean indicating whether 
or not there exists a path between node_A and node_B.
"""

from collections import defaultdict
import collections 
def undirected_path(edges, start, end):

    graph = collections.defaultdict(list)
    # Since this is an undirected graph, it is important to create an adjacency list for i to j as 
    # well as to j to i
    for x,y in edges:
        graph[x].append(y)
        graph[y].append(x) 
    # A set type variable that is going to keep track of visited nodes. 
    # Set has O(1) inserting/look-up time
    visited = set()

    return has_path(graph, start, end, visited)


    
def has_path(graph, start, end, visited):
    # If previously visited, then return
    if start in visited:
        return 
    # Otherwise add it to the set
    visited.add(start)
    # Base case if I find what I am looking for
    if start == end:
        return True 
    # Iterating through the neighbors of the start node
    for neighbor in graph[start]:
        if has_path(graph, neighbor, end, visited) == True:
            return True 
    return False 

edges = [
  ('i', 'j'),
  ('k', 'i'),
  ('m', 'k'),
  ('k', 'l'),
  ('o', 'n')
]

print(undirected_path(edges, 'j', 'm'))