""" 
Write a function, semesters_required, that takes in a number of courses (n) and a 
list of prerequisites as arguments. Courses have ids ranging from 0 through n - 1. 
A single prerequisite of (A, B) means that course A must be taken before course B. 
Return the minimum number of semesters required to complete all n courses. There 
is no limit on how many courses you can take in a single semester, as long the 
prerequisites of a course are satisfied before taking it.

Note that given prerequisite (A, B), you cannot take course A and course B concurrently 
in the same semester. You must take A in some semester before B.

You can assume that it is possible to eventually complete all courses.

The problem can be visualized as below:

1 -- > 2 -- > 4 : courses 1 and 2 must be taken before 4 
3 -- > 5 : courses 3 and 0 must be taken before 5  
      /
    0

Very important: This is a DIRECTED ACYCLIC GRAPH type problem, where there are no cycles. 
"""

num_courses = 6
prereqs = [
  (1, 2),
  (2, 4),
  (3, 5),
  (0, 5),
]

import collections 

def semesters_required(num_courses, prereqs):
    # helper function to create an adjacency list
    graph = build_graph(num_courses, prereqs)
    
    # New dictionary to keep track of the distance/semesters required
    distance = {}
    # Step to identify terminal nodes
    for node in graph:
        # If I find a terminal node, then I assign 1 to it 
        # because I will need atleast one semester to complete that course
        if len(graph[node]) == 0:
            distance[node] = 1 
    
    # Once terminal nodes have been found I need to traverse through each 
    # node to identify the longest path (or the number of semesters requires)
    for node in graph:
        # DFS to traverse through each node
        traverse_nodes(graph, node, distance)

    print(distance)
    # return the maximum value of values in distance dictionary
    return max(distance.values())

def traverse_nodes(graph, current, distance):
    # Base case
    if current in distance:
        return distance[current]

    # Starting the terminal nodes with a distance of 1
    semester = 1
    for neighbor in graph[current]:
        # recursive call 
        attempt = traverse_nodes(graph, neighbor, distance)
        # selecting the maximum 
        semester = max(semester, attempt) 

    # Incrementing distance by 1 for each node
    distance[current] = 1 + semester

    # returning the distance
    return distance[current]


def build_graph(num_courses, prereqs):
    # Creating a graph dictionary with list as values 
    graph = collections.defaultdict(list)

    # Looping over number of courses because key in our dictionary should be for every course 
    # This is an important to determine terminal nodes in our graph
    for course in range(num_courses):
        graph[course] = [] 

    # Since this is a DAG type problem, we only append in the direction of the required 
    # courses. We don't do graph[y].append(x)
    for x,y in prereqs:
        graph[x].append(y) 

    return graph 




print(semesters_required(num_courses, prereqs))
