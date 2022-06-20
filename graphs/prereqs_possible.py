""" 
Write a function, prereqs_possible, that takes in a number of courses (n) 
and prerequisites as arguments. Courses have ids ranging from 0 through 
n - 1. A single prerequisite of (A, B) means that course A must be taken 
before course B. The function should return a boolean indicating whether 
or not it is possible to complete all courses.

If you visualize this problem given below, you'll find that there is a cycle 
detected. For courses which have a cylce, it is impossible to find minimum 
prerequisites. 

d -- > b --> a --> c 
^    ^
|  /              |
e <----------------  

There is a cycle in e, b, a, c, and e nodes. So the answer is False 
"""

numCourses = 6
prereqs = [
  (0, 1),
  (2, 3),
  (0, 2),
  (1, 3),
  (4, 5),
] 

def prereqs_possible(numCourses, prereqs):

    # Helper function to build an adjacency list for the information provided
    graph = build_graph(numCourses, prereqs)
    # Variables to mark nodes as gray and black
    # In this code, nodes are not literally marked white/grey/black. But we keep 
    # track of them in visiting (in the process of being explored) or visited (done exploring).
    visiting = set() 
    visited = set() 
    # Iterating over every node in the adjacency matrix
    for node in graph:
        # If the DFS returns true, then we have detected a cycle and we must return False 
        if detect_cycle(graph, node, visiting, visited) == True:
            return False  
    # Base case, return True if no cycle is detected
    return True 

# DFS implementation
def detect_cycle(graph, node, visiting, visited):
    # if node is in visited set, then it has been previously explored. 
    # No need to explore any further
    if node in visited:
        return False 
    # Base case, node exists in visiting, cycle has been detected
    if node in visiting:
        return True 
    # If not, add it to the visiting
    visiting.add(node)

    # Exploring all the neighbors of the node
    for neighbor in graph[node]:
        # If the above code return true, we have detected a cycle
        if detect_cycle(graph, neighbor, visiting, visited) == True:
            return True 
    # Otherwise remove the node from visitng and add it to visited 
    visiting.remove(node)
    visited.add(node)

    # return False by defaul if above conditions don't apply. 
    return False 

# Code to generate an adjacency matrix
import collections 
def build_graph(numCourses, prereqs):

    graph = collections.defaultdict(list) 

    for i in range(numCourses):
        graph[i] = []

    for a,b in prereqs:
        graph[a].append(b)

    return graph
# Drive code
print(prereqs_possible(numCourses, prereqs))
