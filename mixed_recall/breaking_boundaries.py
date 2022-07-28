""" 
Write a function, breaking_boundaries, that takes in 5 arguments: a number of rows (m), 
a number of columns (n), a number of moves (k), a starting row (r), and a starting column (c). 
Say you were situated in a grid with dimensions m * n. If you had to start at position (r,c), 
in how many different ways could you move out of bounds if you could take at most k moves. 
A single move is moving one space up, down, left, or right. During a path you may revisit 
a position.

For example:
3, 4, 2, 0, 0

This input asks us to count the numbers of ways
to move out of bounds in a 3 by 4 grid, starting at
position (0, 0) if we could take at most 2 moves.

The answer is 4 because of these 4 distinct ways:
 1. left
 2. up
 3. right, up
 4. down, left
"""

def breaking_boundaries(m, n, k, r, c):
    return _breaking_boundaries(m, n, k, r, c, {})


def _breaking_boundaries(m, n, k, r, c, memo):
    key = (k,r,c)
    if key in memo:
        return memo[key]

    row_inbounds = 0 <= r < m 
    col_inbounds = 0 <= c < n 

    if not row_inbounds or not col_inbounds:
        return 1 
    
    if k == 0:
        return 0 

    total_count = 0
    deltas = [(-1,0), (1,0), (0,1), (0,-1)]
    for delta in deltas:
        dx, dy = delta 
        total_count += _breaking_boundaries(m, n, k-1, r+dx, c+dy, memo)
        memo[key] = total_count 

    return total_count 

# Driver code
# Test case 01
print(breaking_boundaries(3, 4, 2, 0, 0)) # -> 4

# Test case 02
print(breaking_boundaries(2, 2, 2, 1, 1)) # -> 6

# Test case 03
print(breaking_boundaries(3, 4, 3, 0, 0)) # -> 11

# Test case 04
print(breaking_boundaries(4, 4, 5, 2, 1)) # -> 160

# Test case 05
print(breaking_boundaries(5, 6, 9, 2, 5)) # -> 11635

# Test case 06 
print(breaking_boundaries(6, 6, 12, 3, 4)) # -> 871065

# Test case 07
print(breaking_boundaries(6, 6, 15, 3, 4)) # -> 40787896

# Test case 08
print(breaking_boundaries(6, 8, 16, 2, 1)) # -> 137495089