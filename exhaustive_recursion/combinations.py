""" 
Write a function, create_combinations, that takes in a list and a length as arguments. The 
function should return a 2D list representing all of the combinations of the specifized length.

The items within the combinations and the combinations themselves may be returned in any order.

You may assume that the input list contains unique elements and 1 <= k <= len(items).
"""
def create_combinations(items, k):
    # Base cases 
    # if k == 0, return [[]] 
    # if k > len(items), return [] 

    if k == 0:
        return [[]]
    if k > len(items):
        return [] 

    first = items[0]
    partial_combos = create_combinations(items[1:], k - 1)

    combos_with_first = [] 

    for comb in partial_combos:
        combos_with_first.append([first, *comb]) 

    combos_without_first = create_combinations(items[1:], k) 

    return combos_without_first + combos_with_first

# Driver code
# Test case 01
print(create_combinations(["a", "b", "c"], 2)); # ->
# [
#   [ 'a', 'b' ],
#   [ 'a', 'c' ],
#   [ 'b', 'c' ]
# ]

# Test case 02
print(create_combinations(["q", "r", "s", "t"], 2)); # ->
# [
#   [ 'q', 'r' ],
#   [ 'q', 's' ],
#   [ 'q', 't' ],
#   [ 'r', 's' ],
#   [ 'r', 't' ],
#   [ 's', 't' ]
# ]

print(create_combinations([1, 28, 94], 3)); # ->
# [
#   [ 1, 28, 94 ]
# ]