""" 
Write a function, compress, that takes in a string as an argument. The function should return a 
compressed version of the string where consecutive occurrences of the same characters are 
compressed into the number of occurrences followed by the character. Single character occurrences 
should not be changed.

'aaa' compresses to '3a'
'cc' compresses to '2c'
't' should remain as 't'
You can assume that the input only contains alphabetic characters.
"""

def compress(s):

    # Initializing two pointers for compressing the string
    i = 0 
    j = 1
    # Since strings are immutable in python, we define a list and later convert to a string
    # Otherwise everytime we add something to a string, it creates copies, thereby increasing 
    # complexity
    result = [] 
    count = 1
 
    while j<len(s):
        
        if s[i] == s[j]:
            count += 1
            i += 1 
            j += 1 
        else:
            if count > 1:
                result.append(str(count))
            result.append(s[i])
            count = 1 
            i += 1
            j += 1

    if count > 1:       
        result.append(str(count))
    result.append(s[i])
                 
    return "".join(result)


# Driver code
# Test case 01
s = "ccaaatsss"
print(compress(s))

# Test case 02 
s = "ssssbbz"
print(compress(s))

# Test case 03 
s = "ppoppppp"
print(compress(s))

