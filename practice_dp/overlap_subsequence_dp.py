""" 
Write a function, overlap_subsequence, that takes in two strings as arguments. The function should 
return the length of the longest overlapping subsequence.

A subsequence of a string can be created by deleting any characters of the string, while maintaining 
the relative order of characters.
"""
# Brute force solution
def overlap_subsequence(s1, s2):
    return _max_overlap(s1, s2, 0, 0)

def _max_overlap(s1, s2, i, j):

    if i == len(s1) or j == len(s2):
        return 0 

    if s1[i] == s2[j]:
        return 1 + _max_overlap(s1, s2, i+1, j+1)
    else:
        return max(_max_overlap(s1, s2, i+1, j), _max_overlap(s1, s2, i, j+1))

# Optimized solution using memoization
def overlap_subsequence_memo(s1, s2):
    return _max_overlap_memo(s1, s2, 0, 0, {})

def _max_overlap_memo(s1, s2, i, j, memo):
    key = (i,j)
    if key in memo:
        return memo[key] 

    if i == len(s1) or j == len(s2):
        return 0 

    if s1[i] == s2[j]:
        memo[key] = 1 + _max_overlap_memo(s1, s2, i+1, j+1, memo)
    else:
        memo[key] = max(_max_overlap_memo(s1, s2, i+1, j, memo), 
        _max_overlap_memo(s1, s2, i, j+1, memo))

    return memo[key]

# Driver code
# Test case 01
print(overlap_subsequence_memo("dogs", "daogt")) # --> 3

# Test case 02
print(overlap_subsequence("xcyats", "criaotsi")) # -> 4

# Test case 03
print(overlap_subsequence("xfeqortsver", "feeeuavoeqr")) # -> 5

# Test case 04
print(overlap_subsequence_memo("kinfolklivemustache", "bespokekinfolksnackwave")) # -> 11

# Test case 05
print(overlap_subsequence_memo(
  "mumblecorebeardleggingsauthenticunicorn",
  "succulentspughumblemeditationlocavore"
)) # -> 15