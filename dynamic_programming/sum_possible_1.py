""" 
Write a function sum_possible that takes in an amount and a list of positive numbers. The 
function should return a boolean indicating whether or not it is possible to create the 
amount by summing numbers of the list. You may reuse numbers of the list as many times as 
necessary.

You may assume that the target amount is non-negative. 

amount = 4 
numbers = [1,2,3]

The below tree is built based on the thre options available, 1,2,and 3. Each node takes the difference 
between the option available keeping in mind that the difference cannot be negative. Which is why the 
tree grows on the left side as opposed to right side.  

                                        4
                             1 /       2|       3\
                             3          2       1
                        1/   2|   3\  1/ 2\   1/
                        2    1    0   1  0    0
                      1/ 0\ 1|
                      1   0  0
                     1|
                     0 
                            
Base case here would be the leaves of 0 
if amount == 0:
    return True 
Meaning I can always generate 0 without any input amount provided. 
Time Complexity: 
a = amount
n = length of the numbers 
Time: O(n^a)

There are duplicate sub trees in the tree displayed above, such as 2 -> 1 -> 0. This is where memoization 
startegy is helpful where once we have calculated a value, next time we just have to fetch them. 

IMPORTANT: With memoization we have reduced the time complexity of O(n^a) to simply O(a*n) because we have 
trimmed our tree by not having to do previous calculations again.  
"""

def sum_possible(amount, nums):
    return _sum_possible(amount, nums, {})


def _sum_possible(amount, nums, memo):
    # Base case if the amount exists in memo, then simply return the value
    # No need to compute it again
    if amount in memo:
        return memo[amount]
    # Another base case, that if any children call becomes 0 return True 
    if amount == 0:
        return True 
    # Another based case to simply return zero if amount - num becomes negative
    if amount < 0:
        return False 
    
    for num in nums:
        if _sum_possible(amount-num, nums, memo) == True:
            memo[amount] = True 
            return True 

    # If none of the above conditions are met then that means that we can't 
    # calculate the amount using the options provided in the numbers list and return False 
    memo[amount] = False 
    return False 