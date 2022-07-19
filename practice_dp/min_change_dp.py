""" 
Write a function min_change that takes in an amount and a list of coins. The function should 
return the minimum number of coins required to create the amount. You may use each coin as many 
times as necessary.

If it is not possible to create the amount, then return -1.
"""

def min_change(target, numbers):
    return _min_change(target, numbers, {}) 

def _min_change(target, numbers, memo):
    if target in memo:
        return memo[target]

    if target < 0:
        return float("inf") 

    if target == 0:
        return 0 

    min_change = float("inf")
    for num in numbers:
        change = 1 + _min_change(target-num, numbers, memo)
        min_change = min(change, min_change) 

    memo[target] = min_change
    return memo[target]

# Driver code 
# Test case 01
print(min_change(8, [1, 5, 4, 12]))

# Test case 02
print(min_change(13, [1, 9, 5, 14, 30])) # -> 5

# test case 03
print(min_change(23, [2, 5, 7])) # -> 4

# Test case 04
print(min_change(102, [1, 5, 10, 25])) # -> 6