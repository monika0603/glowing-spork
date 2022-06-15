"""_summary_
    Write a function, minimum_island, that takes in a grid containing Ws and Ls. 
    W represents water and L represents land. The function should return the size 
    of the smallest island. An island is a vertically or horizontally connected 
    region of land.

You may assume that the grid contains at least one island.
"""

grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]

def minimum_island(grid):

    # number of rows
    row = len(grid)
    # number of cols
    col = len(grid[0])
    # set variable to check if a position has been visited 
    visited = set()
    # minimum variable set to a max value
    minimum = float("inf")

    # iterating over the row and col position
    for r in range(row):
        for c in range(col):
            # iterative loop to explore every row, col position in the grid
            # exploreSize function returns the count of the island
            count = exploreSize(grid, r, c, visited)
            # Very important! 
            # Since we are returning zero in the helper function if the position has 
            # already been visited or if it is water, it will return 0 as the minimum value 
            # However, we need to return a value only when we actually count an island
            if count > 0:
                minimum = min(minimum, count)

    return minimum


def exploreSize(grid, r, c, visited):
    # Basic checks to ensure we are inbounds of the grid and not calling DFS for water 
    if r <0 or r>=len(grid) or c<0 or c>=len(grid[0]) or grid[r][c] == 'W':
        return 0

    # Creating a variable to store the row, col value of a cell
    pos = str(r) + ',' + str(c)
    # if a position has already been visited then simply return 0 
    if pos in visited:
        return 0 
    
    # Otherwise add it to the set variable. If we don't do it we get stuck in a cycle
    visited.add(pos)

    # Now simply calling dfs on up, down, right and left positions
    count = 1
    count += exploreSize(grid, r-1, c, visited)
    count += exploreSize(grid, r+1, c, visited)
    count += exploreSize(grid, r, c+1, visited)
    count += exploreSize(grid, r, c-1, visited) 

    # return the size of an island
    return count 

print(minimum_island(grid))
    