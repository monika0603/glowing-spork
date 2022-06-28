""" 
Write a function tribonacci that takes in a number argument, n, and returns the n-th number of 
the Tribonacci sequence.

The 0-th and 1-st numbers of the sequence are both 0.

The 2-nd number of the sequence is 1.

To generate further numbers of the sequence, calculate the sum of previous three numbers.

Solve this recursively.
"""
def tribonacci(n):
  return _trinonacci(n, {})
  
def _trinonacci(n, memo):
  if n in memo:
    return memo[n] 
  
  if n == 0 or n == 1:
    return 0 
  if n == 2:
    return 1 
  
  
  memo[n] = _trinonacci(n-1, memo) + _trinonacci(n-2, memo) + _trinonacci(n-3, memo)
  return memo[n]

# Test case 01
print(tribonacci(0)) # -> 0

# Test case 02
print(tribonacci(1)) # -> 0

# Test case 03
print(tribonacci(2)) # -> 1

# Test case 04
print(tribonacci(5)) # -> 4

# Test case 05
print(tribonacci(7)) # -> 13

# Test case 06
print(tribonacci(14)) # -> 927