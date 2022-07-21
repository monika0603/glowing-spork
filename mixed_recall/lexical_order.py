""" 
Write a function, lexical_order, that takes in 2 words and an alphabet string as an argument. The function 
should return True if the first word should appear before the second word if lexically-ordered according 
to the given alphabet order. If the second word should appear first, then return False.

Note that the alphabet string may be any arbitrary string.

Intuitively, Lexical Order is like "dictionary" order:

You can assume that all characters are lowercase a-z.

You can assume that the alphabet contains all 26 letters.
"""

def lexical_order(s1, s2, alphabet):

    max_length = max(len(s1), len(s2))

    for i in range(max_length):
        
        value_1 = alphabet.index(s1[i]) if i < len(s1) else float("-inf")
        value_2 = alphabet.index(s2[i]) if i < len(s2) else float("-inf")

        if value_1 < value_2:
            return True 
        elif value_2 < value_1:
            return False 

# Driver code
# Test case 01
alphabet = "abcdefghijklmnopqrstuvwxyz"
print(lexical_order("apple", "dock", alphabet)) # -> True

# Test case 02
alphabet = "abcdefghijklmnopqrstuvwxyz"
print(lexical_order("apple", "ample", alphabet)) # -> False

# Test case 03
alphabet = "abcdefghijklmnopqrstuvwxyz"
print(lexical_order("app", "application", alphabet)) # -> True