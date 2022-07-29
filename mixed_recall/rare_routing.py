""" 
Write a function, rare_routing, that takes in a number of cities (n) and a list of tuples 
where each tuple represents a direct road that connects a pair of cities. The function 
should return a boolean indicating whether or not there exists a unique route for every 
pair of cities. A route is a sequence of roads that does not visit a city more than once.

Cities will be numbered 0 to n - 1.

You can assume that all roads are two-way roads. This means if there is a road between 
A and B, then you can use that road to go from A to B or go from B to A.
"""

import collections
def rare_routing(num_of_cities, list_of_cities):

    graph = build_graph(num_of_cities, list_of_cities) 
    print(graph)

def build_graph(num_of_cities, list_of_cities):

    graph = collections.defaultdict(list) 

    for i in range(num_of_cities):
        graph[i] = [] 

    for x, y in list_of_cities:
        graph[x].append(y) 
        graph[y].append(x) 

    visited = set() 

    valid = explore(graph, 0, visited, None)

    return valid and len(visited) == num_of_cities

def explore(graph, node, visited, last_node):
    if node in visited:
        return False 

    visited.add(node) 

    for neighbor in graph[node]:
        if neighbor != last_node and explore(graph, neighbor, visited, node) == False:
            return False

    return True  
     


print(rare_routing(4, [
  (0, 1),
  (0, 2),
  (0, 3)
])) # -> True

print(rare_routing(4, [
  (0, 1),
  (0, 2),
  (0, 3),
  (3, 2)
])) # -> False