""" 
Problem: Calculate factorial of a given number. 
Essentially we start by defining the base cases for a recursive function. Which will ve 0! = 1 and 1! = 1 

first: 5*factorial(4)
second: 4*factorial(3)
Third:   3*factorial(2)
Forth:    2*factorial(1)
Fifth:     1*factorial(0)
"""
def factorial(num):
    # Base cases
    if num == 1:
        return 1 
    if num == 0:
        return 1 
    
    return num*factorial(num-1)

print(factorial(5))