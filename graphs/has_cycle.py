""" 
Write a function, has_cycle, that takes in an object representing the adjacency list 
of a directed graph. The function should return a boolean indicating whether or not the 
graph contains a cycle.

  a -- > b
   \   /
     c

This is a white-grey-black problem. Where 
 white = unexplored node 
 grey = visiting (in-progress)
 black = fully visited 

 # At first all the nodes begin as white, when we are exploring a given node, we mark it as 
 visiting. Once nodes are explored, they are marked as black. So if we ever visit a node that 
 is grey, that means that we have found a node that we had previously visited and we've found a 
 cycle. 
"""

graph = {
  "a": ["b"],
  "b": ["c"],
  "c": ["a"],
}

def has_cycle(graph):

    # set type variable for marking nodes as grey. 
    # Nodes are literaly marked as grey in this code, however, the logic is that 
    # if any neighboring node is in visiting set, that means I previously visited it 
    # and I am visiting it, so I have found a cycle
    visiting = set() 
    # visited set marks the node as black, meaning no further exploration required
    visited = set()

    # classic code to begin exploring a node
    for node in graph:
        # DFS to check for cycles
        if cycle_detect(graph, node, visiting, visited) == True:
            return True 
    
    return False 

# DFS implementation
def cycle_detect(graph, node, visiting, visited):
    # If a node is already in visited, I don't need to do anything
    if node in visited:
        return False 

    # If a node exists in visiting, then I have found a cycle
    if node in visiting:
        return True 
    # If I get to this part of the code, that means I have to add the node to visiting first
    visiting.add(node) 

    # Being exploring node's neighbor
    for neighbor in graph[node]:
        # if we get returned True in the code above, means that we have found a cycle
        if cycle_detect(graph, neighbor, visiting, visited) == True:
            return True 

    # otherwise remove it from visiting and add it to visited set. Marking it black, so 
    # no futher exploration can be done
    visiting.remove(node)
    visited.add(node)

    # return False by default if none of the statements return true at all
    return False 

# Driver code
print(has_cycle(graph))