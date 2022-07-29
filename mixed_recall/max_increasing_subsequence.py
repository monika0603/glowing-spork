""" 
Write a function, max_increasing_subseq, that takes in a list of numbers as an argument. The 
function should return the length of the longest subsequence of strictly increasing numbers.

A subsequence of a list can be created by deleting any items of the list, while maintaining 
the relative order of items.
"""

def max_increasing_subseq(numbers):
    return _max_increasing_subsequence(numbers, 0, float("-inf"), {}) 


def _max_increasing_subsequence(numbers, i, previous, memo):
    # Anything that changes becomes a key for our memo dictionary
    key = (i, previous)
    if key in memo:
        return memo[key] 
    # Base case if the index becomes equal to the length
    if i == len(numbers):
        return 0 

    # Start my extracting the current number
    current = numbers[i] 
    options = []
    # if you don't take the current number then your previous number doesn't change
    dont_take_current = _max_increasing_subsequence(numbers, i+1, previous, memo) 
    options.append(dont_take_current)
    # Important logic to implement to check if the previous is less than the current number
    if current > previous:
        take_current = 1 + _max_increasing_subsequence(numbers, i+1, current, memo)
        options.append(take_current) 

    # Whatever gets returned in the function gets stored in the memo dictionary
    memo[key] =  max(options)
    return memo[key]

# Driver code
# Test case 01 
numbers = [4, 18, 20, 10, 12, 15, 19]
print(max_increasing_subseq(numbers)) # -> 5 

# Test case 02
numbers = [12, 9, 2, 5, 4, 32, 90, 20]
print(max_increasing_subseq(numbers)) # -> 4

# Test case 03
numbers = [42, 50, 51, 60, 55, 70, 4, 5, 70]
print(max_increasing_subseq(numbers)) # -> 5 

# Test case 04
numbers = [7, 14, 10, 12]
print(max_increasing_subseq(numbers)) # -> 3 

# Test case 05
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
print(max_increasing_subseq(numbers)) # -> 21 

# Test case 06
numbers = [
  1, 2, 3, 4, 5, 12, 6, 30, 7, 8, 9, 10, 11, 12, 13, 10, 18, 14, 15, 16, 17, 18, 19, 20, 21, 100,
  104,
]
print(max_increasing_subseq(numbers)) # -> 23

# Test case 07
numbers = [
  1, 2, 300, 3, 4, 305, 5, 12, 6, 30, 7, 8, 9, 10, 10, 10, 15, 11, 12, 13, 10, 18, 14, 15, 16,
  17, 18, 19, 20, 21, 100,101 ,102, 103, 104, 105
]
print(max_increasing_subseq(numbers)) # -> 27