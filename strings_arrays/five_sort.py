""" 
Write a function, five_sort, that takes in a list of numbers as an argument. The function 
should rearrange elements of the list such that all 5s appear at the end. Your function 
should perform this operation in-place by mutating the original list. The function should 
return the list.

Elements that are not 5 can appear in any order in the output, as long as all 5s are at 
the end of the list.
"""

def five_sort(nums):

    i = 0
    j = len(nums)-1

    # Loop to run while the two pointers cross 
    while i <= j:
        # if the last element is already 5 then I don't want to do anything but just decrement j
        if nums[j] == 5:
            j -= 1 
        # Otherwise if i is pointing at 5 I want to swap it
        elif nums[i] == 5:
            nums[i], nums[j] = nums[j], nums[i]
            # Increment i
            i += 1
        else:
            i += 1
            
    return nums

# Driver code
# Test case 01
nums = [12, 5, 1, 5, 12, 7]
print(five_sort(nums))

# Test case 02
nums = [5, 2, 5, 6, 5, 1, 10, 2, 5, 5]
print(five_sort(nums))
