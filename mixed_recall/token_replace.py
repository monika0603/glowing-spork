""" 
Write a function, token_replace, that takes in a dictionary of tokens and a string. The function 
should return a new string where tokens are replaced.

Tokens are enclosed in a pair of '$'. You can assume that the input string is properly formatted. 
Tokens should be replaced from left to right in the string (see test_05).
"""

def token_replace(s, token):
    
    for word, value in token.items():
        s = s.replace(word, value)

    return s 

# Driver code
# Test case 01

tokens = {
  '$LOCATION$': 'park',
  '$ANIMAL$': 'dog',
}
print(token_replace('Walk the $ANIMAL$ in the $LOCATION$!', tokens))
# -> 'Walk the dog in the park!'

# Test case 02
tokens = {
  '$ADJECTIVE$': 'quick',
  '$VERB$': 'hopped',
  '$DIRECTION$': 'North'
}
print(token_replace('the $ADJECTIVE$ fox $VERB$ $ADJECTIVE$ly $DIRECTION$ward', tokens))
# -> 'the quick fox hopped quickly Northward'

# Test case 03 
tokens = {
  '$greeting$': 'hey programmer',
}
print(token_replace('his greeting is always $greeting$.', tokens))
# -> 'his greeting is always hey programmer.'