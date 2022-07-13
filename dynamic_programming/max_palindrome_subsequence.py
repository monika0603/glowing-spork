""" 
Write a function, max_palin_subsequence, that takes in a string as an argument. The function 
should return the length of the longest subsequence of the string that is also a palindrome.

A subsequence of a string can be created by deleting any characters of the string, while 
maintaining the relative order of characters.

A string subsequence is when I can delete a character to keep it a palindrome. 

String = lxuul 

                                        lxuul
                                          | (since l and l are equal, return 2)
                                         xuu
                                    / (delete first char) \ (delete last char)
                                uu (return 2)             xu
                                                      0 /    \ 0
                                                      u        x
""" 
# Brute force solution without using memoization
def max_palin_subsequence(s):
    # Staring with the first and last index to compare them
    return _max_palin_subsequence(s, 0, (len(s)-1)) 

def _max_palin_subsequence(s, i, j):
    # if the two index match, then we have a string of one character
    if i == j:
        return 1
    # if i and j cross
    if i > j:
        return 0
    # If the two characters match, then I want to recurssively call the function 
    # by incrementing i and decrementing j
    if s[i] == s[j]:
        return 2 + _max_palin_subsequence(s, i+1, j-1)
    # Otherwise pick the larger return value between the left and right
    else:
        return max(_max_palin_subsequence(s, i, j-1), 
                   _max_palin_subsequence(s, i+1, j))

# Optimized solution using memoization
def max_palin_subsequence_memo(s):
    return _max_palin_subsequence_memo(s, 0, (len(s)-1), {})

def _max_palin_subsequence_memo(s, i, j, memo):
    key = (i,j)
    if key in memo:
        return memo[key]

    if i == j:
        return 1 
    if i > j:
        return 0 

    if s[i] == s[j]:
        memo[key] = 2 + _max_palin_subsequence_memo(s, i+1, j-1, memo)
    else:
        memo[key] = max(_max_palin_subsequence_memo(s, i+1, j, memo), 
        _max_palin_subsequence_memo(s, i, j-1, memo))
    return memo[key]


# Driver code
# Test case 01
s = "luwxult"
print(max_palin_subsequence(s))

# Test case 02
s = "xyzaxxzy"
print(max_palin_subsequence(s))

# Test case 03
s = "lol"
print(max_palin_subsequence(s))

# Test case 04
s = "boabcdefop"
print(max_palin_subsequence(s))

# Test case 05
s = "chartreusepugvicefree"
print(max_palin_subsequence(s))

# Test case 06
s = "qwueoiuahsdjnweuueueunasdnmnqweuzqwerty"
print(max_palin_subsequence_memo(s))

# Test case 07 
s = "enamelpinportlandtildecoldpressedironyflannelsemioticsedisonbulbfashionaxe"
print(max_palin_subsequence_memo(s))
