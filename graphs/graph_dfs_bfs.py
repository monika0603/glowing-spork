"""_summary_

You are provided a graph as shown here:

       a
    /     \
  b         c
  |         |
  d         e
  |
  f

This algorithm shows DFS and BFS implemented in different ways. The key concept here is that BFS uses 
queue data structure that is built on LIFO concept. We add elements from the end the remove elements from 
front. While in DFS, we use a stack data structure where we add elements from the back AND remove them from
the back. So DFS is built on LIFO. 
"""

graph = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f":[]
}

# First example of BFS implementation
def bfs_traversal(graph):

    # Set variable to keep track of visited elements
    visited = set()
    # Iteration to check for every node
    for neighbor in graph:
        # Recursive function to print a node
        exploreBFS(graph, neighbor, visited)

def exploreBFS(graph, node, visited):
    # Base case if we have already visited a node
    if node in visited:
        return 
    # If not add it to the variable. Very important, otherwise we get stuck in a loop
    visited.add(node)
    # print statement IN A RECURSIVE call makes it a BFS traversal
    print(node)
    # recursive call to the function
    exploreBFS(graph, node, visited)

# Set variable to keep track of visited elements
visited = set()
def dfs(graph, node, visited):
    # Base case if we have already visited a node
    if node in visited:
        return 

    # print statement outside of the recursive call
    print(node)
    # If a node has not been previously visited, then add it to the visited variable
    visited.add(node)
    # Exploring each neighbor 
    for neighbor in graph[node]:
        dfs(graph, neighbor, visited)


# DFS implementation using stack data structure, based on LIFO
def depth_first_print(graph, start):
    # Defining a stack DS
    stack = [] 
    # Append the start node
    stack.append(start)
    # While the length in greater than 0
    while(len(stack) > 0):
        # REMOVE FROM THE LAST
        current = stack.pop() 
        # print statement
        print(current)
        # recursive call to check for neighboring nodes
        for neighbor in graph[current]:
            stack.append(neighbor)

# BFS implementation using stack data structure, based on FIFO
def breadth_first_print(graph, start):
    # Defining a queue DS
    queue = []
    queue.append(start)

    while(len(queue) > 0):
        # Removing from the FRONT of the queue
        current = queue.pop(0)
        # print statement
        print(current)
        # recursive call to check for neighboring nodes
        for neighbor in graph[current]:
            queue.append(neighbor)



# Driver code
print(bfs_traversal(graph))
#print(dfs(graph, "a", visited))
#print( depth_first_print(graph, "a"))
#print(breadth_first_print(graph, "a"))