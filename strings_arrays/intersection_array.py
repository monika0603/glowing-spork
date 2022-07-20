""" 
Given two arrays, write a function to get the intersection of the two. For example, if 
A = [1,2,3,4,5], and B = [0,1,3,7] then you should return [1,3]
"""

def intersection(list_1, list_2):

    return [i for i in list_1 if i in list_2]

A = [1,2,3,4,5]
B = [0,1,3,7]
print(intersection(A, B))