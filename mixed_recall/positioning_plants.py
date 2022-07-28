""""
You've been hired to plant flowers in a garden with n different positions. There are m different 
flower types. The prices of flowers types vary depending on which position they are planted. 
Your bosses are picky, they tell you to never plant two of the same flower type right next 
to each other. What is the minimum cost we need to plant a flower in each position of the garden?

Write a function, positioningPlants, that takes in a 2D list with dimensions n * m. Each row 
of the list represents the costs of the flower types at that position. This means that costs[i][j] 
represents the cost of planting flower type j at position i. For example: 

Given these costs,

costs = [
  [4, 3, 7],
  [6, 1, 9],
  [2, 5, 3]
]

The costs of plants at position 1 are $6, $1, and $9.
The cost of planting flower type 0 at position 1 is $6.
The cost of planting flower type 2 at position 1 is $9.

The function should return the minimum cost of planting flowers without placing the same flower 
type in adjacent positions.

At the root level you start with the zeroth position and you can choose any type of plant. 

                                                   0, null
                                    4 /            | 3            \ 7 
                                  (1,0)           (1,1)           (1,2)
                                /1      \9       6/    9\        6/    1\
                              (2,1)    (2,2)   (2,0)    (2,2)   (2,0)  (2,1)
                            2/   3\    2/  5\  5/ 3\    2/ 5\   5/ 3\  2/  3\
                          (3,0) (3,2) (3,0)(3,1)(3,1)(3,2)(3,0)(3,1)(3,2)(3,0)(3,2)

So from the bottom, between the edges we will choose the minimum. For left most, between 2 & 3
we will choose 2. At level 2, add it to 1 and similarly at level 1, add it to 4. So for the 
left most branch the cost = 4+1+2 which is the minimum cost in this case.    

Time complexity:
n = # of positions
m = # of plants types 
Time: O(m^n)
Space: O(n)

So with memoization we get a time complexity of O(mn). So instead of raising a base to an exponent 
we are just multiplying m with n. 
"""
# Brute force solution

def positioning_plants(costs, pos=0, last_plant=None):
  if pos == len(costs):
    return 0 

  min_cost = float("inf")
  for plant_type, plant_cost in enumerate(costs[pos]):
    if plant_type != last_plant:
      candidate = plant_cost + positioning_plants(costs, pos + 1, plant_type)
      min_cost = min(min_cost, candidate)

  return min_cost

# Driver code
# Test case 01
print(positioning_plants([
  [4, 3, 7],
  [6, 1, 9],
  [2, 5, 3]
])) # -> 7, by doing 4 + 1 + 2.

# Test case 02
print(positioning_plants([
  [12, 14, 5],
  [6, 3, 2]
])) # -> 8

# Test case 03
print(positioning_plants([
  [12, 14, 5],
  [6, 3, 2],
  [4, 2, 7],
  [4, 8, 4],
  [1, 13, 5],
  [8, 6, 7],
])) # -> 23

# Test case 04 
print(positioning_plants([
  [12, 14, 5, 13],
  [6, 3, 20, 3],
  [24, 12, 7, 2],
  [4, 80, 45, 3],
  [104, 13, 5, 14],
  [38, 19, 7, 6],
  [12, 2, 1, 2],
])) # -> 26

# Optimized solution, using memoization
def positioning_plants_memo(costs, pos=0, last_plant=None):
  return _positioning_plants_memo(costs, pos, last_plant, {})

def _positioning_plants_memo(costs, pos, last_plant, memo):
  key = (pos, last_plant)
  if key in memo:
    return memo[key] 

  if pos == len(costs):
    return 0 

  min_cost = float("inf")
  for plant_type, plant_cost in enumerate(costs[pos]):
    if plant_type != last_plant:
      candidate = plant_cost + _positioning_plants_memo(costs, pos+1, plant_type, memo)
      min_cost = min(min_cost, candidate)
      memo[key] = min_cost 

  return memo[key] 

# Driver code
# Test case 01
print(positioning_plants_memo([
  [4, 3, 7],
  [6, 1, 9],
  [2, 5, 3]
])) # -> 7, by doing 4 + 1 + 2.

# Test case 02
print(positioning_plants_memo([
  [12, 14, 5],
  [6, 3, 2]
])) # -> 8

# Test case 03
print(positioning_plants_memo([
  [12, 14, 5],
  [6, 3, 2],
  [4, 2, 7],
  [4, 8, 4],
  [1, 13, 5],
  [8, 6, 7],
])) # -> 23

# Test case 04 
print(positioning_plants_memo([
  [12, 14, 5, 13],
  [6, 3, 20, 3],
  [24, 12, 7, 2],
  [4, 80, 45, 3],
  [104, 13, 5, 14],
  [38, 19, 7, 6],
  [12, 2, 1, 2],
])) # -> 26







