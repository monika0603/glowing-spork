""" 
Write a function, max_path_sum, that takes in a grid as an argument. The function should return 
the maximum sum possible by traveling a path from the top-left corner to the bottom-right corner. 
You may only travel through the grid by moving down or right.

You can assume that all numbers are non-negative.
"""

def max_path_sum(grid):
    r, c = 0, 0 
    return _max_path_sum(grid, r, c, {}) 

def _max_path_sum(grid, r, c, memo):
    pos = (r,c)
    if pos in memo:
        return memo[pos]

    if r == len(grid) or c == len(grid[0]):
        return 0 

    if r == len(grid) - 1 and c == len(grid[0]) - 1:
        return grid[r][c] 

    down = _max_path_sum(grid, r+1, c, memo)
    right = _max_path_sum(grid, r, c+1, memo)

    max_sum = grid[r][c] + max(down, right)
    memo[pos] = max_sum 

    return memo[pos]

# Driver code
# Test case 01
grid = [
  [1, 3, 12],
  [5, 1, 1],
  [3, 6, 1],
]
print(max_path_sum(grid)) # -> 18

# Test case 02
grid = [
  [1, 2, 8,  1],
  [3, 1, 12, 10],
  [4, 0, 6,  3],
]
print(max_path_sum(grid)) # -> 36

# Test case 03
grid = [
  [1, 2, 8, 1],
  [3, 10, 12, 10],
  [4, 0, 6, 3],
]
print(max_path_sum(grid)) # -> 39

