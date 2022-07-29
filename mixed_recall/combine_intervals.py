""" 
Write a function, combine_intervals, that takes in a list of intervals as an argument. Each interval 
is a tuple containing a pair of numbers representing a start and end time. Your function should 
combine overlapping intervals and return a list containing the combined intervals.

Given two intervals:

(1, 4) and (3, 7)

The intervals overlap and
should be combined into:

(1, 7)

For example: If the input is given as below 
intervals = [
  (1, 4),
  (12, 15),
  (3, 7),
  (8, 13),
]
combine_intervals(intervals)
# -> [ (1, 7), (8, 15) ]

The first step is to sort in the input list by the first element in each pair. That would be 
(1,4), (3,7), (8, 13), (12, 15). That would give it a time complexity of nlogn. Then look through each 
pair to combine the intervals. 
"""

def combine_intervals(intervals):
    # Using the in-built sorted function in python which also takes key as input where we can 
    # specify a key that we want it to sort by 
    # So using lambda function for each pair, take the zeroth element
    # by saying key=lambda x: x[0]
    #sorted_intervals = sorted(intervals, key=lambda x: x[0])
    sorted_intervals = sorted(intervals)
    
    combined = [sorted_intervals[0]]

    for current_interval in sorted_intervals[1:]:
        current_start, current_end = current_interval 
        last_start, last_end = combined[-1]

        if last_end >= current_start:
            if current_end > last_end:
                combined[-1] = (last_start, current_end)
        else:
            combined.append(current_interval)

    return combined 


# Driver code 
# Test case 01
intervals = [
  (1, 4),
  (12, 15),
  (3, 7),
  (8, 13),
]
print(combine_intervals(intervals))

# Test case 02
intervals = [
  (6, 8),
  (2, 9),
  (10, 12),
  (20, 24),
]
print(combine_intervals(intervals))
# -> [ (2, 9), (10, 12), (20, 24) ]

# Test case 03
intervals = [
  (3, 7),
  (5, 8),
  (1, 5),
]
print(combine_intervals(intervals))
# -> [ (1, 8) ]

# Test case 04
intervals = [
  (3, 7),
  (10, 13),
  (5, 8),
  (27, 31),
  (1, 5),
  (12, 16),
  (20, 22),
]
print(combine_intervals(intervals))
# -> [ (1, 8), (10, 16), (20, 22), (27, 31) ]

# Test case 05
intervals = [
  (3, 7),
  (10, 13),
  (5, 8),
  (27, 31),
  (1, 5),
  (12, 16),
  (20, 32),
]
print(combine_intervals(intervals))
# -> [ (1, 8), (10, 16), (20, 32) ]

# Test case 06
intervals = [
  (64, 70),
  (50, 55),
  (62, 65),
  (12, 50),
  (72, 300000),
]
print(combine_intervals(intervals))
# -> [ (12, 55), (62, 70), (72, 300000) ]
