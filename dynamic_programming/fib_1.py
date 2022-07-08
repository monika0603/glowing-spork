""" 
Write a function fib that takes in a number argument, n, and returns the n-th number of 
the Fibonacci sequence.

The 0-th number of the sequence is 0.

The 1-st number of the sequence is 1.

To generate further numbers of the sequence, calculate the sum of previous two numbers.

Solve this recursively.

Fibonacci sequence: 
index:    0 1 2 3 4 5 6 7  8
sequence: 0 1 1 2 3 5 8 13 21

so fib(6) --> 8
   fib(6) = fib(5) + fib(4)
   fib(n) = fib(n-1) + fib(n-2)
 
                  6
                /   \
               5     4 
              / \   / \
             4   3 3   2
            / \  
           3   2 
          / \
         2   1
        /\
       1  0    
return values of bottom nodes will be 1 or 0. Let's focus on the left most node of 2 which will be adding it's 
children of 0 and 1. Node 2 represents the 2 index, with an output of 1 because 0+1 = 1 (sum of it's children). 
This pattern continues recursivvely until the top of the root of the tree is reached. 

Time complexity: Typically time complexity of a recursive call is O(2^n).
"""

def fib_bf(n):

    if n == 0:
        return 0 
    if n == 1:
        return 1 

    # Brute force solution without using memoization
    return fib(n-1) + fib(n-2)

# driver code
# Takes 2001 ms
print(fib_bf(36))

# Instead of using a brute-force solution we use memoization using dictionary in python. This basically keeps 
# track of the nodes that have been previously calculated. Without having to repeat calculations. 
def fib(n):
    return _fib(n, {})

def _fib(n, memo):
    # We need to store information inside of the memo. 
    # Keys of the memo will be n and values will be return value of that node
    # Where n basically represents the index of the fibonacci sequence.
    # If n is in memo, then simply return the stored value of that key
    if n in memo:
        return memo[n]

    if n == 0:
        return 0 
    if n == 1:
        return 1 
    
    # So now first we are calculating n-1 and n-2 and storing it in the memo. 
    memo[n] = _fib(n-1, memo) + _fib(n-2, memo)
    # Now finally returning the memo itself. This prevents recalculations of the nodes during a recursive call. 
    return memo[n]


