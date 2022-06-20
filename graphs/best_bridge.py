""" 
Write a function, best_bridge, that takes in a grid as an argument. 
The grid contains water (W) and land (L). There are exactly two islands 
in the grid. An island is a vertically or horizontally connected region 
of land. Return the minimum length bridge needed to connect the two islands. 
A bridge does not need to form a straight line.

Algorithm: The idea here is to identify the first main island using DFS and then 
call BFS to calculate the shortest distance
"""

grid = [
  ["W", "W", "W", "L", "L"],
  ["L", "L", "W", "W", "L"],
  ["L", "L", "L", "W", "L"],
  ["W", "L", "W", "W", "W"],
  ["W", "W", "W", "W", "W"],
  ["W", "W", "W", "W", "W"],
]

def best_bridge(grid):
  
  # Getting number of rows in the grid
  row = len(grid)
  # Getting number of cols in the grid
  col = len(grid[0]) 

  # Initializing main_island to None
  main_island = None 
  # Looping over the number of rows and cols
  for i in range(row):
    for j in range(col):
      # DFS to identify the first island
      potential_island = traverse_island(grid, i, j, set())

      if len(potential_island) > 0:
        main_island = potential_island
        break  

  # Creates a copy of the main_island and put it a in a new set variable
  visited = set(main_island)
  queue = [] 
  # Code block to append row, col position in the queue
  # Queue will already have all the position of the main island. 
  for pos in main_island:
    r, c = pos 
    queue.append((r,c,0))

  # Classic BFS algorithm
  while(len(queue) > 0):
    # Poping from the front of the queue
    r, c, distance = queue.pop(0)

    # Checking of we haven't found a new cell with land and the positions don't exist 
    # in the main_island. Otherwise we will get stuck in a loop
    if grid[r][c] == 'L' and (r,c) not in main_island:
      return distance - 1

    # Iterating over the neighbors 
    deltas = [(-1,0), (1,0), (0,1), (0,-1)]
    for delta in deltas:
      x, y = delta 
      dx = r + x
      dy = c + y 
      # if the neighbors are inbounds and they are not added in visited set yet 
      if is_inbounds(grid, dx, dy) and (dx, dy) not in visited:
        # add them to the visited set
        visited.add((dx,dy))
        # also append them to the queue and increment the distance
        queue.append((dx, dy, distance+1))

# Code block to check if a cell is in bounds
def is_inbounds(grid, r, c):
  row_inbounds = 0 <= r < len(grid)
  col_inbounds = 0 <= c < len(grid[0])

  return row_inbounds and col_inbounds 

# Classic DFS logic to check if neighboring cells are land 
def traverse_island(grid, row, col, visited):
  if not is_inbounds(grid, row, col) or grid[row][col] == 'W':
    return visited 

  pos = (row, col)
  if pos in visited:
    return visited 
  visited.add(pos) 

  traverse_island(grid, row-1, col, visited)
  traverse_island(grid, row+1, col, visited)
  traverse_island(grid, row, col+1, visited)
  traverse_island(grid, row, col-1, visited)

  return visited 



  

  



print(best_bridge(grid))



