""" 
Problem: We are given an edge list for an undirected graph. And our job is to find if a cycle exists in the 
list of edges. 

Every pair in this edge list represents a connection between two nodes. Meaning there is an edge between 
i to j and vice-versa is also true. Graph for the list can be shown as below. 

  i --------- j 
  |
  |
  |
  k --------- l 
  |
  |
  |
  m 

  o --------- n 
"""

edges = [
    ['i', 'j'],
    ['k', 'i'],
    ['m', 'k'],
    ['k', 'l'],
    ['o', 'n']
]

from collections import defaultdict 
def hasPath(graph, src, dst, visited):
    # base case, if the source is equal to the destination, then we have found a cycle
    if src == dst:
        return True 
    # checks if the source has previously been visited or not
    if src in visited:
        return False 

    # if not, then I am currently visiting it, so add it to the set
    visited.add(src)
    

    for nei in graph[src]:
        if hasPath(graph, nei, dst, visited) == True:
            print(nei, dst)
            return True 

    return False 


def cycle(edges, nodeA, nodeB):

    adj_matrix = defaultdict(list) 

    # building adjacency list for the list of edges given
    for x, y in edges:
        adj_matrix[x].append(y)
        adj_matrix[y].append(x)

    visited = set()
    return hasPath(adj_matrix, nodeA, nodeB, visited)
    

print(cycle(edges, 'j', 'm'))