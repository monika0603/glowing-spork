""" 
Write a function, count_paths, that takes in a grid as an argument. In the grid, 
'X' represents walls and 'O' represents open spaces. You may only move down or to 
the right and cannot pass through walls. The function should return the number of 
ways possible to travel from the top-left corner of the grid to the bottom-right corner.

Example: 

           columns
        0       1       2
      0 (0,0)  (0,1)   (0,2)X
  
rows  1 (1,0)  (1,1)   (1,2)

      2 (2,0)  (2,1)   (2,2)
rows increase vertically while the columns increase horizontally. So if we are starting from (0,0) our 
tree would look something like below

                                           (0,0)
                                    /                \
                                (1,0)                (0,1)
                              /       \                |
                           (2,0)      (1,1)          (1,1)
                             |       /      \        /   \
                           (2,1)    (2,1)   (1,2)  (2,1) (1,2)
                             |        |       |     |      |
                           (2,2)    (2,2)   (2,2)  (2,2)  (2,2)

Base case count in this case would be 1 because when we get to (2,2) cell we are already at the cell 
where we want to be. So we should return a count of 1. 
""" 

def count_paths(grid):
    r,c = 0,0
    return _count_path(grid, r, c, {}) 

def _count_path(grid, r, c, memo):
    # Storing the row and column position as a tuple
    pos = (r,c)
    # If the tuple already exists in the memo, then simply return it
    if pos in memo:
        return memo[pos]
    # Base case to not count if we are outside of any cell boundaries
    if r == len(grid) or c == len(grid[0]) or grid[r][c] == 'X':
        return 0 
    # If I am already at the bottom right corner then return 1 
    if r == len(grid)-1 and c == len(grid[0])-1:
        return 1 

    down_count = _count_path(grid, r+1, c, memo)
    right_count = _count_path(grid, r, c+1, memo)
    # Otherwise store the information in the memo
    memo[pos] = down_count + right_count
    return memo[pos]

# Driver code
# Test case 01 
grid = [ 
    ["0", "0"],
    ["0", "0"]
]
print(count_paths(grid))

# Test case 02
grid = [
  ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
  ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
  ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
  ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
  ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
  ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
  ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
  ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
  ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
  ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
  ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
  ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
  ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
  ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
  ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
]
print(count_paths(grid))
    