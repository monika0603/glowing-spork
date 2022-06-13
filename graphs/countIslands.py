
class Graph:
    def __init__(self, row, col, graph) -> None:
        self.row = row 
        self.col = col 
        self.graph = graph 

    def dfs(self, i, j):
        if i<0 or i>=len(self.graph) or j<0 or j>=len(self.graph[0]) or self.graph[i][j]!=1:
            return  

        # mark as visited
        self.graph[i][j] = -1 

        self.dfs(i-1, j-1)
        self.dfs(i-1, j)
        self.dfs(i-1, j+1)
        self.dfs(i, j-1)
        self.dfs(i, j+1)
        self.dfs(i+1, j-1)
        self.dfs(i+1, j)
        self.dfs(i+1, j+1) 


    def countIslands(self):
        count = 0
        
        for i in range(self.row):
            for j in range(self.col):
                if self.graph[i][j] == 1:
                    count+=1
                    self.dfs(i,j)

        return count

graph = [
    [1, 1, 0, 0, 0],
    [0, 1, 0, 0, 1],
    [1, 0, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1]
]

graph = [
    [1, 1, 0],
    [0, 1, 0],
    [0, 1, 0],
    [1, 1, 1]
]

row = len(graph)
col = len(graph[0])
g = Graph(row, col, graph)
print(g.countIslands())
