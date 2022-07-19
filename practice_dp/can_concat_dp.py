""" 
Write a function, can_concat, that takes in a string and a list of words as arguments. The function 
should return boolean indicating whether or not it is possible to concatenate words of the list 
together to form the string.

You may reuse words of the list as many times as needed.
"""

def can_concat(s, words):
    return _can_concat(s, words)

def _can_concat(s, words):

    if len(s) == 0:
        return True

    for word in words:
        if s.startswith(word):
            suffix = s[len(word):]
            if _can_concat(suffix, words) == True:
                return True 

    return False 

# Driver code 
# Test case 01
print(can_concat("oneisnone", ["one", "none", "is"])) #  -> True

# Test case 02
print(can_concat("oneisnone", ["on", "e", "is"])) #  -> False