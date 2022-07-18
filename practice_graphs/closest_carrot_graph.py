""" 
Write a function, closest_carrot, that takes in a grid, a starting row, and a starting column. 
In the grid, 'X's are walls, 'O's are open spaces, and 'C's are carrots. The function should 
return a number representing the length of the shortest path from the starting position to a 
carrot. You may move up, down, left, or right, but cannot pass through walls (X). If there is 
no possible path to a carrot, then return -1.
"""

def closest_carrot(grid, r, c):

    visited = set()
    pos = (r, c, 0)
    queue = []
    queue.append(pos)
    visited.add((r,c)) 

    while queue:
        row, col, distance = queue.pop(0)

        if grid[row][col] == 'C':
            return distance 

        deltas = [(-1,0), (1,0), (0,1), (0,-1)]
        for delta in deltas:
            dx, dy = delta 

            neighbor_row = row + dx 
            neighbor_col = col + dy 

            if (neighbor_row >= 0 and neighbor_row < len(grid) 
               and neighbor_col >= 0 and neighbor_col < len(grid[0]) 
               and grid[neighbor_row][neighbor_col] != 'X'):
               position = (neighbor_row, neighbor_col)
               if position not in visited:
                   visited.add(position)
                   queue.append((neighbor_row, neighbor_col, distance+1))

    return -1

# Driver code
# Test case 01    
grid = [
  ['O', 'O', 'O', 'O', 'O'],
  ['O', 'X', 'O', 'O', 'O'],
  ['O', 'X', 'X', 'O', 'O'],
  ['O', 'X', 'C', 'O', 'O'],
  ['O', 'X', 'X', 'O', 'O'],
  ['C', 'O', 'O', 'O', 'O'],
]

print(closest_carrot(grid, 1, 2)) # --> 4

# Test 02 
grid = [
  ['O', 'O', 'O', 'O', 'O'],
  ['O', 'X', 'O', 'O', 'O'],
  ['O', 'X', 'X', 'O', 'O'],
  ['O', 'X', 'C', 'O', 'O'],
  ['O', 'X', 'X', 'O', 'O'],
  ['C', 'O', 'O', 'O', 'O'],
]

print(closest_carrot(grid, 0, 0)) # -> 5

# Test 03
grid = [
  ['O', 'O', 'X', 'X', 'X'],
  ['O', 'X', 'X', 'X', 'C'],
  ['O', 'X', 'O', 'X', 'X'],
  ['O', 'O', 'O', 'O', 'O'],
  ['O', 'X', 'X', 'X', 'X'],
  ['O', 'O', 'O', 'O', 'O'],
  ['O', 'O', 'C', 'O', 'O'],
  ['O', 'O', 'O', 'O', 'O'],
]

print(closest_carrot(grid, 3, 4)) # -> 9

# Test case 04
grid = [
  ['O', 'O', 'X', 'O', 'O'],
  ['O', 'X', 'X', 'X', 'O'],
  ['O', 'X', 'C', 'C', 'O'],
]

print(closest_carrot(grid, 1, 4)) # -> 2

# Test case 05
grid = [
  ['O', 'O', 'X', 'O', 'O'],
  ['O', 'X', 'X', 'X', 'O'],
  ['O', 'X', 'C', 'C', 'O'],
]

print(closest_carrot(grid, 2, 0)) # -> -1

# Test case 06
grid = [
  ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
  ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
  ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
  ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
  ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
  ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
  ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
  ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
  ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
  ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
  ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'X'],
  ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'C'],
]

print(closest_carrot(grid, 0, 0)) # -> -1