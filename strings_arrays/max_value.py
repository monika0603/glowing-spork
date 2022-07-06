""" 
Write a function, max_value, that takes in list of numbers as an argument. 
The function should return the largest number in the list.
"""

def max_value(nums):

    maximum = float("-inf")

    for num in nums:
        maximum = max(maximum, num)

    return maximum

    
nums = [4,7,2,8,10,9]
print(max_value(nums))