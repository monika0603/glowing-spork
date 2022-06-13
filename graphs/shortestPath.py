"""
summary:
The graph we are provided is acyclic. There are two solutions implemented here. DFS (hasPath) 
and BFS (hasPath_BFS). This solution, however, does not provide a shortest path from source 
to destination. Instead, it provides a simple implementation of whether or not there exists a 
path from source to destination. 

Returns:
        type: Boolean value 
"""


graph = {
    'f' : ['g','i'],
    'g' : ['h'],
    'h' : [],
    'i' : ['g', 'k'],
    'j' : ['i'],
    'k' : []
}

def hasPath_BFS(graph, source, destination):
    # base case 
    if not source and not destination:
        return 

    queue = []
    queue.append(source)

    while(len(queue) > 0):
        node = queue.pop(0)
        print(node)
        # will return true if the current node is equal to the destination
        if node == destination:
            return True 
        # if not, we need to continue to look at the neighbors 
        for nei in graph[node]:
            queue.append(nei)

    # In case there is no path between the source and the destination then after our queue becomes 
    # and there is still no path found, then we must return false 
    return False 


def hasPath(graph, source, destination):
    # base case
    print(source)
    if source == destination:
        return True 
    
    for nei in graph[source]:
        # Check if the recursive call returns true or not 
        if hasPath(graph, nei, destination) == True:
            return True 

    # default case of returning false if we never find a path 
    return False 

source = 'f'
destination = 'k'

#print(hasPath(graph, source, destination))
print(hasPath_BFS(graph, source, destination))