""" 
Write a function, pair_product, that takes in a list and a target product as arguments. 
The function should return a tuple containing a pair of indices whose elements multiply 
to the given target. The indices returned must be unique.

Be sure to return the indices, not the elements themselves.

There is guaranteed to be one such pair whose product is the target.
"""

def pair_product(nums, target):

    mapping = {}

    for i,n in enumerate(nums):
        ratio = target/n 
        if ratio in mapping:
            return (mapping[ratio], i) 
        else:
            mapping[n] = i 

# Driver code
# Test case 01
nums = [3,2,5,4,1]
target = 8
print(pair_product(nums, target))

# Test case 02
nums = [3, 2, 5, 4, 1]
target = 10 
print(pair_product(nums, target))

# Test case 03
nums = [4, 7, 9, 2, 5, 1]
target = 5
print(pair_product(nums, target))
