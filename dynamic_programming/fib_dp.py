""" 
Write a function fib that takes in a number argument, n, and returns the n-th number of the Fibonacci sequence.

The 0-th number of the sequence is 0.

The 1-st number of the sequence is 1.

To generate further numbers of the sequence, calculate the sum of previous two numbers.

Solve this recursively.

Example: fib(0) -> 0 
"""

def fib(n):
    # Passing an empty dictionary 
    return _fib(n, {})

# Brute force solution: This solution will work for the most part until the input number is very large 
def _fib(n, memo):
    if n in memo:
        return memo[n]

    if n == 0:
        return 0 
    if n == 1:
        return 1 

    memo[n] = _fib(n-1, memo) + _fib(n-2, memo)
    return memo[n] 
    
# Driver code
print(fib(6))

# Using a memoization strategy


