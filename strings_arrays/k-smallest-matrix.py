""" 
Problem: Say you have an nxn matrix of elements that are sorted in ascending order both in the 
column and rows of the matrix. Return the kth smallest element of the matrix. For example, 
consider the matrix below:

[1 4 7]
[3 5 9]
[6 8 11]

if k=4, then return 5
"""

grid = [ 
    [1, 4, 7],
    [3, 5, 9],
    [6, 8, 11]
]

import heapq
def smallest(grid, k):

    minHeap = []
    res = []
    for row in range(min(len(grid), k)):
        for col in range(min(len(grid[0]), k)):
            minHeap.append(grid[row][col])
    
    heapq.heapify(minHeap) 
    
    return minHeap[k]

print(smallest(grid, 4))




