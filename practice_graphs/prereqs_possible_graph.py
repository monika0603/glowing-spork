""" 
Write a function, prereqs_possible, that takes in a number of courses (n) and 
prerequisites as arguments. Courses have ids ranging from 0 through n - 1. A 
single prerequisite of (A, B) means that course A must be taken before course B. 
The function should return a boolean indicating whether or not it is possible to 
complete all courses.
"""

import collections
def prereqs_possible(numCourses, prereqs):

    graph = build_graph(numCourses, prereqs) 

    visiting = set()
    visited = set() 
    # If we detect a cycle in the course prerequisites, then it is not possible to 
    # complete all the courses. So if we our helper function returns True, then 
    # we have detected a cycle. 
    for node in graph:
        if explore(graph, node, visiting, visited) == True:
            return False

    return False 

def explore(graph, node, visiting, visited):
    if node in visited:
        return False 

    if node in visiting:
        return True 

    visiting.add(node) 

    for neighbor in graph[node]:
        if explore(graph, neighbor, visiting, visited) == True:
            return True 

    visiting.remove(node)
    visited.add(node) 

    return False 
    


def build_graph(numCourses, prereqs):

    graph = collections.defaultdict(list)

    for i in range(numCourses):
        graph[i] = [] 

    for a,b in prereqs:
        graph[a].append(b) 

    return graph 


numCourses = 6
prereqs = [
  (0, 1),
  (2, 3),
  (0, 2),
  (1, 3),
  (4, 5),
]
print(prereqs_possible(numCourses, prereqs)) # -> True