""" 
Write a function tribonacci that takes in a number argument, n, and returns the n-th number of the 
Tribonacci sequence.

The 0-th and 1-st numbers of the sequence are both 0.

The 2-nd number of the sequence is 1.

To generate further numbers of the sequence, calculate the sum of previous three numbers.

Solve this recursively.
"""

def trib(num):
    return _trib(num, {}) 

def _trib(num, memo):
    if num in memo:
        return memo[num]

    if num == 0:
        return 0 
    if num == 1:
        return 0 
    if num == 2:
        return 1 

    memo[num] = _trib(num-1, memo) + _trib(num-2, memo) + _trib(num-3, memo)
    return memo[num]

# Driver code 
# Test case 01
print(trib(5))

# Test case 02
print(trib(7))