


graph = {
    'A' : ['C', 'B'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

def bfs(graph, node):
    # base case if node is empty
    if not node:
        return 

    # defining a queue 
    queue = [] 
    # pushing to the queue
    queue.append(node)
    # iterating over the length of the queue
    while(len(queue) > 0):
        # pop from the queue and print
        node = queue.pop(0)
        print(node)

        # iterating over the neighbors
        for nei in graph[node]:
            queue.append(nei)

bfs(graph, 'A')

