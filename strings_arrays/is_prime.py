""" 
The function should return a boolean indicating whether or not the given number is prime.

A prime number is a number that is only divisible by two distinct numbers: 1 and itself.

For example, 7 is a prime because it is only divisible by 1 and 7. For example, 6 is not a prime 
because it is divisible by 1, 2, 3, and 6.

You can assume that the input number is a positive integer.
"""

def is_prime(number):

    # A prime number is a number divisible by 1 or by itself
    # Logic is to divide the input number by all the numbers between 
    # 2 and one less than the input number. Return False as soon as the 
    # anytime the remainder is zero.
    for i in range(2, number):
        if number%i == 0:
            return False 

    return True  

    # To take into account that 1 is not a prime number
    if number == 1:
        return False 

# Driver code
print(is_prime(2))
