""" 
Write a function fib that takes in a number argument, n, and returns the n-th number of the Fibonacci sequence.

The 0-th number of the sequence is 0.

The 1-st number of the sequence is 1.

To generate further numbers of the sequence, calculate the sum of previous two numbers.

Solve this recursively.
"""

def fib(num):
    return _fib(num, {}) 

def _fib(num, memo):
    if num in memo:
        return memo[num]

    if num == 0:
        return 0 

    if num == 1:
        return 1 

    memo[num] = _fib(num-1, memo) + _fib(num-2, memo)
    return memo[num]

# Driver code
# Test case 01
print(fib(0))

# Test case 1
print(fib(1))

# Test case 2
print(fib(2))

# Test case 3
print(fib(3))

# Test case 4
print(fib(5))