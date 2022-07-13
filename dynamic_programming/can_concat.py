""" 
Write a function, can_concat, that takes in a string and a list of words as arguments. 
The function should return boolean indicating whether or not it is possible to concatenate 
words of the list together to form the string.

You may reuse words of the list as many times as needed.
Example: foodisgood 
[is, g, f, ood, foo]

                                foodisgood
                        f   /               \ foo 
                        oodisgood           disgood
                       ood |                 | --> no where to go since I have 'dis' at the beginning of the string
                         isgood
                        is |
                          good
                         g |
                          ood
                        ood|
                      empty string

On the left branch the characters/words along the edges give us the exact string we are looking for 
'foodisgood'.

Base case if to return True when we have a empty string, meaning we are at the bottom of the branch. 
if len(string) == 0:
    return True

The time complexity of this problem is O(n^s)
where n = len(string)
s = length of the list containing words/characters 

However, with memoization the time complexity reduces down to O(mn).
"""

# Brute force solution, without using memoization
def can_concat(s, words):
    # Base case: If the string is empty
    if s == '':
        return True
    
    # Looping over the list of words
    for word in words:
        # Using a built-in library in python startswith, if the string starts with the word 
        # provided 
        if s.startswith(word):
            # If it does then I want shrink my string by the letters I just matched 
            suffix = s[len(word):]
            # if the recursive leap-of-faith returns True then I want to return True 
            # Otherwise return False 
            if can_concat(suffix, words) == True:
                return True 
    return False 

# Optimized solution using memoization
def can_concat_memo(s, words):
    return _can_concat(s, words, {}) 

def _can_concat(s, words, memo):
    # Base case: if I have solved this problem before, then simply return memo at s
    if s in memo:
        return memo[s]
    # If my string has become empty, then return True
    if s == '':
        return True 

    for word in words:
        if s.startswith(word):
            suffix = s[len(word):]
            if _can_concat(suffix, words, memo) == True:
                # storing the values in the memo
                memo[s] = True
                return memo[s]

    memo[s] = False
    return memo[s] 
    


# Driver code
# Test case 01
s1 = "oneisnone"
str = ["one", "none", "is"] 
print(can_concat(s1, str))

# Test case 02
s1 = "oneisnone"
str = ["one", "none", "is"] 
print(can_concat_memo(s1, str))