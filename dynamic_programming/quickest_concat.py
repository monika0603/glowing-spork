""" 
Write a function, quickest_concat, that takes in a string and a list of words as arguments. 
The function should return the minimum number of words needed to build the string by concatenating 
words of the list.

You may use words of the list as many times as needed.

Example: s = caution
words = ['ca', 'ut', 'ion', 'caut']
"""
# Brute force solution, using recursion without memoization
def quickest_concat(s, words):
    return _quickest_concat(s, words) 

def _quickest_concat(s, words):
    # Base case: is we reach an empty string, then return True
    if s == '':
        return 0 
    
    min_words = float("inf")
    # Loop over the list of words provided to chop of the suffix from the string if it exists
    for word in words:
        if s.startswith(word):
            suffix = s[len(word):]
            # Recur on the suffix now, thereby shrinking the length of the string and increment the count by 1
            attempt = 1 + _quickest_concat(suffix, words)
            min_words = min(attempt, min_words)

    return min_words 

# Optimized solution, with memoization
def quickest_concat_memo(s, words):
    result = _quickest_concat_memo(s, words, {})
    if result == float("inf"):
        return -1 
    else:
        return result

def _quickest_concat_memo(s, words, memo):
    if s in memo:
        return memo[s] 

    if s == '':
        return 0 
    min_words = float("inf")
    for word in words:
        if s.startswith(word):
            suffix = s[len(word):]
            attempt = 1 + _quickest_concat_memo(suffix, words, memo)
            min_words = min(attempt, min_words)
            memo[s] = min_words 

    return min_words

# Driver code
# Test case #1
s = 'caution'
words = ['ca', 'ion', 'caut', 'ut']
print(quickest_concat(s, words))

# Test case #2
s = 'caution'
words = ['ion', 'caut', 'caution']
print(quickest_concat(s, words))

# Test case #3
s = 'caution'
words = ['ion', 'caut', 'caution']
print(quickest_concat(s, words))

# Test case #4
s = 'respondorreact'
words = ['re', 'or', 'spond', 'act', 'respond']
print(quickest_concat(s, words))

# Test case #5
s = 'uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu'
words = ['u', 'uu', 'uuu', 'uuuu', 'uuuuu']
print(quickest_concat_memo(s, words))

# Test case #6
s = 'simchacindy'
words = ['sim', 'simcha', 'acindy', 'ch']
print(quickest_concat_memo(s, words))