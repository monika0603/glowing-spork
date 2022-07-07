""" 
Write a function, anagrams, that takes in two strings as arguments. The function should 
return a boolean indicating whether or not the strings are anagrams. Anagrams are strings 
that contain the same characters, but in any order.
"""

def anagrams(s1, s2):
    # If lengths don't match then return false immediately
    if len(s1) != len(s2):
        return False 

    # Defining dictionaries for two strings
    count_s1 = {}
    count_s2 = {}

    # Fetching the count of keys in different string
    for i in range(len(s1)):
        count_s1[s1[i]] = 1 + count_s1.get(s1[i], 0)
        count_s2[s2[i]] = 1 + count_s2.get(s2[i], 0) 

    # Matching the counts of keys in different string
    for c in count_s1:
        if count_s1[c] != count_s2.get(c, 0):
            return False

    return True

# Driver code
# Test case 01
s1 = 'restful'
s2 = 'fluster'
print(anagrams(s1, s2)) 

# Test case 02
s1 = 'cats'
s2 = 'tocs'
print(anagrams(s1, s2)) 