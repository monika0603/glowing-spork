""" 
Problem: Given an integer array, return the maximum product of any three numbers in the 
array, For example if A = [1,3,4,5], you should return 60, while for B = [-2, -4, 5, 3]

Important: Ask clarifying question before jumping into the solution. If the input array will 
only contain all positive numbers or is also likely to contain negative numbers
"""

import heapq 
def max_product(A, B):

    a = heapq.nlargest(3, A) # For positive cases 
    b = heapq.nlargest(2, B) # For negative cases 

    return min(a[0]*a[1]*a[2], b[0]*b[1])

A = [1,3,4,5]
B = [-2, -4, 5, 3]

print(max_product(A, B))
