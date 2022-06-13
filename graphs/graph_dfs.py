""" 
Depth-first-search for graph algorithms. DFS is a tree-traversal algorithm on graphs 
or for tree data structures. It can be implemented esily using recursion and data 
structures like dictionaries and set. 

The Algorithm:
1. Pick any node. If unvisited, mark it as visited and recur on all its adjacent nodes. 
2. Repeat until all the nodes are visited, or the node to be searched is found. 

Conside this graph, implemented in the code below (arrows are pointing down):

        A 
      /   \
    B       C
   / \       \
  D    E---> F

Time complexity: Since all the nodes and vertices are visited, the average time complexity for 
DFS on a graph is O(V+E), where E is the number of vertices and E is the number of edges. In case 
of DFS on a tree, the time complexity is O(V), where V is the number of nodes. 
"""

graph = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

visited = set() 

def dfs(visited, graph, node):
    if not node in visited:
        print(node)
        visited.add(node)
        for nei in graph[node]:
            dfs(visited, graph, nei)

    return visited

# driver code
dfs(visited, graph, 'A')
