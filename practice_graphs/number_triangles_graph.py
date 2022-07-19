""" 
Problem: Given a list of lists, count the number of triangles if there is a cycle in the nodes. 
"""

import collections
def detect_cycle(edges):

    graph = collections.defaultdict(list)

    for a,b in edges:
        graph[a].append(b) 
        graph[b].append(a) 

    count = 0 
    for x,y in edges:
        for node in graph:
            if x in graph[node] and y in graph[node]:
                count += 1 

    return count//3


edges = [[0,1], [3,0], [0,2], [3,2], [1,2], [4,0], [3,4], [3,5], [4,5], [1,5], [1,3]]
print(detect_cycle(edges))