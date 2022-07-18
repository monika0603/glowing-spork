""" 
Write a function, has_path, that takes in a dictionary representing the adjacency list of a 
directed acyclic graph and two nodes (src, dst). The function should return a boolean 
indicating whether or not there exists a directed path between the source and destination nodes.
"""

def has_path(graph, src, dst):

    if src == dst:
        return True 

    for neighbor in graph[src]:
        if has_path(graph, neighbor, dst) == True:
            return True 

    return False 

def has_path_dfs(graph, src, dst):

    stack = [src]
    while stack:
        current = stack.pop() 

        if current == dst:
            return True 

        for neighbor in graph[current]:
            stack.append(neighbor)

    return False 

from collections import deque
def has_path_bfs(graph, src, dst):

    queue = deque([src])
    while queue:
        current = queue.popleft()

        if current == dst:
            return True 

        for neighbor in graph[current]:
            queue.append(neighbor)

    return False 

# Driver code
# Test case 01
graph = {
  'f': ['g', 'i'],
  'g': ['h'],
  'h': [],
  'i': ['g', 'k'],
  'j': ['i'],
  'k': []
}

print(has_path(graph, 'f', 'k')) # True
print(has_path_dfs(graph, 'f', 'k')) # True
print(has_path_bfs(graph, 'f', 'k')) # True

# Test case 02
graph = {
  'f': ['g', 'i'],
  'g': ['h'],
  'h': [],
  'i': ['g', 'k'],
  'j': ['i'],
  'k': []
}

print(has_path(graph, 'f', 'j')) # False
print(has_path_dfs(graph, 'f', 'j')) # False
print(has_path_bfs(graph, 'f', 'j')) # False

# Test case 03
