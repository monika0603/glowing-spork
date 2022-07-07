""" 
Write a function, intersection, that takes in two lists, a,b, as arguments. The function 
should return a new list containing elements that are in both of the two lists.

You may assume that each input list does not contain duplicate elements.
"""
# Brute force solution
# This has a time complexity of O(mn) as I am iterting through the array twice
def intersection(nums1, nums2):

    return [a for a in nums1 if a in nums2]

nums1 = [4,2,1,6]
nums2 = [3,6,9,2,10]
print(intersection(nums1, nums2))

def intersection_optimized(nums1, nums2):

    nums1_set = set(nums1)
    output = []

    for num in nums2:
        if num in nums1_set:
            output.append(num)

    return output

# Driver code
nums1 = [ i for i in range(0, 50000) ]
nums2 = [ i for i in range(0, 50000) ]
print(intersection_optimized(nums1, nums2))
