""" 
Write a function sum_possible that takes in an amount and a list of positive numbers. 
The function should return a boolean indicating whether or not it is possible to create 
the amount by summing numbers of the list. You may reuse numbers of the list as many times 
as necessary.

You may assume that the target amount is non-negative.
"""

def sum_possible(target, numbers):
    return _sum_possible(target, numbers, {}) 

def _sum_possible(target, numbers, memo):

    if target in memo:
        return memo[target]
    if target < 0:
        return False 
    if target == 0:
        return True 

    for num in numbers:
        if _sum_possible(target-num, numbers, memo) == True:
            memo[target] = True
            return memo[target] 

    memo[target] = False 
    return memo[target] 

# Driver code 
# Test case 01
print(sum_possible(8, [5, 12, 4]))

# Test case 02
print(sum_possible(15, [6, 2, 10, 19])) # -> False

# Test case 03
print(sum_possible(103, [6, 20, 1])) # -> True

