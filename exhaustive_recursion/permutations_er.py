"""" 
Write a function, permutations, that takes in a list an argument. The function should return a 2D list 
where each sublist represents one of the possible permutations of the list.

The sublists may be returned in any order.

You may assume that the input list contains unique items.
"""

def permutations(items):
    # Base case, as we shorten our input we get to a point where the len of the 
    # input become zero
    if len(items) == 0:
        return [[]]

    first = items[0] # first = 'a' 
    perm_without_first = permutations(items[1:])

    full_list = [] 
    for perms in perm_without_first:
        for i in range(len(perms)+1):
            full_list.append(perms[:i] + [first] + perms[i:])

    return full_list

# Driver code
# Test case 01
print(permutations(['a', 'b', 'c'])) # -> 
# [ 
#   [ 'a', 'b', 'c' ], 
#   [ 'b', 'a', 'c' ], 
#   [ 'b', 'c', 'a' ], 
#   [ 'a', 'c', 'b' ], 
#   [ 'c', 'a', 'b' ], 
#   [ 'c', 'b', 'a' ] 
# ] 

# Test case 02
print(permutations(['red', 'blue'])) # ->
# [ 
#   [ 'red', 'blue' ], 
#   [ 'blue', 'red' ] 
# ]

# Test case 03
print(permutations([])) # ->
# [
#  [ ]
# ]

# Test case 04
print(permutations([8, 2, 1, 4])) # ->
# [ 
#   [ 8, 2, 1, 4 ], [ 2, 8, 1, 4 ], 
#   [ 2, 1, 8, 4 ], [ 2, 1, 4, 8 ], 
#   [ 8, 1, 2, 4 ], [ 1, 8, 2, 4 ], 
#   [ 1, 2, 8, 4 ], [ 1, 2, 4, 8 ], 
#   [ 8, 1, 4, 2 ], [ 1, 8, 4, 2 ], 
#   [ 1, 4, 8, 2 ], [ 1, 4, 2, 8 ], 
#   [ 8, 2, 4, 1 ], [ 2, 8, 4, 1 ], 
#   [ 2, 4, 8, 1 ], [ 2, 4, 1, 8 ], 
#   [ 8, 4, 2, 1 ], [ 4, 8, 2, 1 ], 
#   [ 4, 2, 8, 1 ], [ 4, 2, 1, 8 ], 
#   [ 8, 4, 1, 2 ], [ 4, 8, 1, 2 ], 
#   [ 4, 1, 8, 2 ], [ 4, 1, 2, 8 ] 
# ] 
