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
        return 1 + _max_palin_subsequence(s, i+1, j-1)
    # Otherwise pick the larger return value between the left and right
    else:
        return max(_max_palin_subsequence(s, i, j-1), 
                   _max_palin_subsequence(s, i+1, j))

# Driver code
# Test case 01
s = "luwxult"
print(len(s)-1)
print(max_palin_subsequence(s))
