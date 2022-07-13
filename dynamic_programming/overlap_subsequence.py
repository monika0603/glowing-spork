""" 
Write a function, overlap_subsequence, that takes in two strings as arguments. The function should 
return the length of the longest overlapping subsequence.

A subsequence of a string can be created by deleting any characters of the string, while maintaining 
the relative order of characters.

With memoization the time complexity of this problem will be O(nm). 
Similarly the space complexity will also O(nm). 

Tip: Avoid any slicing, instead track indices
"""

# Brute force solution, which takes too long for step 4
def overlap_subsequence(s1, s2):
    return _overlap_subsequence(s1, s2, 0, 0) 

def _overlap_subsequence(s1, s2, i, j):
    # i, j are two indices that are the logical start of string 1 and string 2 respectively. 
    # This will help us avoid any string slicing.
    # Base case: if any index i or j is out-of-bounds, meaning strings have become empty
    if i == len(s1) or j == len(s2):
        return 0 
    # If the characters of the string match, then I want to recurssively call the function 
    # with i, j incremented
    if s1[i] == s2[j]:
       return 1 + _overlap_subsequence(s1, s2, i+1, j+1)
    else:
        return max(_overlap_subsequence(s1, s2, i, j+1), _overlap_subsequence(s1, s2, i+1, j))

# Optimized solution with memoization
def overlap_subsequence_optimized(s1, s2):
    return _overlap_subsequence_optimized(s1, s2, 0, 0, {})

def _overlap_subsequence_optimized(s1, s2, i, j, memo):
    key = (i, j)
    if key in memo:
        return memo[key]

    if i == len(s1) or j == len(s2):
        return 0 
    if s1[i] == s2[j]:
        memo[key] = 1 + _overlap_subsequence_optimized(s1, s2, i+1, j+1, memo) 
    else:
        memo[key] = max(_overlap_subsequence_optimized(s1, s2, i, j+1, memo), 
        _overlap_subsequence_optimized(s1, s2, i+1, j, memo))

    return memo[key]

# Driver code
# Test case 01
s1 = "dogs"
s2 = "daogt"
print(overlap_subsequence(s1, s2))

# Test case 02
s1 = "xcyats"
s2 = "criaotsi"
print(overlap_subsequence(s1, s2))

# Test case 03
s1 = "xfeqortsver"
s2 = "feeeuavoeqr"
print(overlap_subsequence(s1, s2))

# Test case 04
s1 = "kinfolklivemustache"
s2 = "bespokekinfolksnackwave"
print(overlap_subsequence_optimized(s1, s2))