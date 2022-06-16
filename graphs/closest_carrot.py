""" 
Write a function, closest_carrot, that takes in a grid, a starting row, 
and a starting column. In the grid, 'X's are walls, 'O's are open spaces, 
and 'C's are carrots. The function should return a number representing the 
length of the shortest path from the starting position to a carrot. You may 
move up, down, left, or right, but cannot pass through walls (X). If there 
is no possible path to a carrot, then return -1.

Approach: Whenever a problem requires closest/shortest path we want to BFS. 
"""

grid = [
  ['O', 'O', 'O', 'O', 'O'],
  ['O', 'X', 'O', 'O', 'O'],
  ['O', 'X', 'X', 'O', 'O'],
  ['O', 'X', 'C', 'O', 'O'],
  ['O', 'X', 'X', 'O', 'O'],
  ['C', 'O', 'O', 'O', 'O'],
]

grid = [
  ['O', 'O', 'O', 'O', 'O'],
  ['O', 'X', 'O', 'O', 'O'],
  ['O', 'X', 'X', 'O', 'O'],
  ['O', 'X', 'C', 'O', 'O'],
  ['O', 'X', 'X', 'O', 'O'],
  ['C', 'O', 'O', 'O', 'O'],
]

def closest_carrot(grid, r, c):

    # defining a queue DS
    queue = []
    # appending row, col, distance as a tuple into the queue
    queue.append((r,c,0))
    # set variable defined to ensure we don't get stuck in a loop
    visited = set()
    # adding the input row and col into visited set
    visited.add((r,c)) 

    # Loop lasts as long as their cell added in the queue
    while(len(queue) > 0):
        # Very important! We pop the FIRST element from the queue
        row, col, distance = queue.pop(0)

        # Base case if cell contains the carrot we are looking for
        if grid[row][col] == 'C':
            return distance 

        # (row-1, col) ==> up ==> (-1,0)
        # (row+1, col) ==> down ==> (1,0)
        # (row, col+1) ==> right ==> (0,1)
        # (row, col-1) ==> left  ==> (0,-1)
        deltas = [(-1,0), (1,0), (0,1), (0,-1)]
        # loop allows to look in all four directions at once
        for delta in deltas:
            dx, dy = delta 
            # new cell row = row + dy
            neighbor_row = row + dy 
            # new cell col = col + dx
            neighbor_col = col + dx 
            # check if the cell is inbound
            if (neighbor_row>=0 and neighbor_row<len(grid) 
                and neighbor_col>=0 and neighbor_col<len(grid[0]) 
                and grid[neighbor_row][neighbor_col] != 'X'):
                # if the cell is inbound and cell does not contain a wall, then create a new tuple of 
                # row, col to add to the visited set
                pos = (neighbor_row, neighbor_col)
                # if the cell has not been previously added
                if pos not in visited:
                    # add it
                    visited.add(pos)
                    # append row, col to the queue and increase the distance
                    queue.append((neighbor_row, neighbor_col, distance+1))
    
    # Base case if there is no carrot ever found
    return -1 


# Driver code 
#print(closest_carrot(grid, 1, 2))
print(closest_carrot(grid, 0, 0))