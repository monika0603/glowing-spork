""" 
Write a function, merge_sort, that takes in a list of numbers as an argument. The 
function should return a new list containing elements of the original list sorted 
in ascending order. Your function must implement the merge sort algorithm.

nums = [4,6,7,3,1,2,5,8]

Time complexity = O(nlogn)
"""
from collections import deque 

def merge_sort(nums):
    # Base case if the length of the input array ia zero or 1, then 
    # simply return the input array itself
    if len(nums) <= 1:
        return nums 

    # Finding the mid-value by dividing by 2
    mid = len(nums)//2
    # Recurssively calling the function to keep diving the inout array
    left_sorted = merge_sort(nums[:mid])
    right_sorted = merge_sort(nums[mid:])
    # Calling the helper function to sort the two portions
    return merge(left_sorted, right_sorted)

def merge(list_1, list_2):
    merged = []
    # Using deque instead of just using a list because when we compare the 
    # zeroth elements of the two lists (left and right) we will pop the first element.
    # This will result in a gap at the beginning and entire list needs to be shifted left 
    # to fill the gap. 
    # Whereas a deque has O(1) insertion and pop time, rendering it more efficient
    list_1 = deque(list_1)
    list_2 = deque(list_2)

    while list_1 and list_2:
        if list_1[0] < list_2[0]:
            merged.append(list_1.popleft())
        else:
            merged.append(list_2.popleft())

    merged += list_1 
    merged += list_2 

    return merged 

# Driver code
# Test case 01
nums = [4,6,7,3,1,2,5,8]
print(merge_sort(nums))

# Test case 02:
numbers = [
  72, 42, 16, 81, 84, 17,  2, 81, 22, 79, 86, 38, 
  77, 80, 81, 70, 81, 80, 35, 21, 89, 38, 57, 28, 
   4, 17, 50, 38, 68, 82, 22, 76, 45, 40, 67, 94, 
  37, 27, 81, 53, 36, 18, 28, 60, 45, 74, 40, 29, 
  18,  6, 28, 57, 42, 60, 64, 12, 78, 97, 96,  1, 
  20, 20, 61, 67, 82, 10, 63, 71, 39, 52, 37, 69, 
  37, 24, 66, 74, 15, 92, 49, 31, 56, 67, 50, 57, 
  79,  0, 21, 56, 82, 22,  4, 20, 91, 72, 58, 93, 
  99, 14, 42, 91 
]
print(merge_sort(numbers))