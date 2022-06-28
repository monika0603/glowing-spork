""" 
Write a function sum_possible that takes in an amount and a list of positive numbers. 
The function should return a boolean indicating whether or not it is possible to create 
the amount by summing numbers of the list. You may reuse numbers of the list as many times 
as necessary.

You may assume that the target amount is non-negative.

For example: sum_possible(8, [5, 12, 4]) # -> True, 4 + 4
"""
def sum_possible(amount, numbers):
    return _sum_possible(amount, numbers, {})

def _sum_possible(amount, numbers, memo):
    if amount in memo:
        return memo[amount]

    # Base case if the amount is less than zero
    if amount < 0:
        return False 

    # Another base case if the amount is zero
    if amount == 0:
        return True 

    # Recursive call to calculate the difference between the amount and each number
    for num in numbers:
        if num <= amount:
            if _sum_possible(amount - num, numbers, memo) == True:
                memo[amount] = True 
                return True 

    memo[amount] = False  
    return False 

# Driver code
# Test case 01
print(sum_possible(8, [5,  12, 4]))

# Test case 02
print(sum_possible(15, [6,  2, 10, 19]))

# test case 03
print(sum_possible(13, [6, 2, 1]))