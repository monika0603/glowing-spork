""" 
Write a function, detectDictionary, that takes in a dictionary of words and an alphabet string. 
The function should return a boolean indicating whether or not all words of the dictionary are 
lexically-ordered according to the alphabet.

You can assume that all characters are lowercase a-z.

You can assume that the alphabet contains all 26 letters.
"""
def lexical_order(word_1, word_2, alphabet):
    # Getting the max length of the two words
    max_length = max(len(word_1), len(word_2))

    for j in range(max_length):
        # Fetching indexes of the characters from the alphabets
        value_1 = alphabet.index(word_1[j]) if j < len(word_1) else float("-inf")
        value_2 = alphabet.index(word_2[j]) if j < len(word_2) else float("-inf")
        # Final decision on whether or not these words are ordered  
        if value_1 < value_2:
            return True 
        elif value_2 < value_1:
            return False 

    return True 

def detect_dictionary(dict, alphabet):
    # First looping over the input dictionary to fetch two words 
    for i in range(0, len(dict)-1):
        word_1, word_2 = dict[i], dict[i+1]
        # Calling the helper function to get their individual lexical ordering
        if not lexical_order(word_1, word_2, alphabet):
            return False 

    return True 
        

# Driver code 
# Test case 01 
dictionary = ["zoo", "tick", "tack", "door"]
alphabet = "ghzstijbacdopnfklmeqrxyuvw"
print(detect_dictionary(dictionary, alphabet)) # -> True

# Test case 02 
dictionary = ["zoo", "tack", "tick", "door"]
alphabet = "ghzstijbacdopnfklmeqrxyuvw"
print(detect_dictionary(dictionary, alphabet)) # -> False

# Test case 03
dictionary = ["zoos", "zoo", "tick", "tack", "door"]
alphabet = "ghzstijbacdopnfklmeqrxyuvw"
print(detect_dictionary(dictionary, alphabet)) # -> False

# Test case 04
dictionary = ["miles", "milestone", "proper", "process", "goal"]
alphabet = "mnoijpqrshkltabcdefguvwzxy"
print(detect_dictionary(dictionary, alphabet)) # -> True

# Test case 05
dictionary = ["miles", "milestone", "pint", "proper", "process","goal", "apple"];
alphabet = "mnoijpqrshkltabcdefguvwzxy"
print(detect_dictionary(dictionary, alphabet)) # -> False
