""" 
Write a function, uncompress, that takes in a string as an argument. The input string will 
be formatted into multiple groups according to the following pattern:

<number><char>
for example, '2c' or '3a'.

The function should return an uncompressed version of the string where each 'char' of a 
group is repeated 'number' times consecutively. You may assume that the input string is 
well-formed according to the previously mentioned pattern.
"""

def uncompress_twopointers(str):

    numbers = '0123456789'
    i = j = 0 
    result = []

    while j < len(str):
        if str[j] in numbers:
            j += 1 
        else:
            nums = int(str[i:j]) 
            # IMPORTANT: strings in python are immutable, so a string concatenation operation such as 
            # given below will result in multiple copies being created
            # result = ''
            # result += str[i]*nums
            result.append(str[j]*nums)
            j += 1 
            i = j 

    return "".join(result) 



# Brute force approach
def uncompress(str):

    nums = [] 
    chars = []
    output = []

    for i in range(len(str)):
        if i%2 != 0:
            chars.append(str[i]) 

        else:
            nums.append(str[i])

    for i in range(len(nums)):
        output.append(chars[i]*int(nums[i]))

    return "".join(output)

# driver code 
str = "2c3a1t"
print(uncompress(str))

# Test case 02:
str = "127y"
print(uncompress_twopointers(str))