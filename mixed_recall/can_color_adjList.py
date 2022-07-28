"""" 
Write a function, can_color, that takes in a dictionary representing the adjacency list of 
an undirected graph. The function should return a boolean indicating whether or not it is 
possible to color nodes of the graph using two colors in such a way that adjacent nodes 
are always different colors.

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

However, for a problem like below the answer will be True because it is possible to color all the nodes
alternatively. 

  a --- b 
  |     |
  |     |
  c --- d

Important: So a simple cycle detection won't help solve this problem. 
"""

def can_color(graph):
    # Empty dictionary which will have nodes as the keys and boolean values as 
    # its values 
    coloring = {}
    # Begin a traversal at any node
    # Passing the current color of the node which is False by default
    # Here instead of passing a visited set, we will use coloring hashmap to check 
    # if we have not already visited the node
    for node in graph:
        if node not in coloring and validate(graph, node, coloring, False) == False:
            return False 

    return True 


def validate(graph, node, coloring, current_color):
    # Base case 
    # Check if the current color is equal to the previously assigned color 
    # If not return False because graph is not bipartite anymore.
    if node in coloring:
        return current_color == coloring[node] 

    coloring[node] = current_color 

    # Now recurssively call the function validate and assign every node an 
    # alternative color. Using the recurssive leap of faith, if the below call 
    # returns a False then we simply return False. If I can't color a region 
    # of the graph, the graph is not bipartite
    for neighbor in graph[node]:
        if validate(graph, neighbor, coloring, not current_color) == False:
            return False 

    return True 

# Driver code
# Test case 01 
print(can_color({
  "x": ["y"],
  "y": ["x","z"],
  "z": ["y"]
})) # -> True 

# Test case 02
print(can_color({
  "q": ["r", "s"],
  "r": ["q", "s"],
  "s": ["r", "q"]
})) # -> False

# Test case 03
print(can_color({
  "a": ["b", "c", "d"],
  "b": ["a"],
  "c": ["a"],
  "d": ["a"],
})) # -> True

# Test case 04
print(can_color({
  "a": ["b", "c", "d"],
  "b": ["a"],
  "c": ["a", "d"],
  "d": ["a", "c"],
})) # -> False

# Test case 05
print(can_color({
  "h": ["i", "k"],
  "i": ["h", "j"],
  "j": ["i", "k"],
  "k": ["h", "j"],
})) # -> True

# Test case 06
print(can_color({
  "z": []
})) # -> True

# Test case 07
print(can_color({
  "h": ["i", "k"],
  "i": ["h", "j"],
  "j": ["i", "k"],
  "k": ["h", "j"],
  "q": ["r", "s"],
  "r": ["q", "s"],
  "s": ["r", "q"]
})) # -> False