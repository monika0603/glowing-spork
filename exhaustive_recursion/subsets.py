""" 
Write a function, subsets, that takes in a list as an argument. The function should return a 2D list where 
each sublist represents one of the possible subsets of the list.

The elements within the subsets and the subsets themselves may be returned in any order.

You may assume that the input list contains unique elements.

"""

def subset(elements):
    # returning one subset which contains no combinations
    if len(elements) == 0:
        return [[]] 

    first = elements[0] # First = 'a'
    subs_without_first = subset(elements[1:])
    
    subs_with_first = []
    for sub in subs_without_first:
        subs_with_first.append([first, *sub])

    return subs_without_first + subs_with_first

# Driver code
# Test case 01
print(subset(['a', 'b'])) # ->
# [ 
#   [], 
#   [ 'b' ], 
#   [ 'a' ], 
#   [ 'a', 'b' ] 
# ]

# Test case 02
print(subset(['a', 'b', 'c'])) # ->
# [
#   [],
#   [ 'c' ],
#   [ 'b' ],
#   [ 'b', 'c' ],
#   [ 'a' ],
#   [ 'a', 'c' ],
#   [ 'a', 'b' ],
#   [ 'a', 'b', 'c' ]
# ]
