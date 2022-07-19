""" 
Write a function, count_paths, that takes in a grid as an argument. In the grid, 'X' 
represents walls and 'O' represents open spaces. You may only move down or to the 
right and cannot pass through walls. The function should return the number of ways 
possible to travel from the top-left corner of the grid to the bottom-right corner.
"""

def count_paths(grid):
    r, c = 0, 0
    return _count_paths(grid, r, c, {}) 

def _count_paths(grid, r, c, memo):
    pos = (r, c)
    if pos in memo:
        return memo[pos]

    if r == len(grid) or c == len(grid[0]) or grid[r][c] == 'X':
        return 0 

    if r == len(grid)-1 and c == len(grid[0])-1:
        return 1 

    down = _count_paths(grid, r+1, c, memo)
    right = _count_paths(grid, r, c+1, memo)

    memo[pos] = down + right 
    return memo[pos]

# Driver code 
# Test case 01 
grid = [
  ["O", "O"],
  ["O", "O"],
]
print(count_paths(grid)) # -> 2

# Test case 02 
grid = [
  ["O", "O", "X"],
  ["O", "O", "O"],
  ["O", "O", "O"],
]
print(count_paths(grid)) # -> 5

# Test case 03
grid = [
  ["O", "O", "O"],
  ["O", "O", "X"],
  ["O", "O", "O"],
]
print(count_paths(grid)) # -> 3

# Test case 04
grid = [
  ["O", "O", "O"],
  ["O", "X", "X"],
  ["O", "O", "O"],
]
print(count_paths(grid)) # -> 1