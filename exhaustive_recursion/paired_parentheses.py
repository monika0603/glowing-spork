""" 
Write a function, paired_parentheses, that takes in a string as an argument. The function should 
return a boolean indicating whether or not the string has well-formed parentheses.

You may assume the string contains only alphabetic characters, '(', or ')'.
"""

def paired_parentheses(string):

    count = 0 

    for char in string:
        if char == '(':
            count += 1 
        elif char == ')':
            # At any point in loop I should never decrement count to less than zero
            if count == 0:
                return False 
            count -= 1 

    return count == 0 

# Driver code 
# Test case 01
print(paired_parentheses("(david)((abby))")) # -> True

# Test case 02
print(paired_parentheses("()rose(jeff")) # -> False

# Test case 03
print(paired_parentheses("")) # -> True