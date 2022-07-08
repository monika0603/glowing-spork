""" 
Write a function min_change that takes in an amount and a list of coins. The function should 
return the minimum number of coins required to create the amount. You may use each coin as 
many times as necessary.

If it is not possible to create the amount, then return -1.

Example: min_change(8, [1, 5, 4, 12]) # -> 2, because 4+4 is the minimum coins possible
"""

# Brute force solution
def min_change(amount, coins):
    if amount == 0:
        return 0 
    if amount < 0:
        return float("inf") 

    min_coins = float("inf")
    for coin in coins:
        num_coins = 1 + min_change(amount-coin, coins)
        min_coins = min(min_coins, num_coins) 

    return min_coins

# Driver code 
# Test case 01
amount = 8 
coins = [1,5,4,12]
print(min_change(amount, coins)) 

# Test case 02 
# Recursive call would take too long for the below test case 
amount = 271
coins = [10, 8, 265, 24]
#print(min_change(amount, coins))

# Optimized solution using memoization
def min_change_optimized(amount, coins):
    return _min_change(amount, coins, {})

def _min_change(amount, coins, memo):

    if amount in memo:
        return memo[amount]
    if amount == 0:
        return 0 
    if amount < 0:
        return float("-inf")

    min_coins = float("inf")
    for coin in coins:
        num_coins = 1 + _min_change(amount-coin, coins, memo)
        min_coins = min(min_coins, num_coins) 

    memo[amount] = min_coins
    return min_coins

# Test case 02 
# 
amount = 271
coins = [10, 8, 265, 24]
print(min_change_optimized(amount, coins))