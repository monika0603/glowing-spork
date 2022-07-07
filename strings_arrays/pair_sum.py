""" 
Write a function, pair_sum, that takes in a list and a target sum as arguments. The function 
should return a tuple containing a pair of indices whose elements sum to the given target. 
The indices returned must be unique.

Be sure to return the indices, not the elements themselves.

There is guaranteed to be one such pair that sums to the target.
"""

def pair_sum(nums, target):

    mapping = {} 

    for i,n in enumerate(nums):
        diff = target - n 
        if diff in mapping:
            return mapping[diff], i 
        else:
            mapping[n] = i

nums = [3,2,5,4,1]
target = 8 
print(pair_sum(nums, target))
