""" 
Write a function, semesters_required, that takes in a number of courses (n) and a list of 
prerequisites as arguments. Courses have ids ranging from 0 through n - 1. A single prerequisite of 
(A, B) means that course A must be taken before course B. Return the minimum number of semesters 
required to complete all n courses. There is no limit on how many courses you can take in a single 
semester, as long the prerequisites of a course are satisfied before taking it.

Note that given prerequisite (A, B), you cannot take course A and course B concurrently in the 
same semester. You must take A in some semester before B.

You can assume that it is possible to eventually complete all courses.

Algorithm: 

Take in an array representing number of courses. Each pair represents the path required to complete 
a course, meaning (a,b), a must be taken first. 
For a problem like this it is important to note that this is a directed acyclic graph, meaning there 
is no cycle between the nodes. Otherwise if there is a cycle then those courses will require each other. 

Similar to the longest path problem, we are now finding the first courses that require nothing. Meaning 
any nodes that have a length of zero, and assign them a 1, because it will take us at least one semester 
to finish them. 
"""

import collections
from multiprocessing.context import set_spawning_popen
def semesters_required(num_courses, prereqs):

    graph = build_graph(num_courses, prereqs)
    distance = {}
    # Find terminal nodes, meaning courses that don't require any other course to be taken
    for node in graph:
        if len(graph[node]) == 0:
            distance[node] = 1 

    
    # Now we can begin exploring the neighboring nodes
    for node in graph:
        explore(graph, node, distance)

    return max(distance.values())

def explore(graph, node, distance):
    if node in distance:
        return distance[node] 

    semester = 1 
    for neighbor in graph[node]:
        attempt = explore(graph, neighbor, distance)
        semester = max(attempt, semester) 

    distance[node] = 1 + semester
    return distance[node] 

def build_graph(num_courses, prereqs):
    graph = collections.defaultdict(list) 

    for i in range(num_courses):
        graph[i] = [] 

    for a,b in prereqs:
        graph[a].append(b) 

    return graph 


# Driver code
# Test case 01
num_courses = 6
prereqs = [
  (1, 2),
  (2, 4),
  (3, 5),
  (0, 5),
]
print(semesters_required(num_courses, prereqs)) # -> 3

# Test case 02 
num_courses = 7
prereqs = [
  (4, 3),
  (3, 2),
  (2, 1),
  (1, 0),
  (5, 2),
  (5, 6),
]
print(semesters_required(num_courses, prereqs)) # -> 5

# Test case 03
num_courses = 5
prereqs = [
  (1, 0),
  (3, 4),
  (1, 2),
  (3, 2),
]
print(semesters_required(num_courses, prereqs)) # -> 2

# Test case 04
num_courses = 12
prereqs = []
print(semesters_required(num_courses, prereqs)) # -> 1

# Test case 05
num_courses = 3
prereqs = [
  (0, 2),
  (0, 1),
  (1, 2),
]
print(semesters_required(num_courses, prereqs)) # -> 3

# Test case 06
num_courses = 6
prereqs = [
  (3, 4),
  (3, 0),
  (3, 1),
  (3, 2),
  (3, 5),
]
print(semesters_required(num_courses, prereqs)) # -> 2