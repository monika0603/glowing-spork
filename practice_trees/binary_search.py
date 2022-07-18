""" 
Write a function, binary_search, that takes in a sorted list of numbers and a target. The 
function should return the index where the target can be found within the list. If the target 
is not found in the list, then return -1.

You may assume that the input array contains unique numbers sorted in increasing order.

Your function must implement the binary search algorithm.
"""

def binary_search(nums, target):
    # Using the two pointer technique
    lo = 0 
    hi = len(nums)-1 
    
    # While lo is less than or equal to the high pointer, otherwise the two pointers have 
    # crossed each other
    while lo <= hi:
        # Calculate te mid point
        mid = (lo + hi)//2

        # If target is less than the mid point, then decrement the high ponter
        if target < nums[mid]:
            hi = mid - 1 
        # Otherwise increment the low pointer
        elif target > nums[mid]:
            lo = mid + 1 
        # Otherwise we have found the target at the mid point itself.
        else:
            return mid
    return -1

# Driver code
# Test case 01 
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8]
target = 6 
print(binary_search(nums, target))

# Test case 02
nums = [0, 6, 8, 12, 16, 19, 20, 24, 28]
target = 27
print(binary_search(nums, target))

# test case 03
nums = [0, 6, 8, 12, 16, 19, 20, 28]
target = 8
print(binary_search(nums, target))
