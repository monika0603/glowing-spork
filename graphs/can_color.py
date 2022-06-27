""" 
Write a function, can_color, that takes in a dictionary representing the adjacency list of an 
undirected graph. The function should return a boolean indicating whether or not it is possible 
to color nodes of the graph using two colors in such a way that adjacent nodes are always different colors.

For example, given this graph:

x-y-z

It is possible to color the nodes by using red for x and z, 
then use blue for y. So the answer is True.

For example, given this graph:

    q
   / \
  s - r

It is not possible to color the nodes without making two 
adjacent nodes the same color. So the answer is False.
"""

def can_color(graph):
    # Empty dictionary to begin with, where keys will be the nodes of the graph and 
    # values will be boolean values representing alternating colors. 
    coloring = {} 
    # Iterating through each node in a graph
    for node in graph:
        if node not in coloring:
            if validate(graph, node, coloring, False) == False:
                return False 

    return True 



def validate(graph, node, coloring, current_color):
    # Base case if the node that I am currently visiting has already been visited before 
    # And if the current color that I am assigning is the color that is previously assigned.
    if node in coloring:
        return current_color == coloring[node] 

    # Otherwise the node has not been previously colored, and we should color it 
    coloring[node] = current_color 
    # Now I am visiting all the neighbors of the current node, recursively call the validate function
    # and importantly flip the color using the boolean not 
    for neighbor in graph[node]:
        if validate(graph, neighbor, coloring, not current_color) == False:
            return False 

    return True 

# test case 01:
graph = {
  "x": ["y"],
  "y": ["x","z"],
  "z": ["y"]
}

print(can_color(graph))

# test case 02:
graph = {
  "q": ["r", "s"],
  "r": ["q", "s"],
  "s": ["r", "q"]
} 
print(can_color(graph))

# test case 03:
print(can_color({
  "a": ["b", "c", "d"],
  "b": ["a"],
  "c": ["a"],
  "d": ["a"],
}))

# test case 04:
print(can_color({
  "h": ["i", "k"],
  "i": ["h", "j"],
  "j": ["i", "k"],
  "k": ["h", "j"],
}))