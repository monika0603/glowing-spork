""" 
Write a function, rare_routing, that takes in a number of cities (n) and a list of tuples 
where each tuple represents a direct road that connects a pair of cities. The function should 
return a boolean indicating whether or not there exists a unique route for every pair of cities. 
A route is a sequence of roads that does not visit a city more than once.

Cities will be numbered 0 to n - 1.

You can assume that all roads are two-way roads. This means if there is a road between A and B, 
then you can use that road to go from A to B or go from B to A.

For example, given these roads:

0 --- 1
| \
|  \
|   \
2    3

There is a unique route for between every pair of cities.
So the answer is True.


For example, given these roads:

0 --- 1
| \
|  \
|   \
2 -- 3

There are two routes that can be used to travel from city 1 to city 2:
- first route:  1, 0, 2
- second route: 1, 0, 3, 2 
The answer is False, because routes should be unique.

IMPORTANT: A simple cycle detection solution applies here for all the test case expect for the 
last test case where we are actually give two disparate nodes (0,1) and (3,2), and there is no 
way to reach from one set to another. So our solution fails here. Becuase by default it is only 
looking to find a cycle, and it indeed doesn't find a cycle. While the problem asks for a unique 
path that must exist between all the cities. There is no path between 0 to 3 or 1 to 2.    
"""

def rare_routing(n, roads):
    graph = {}
    for i in range(n):
        graph[i] = [] 

    for x,y in roads:
        graph[x].append(y)
        graph[y].append(x) 

    visited = set() 

    # IMPORTANT: I need to be able to visit all cities with a unique path starting from just one city
    # In this case we are using 0 as our first city 
    # Also, using last_node to account for the last visited node so our code doesn't stuck in a loop 
    # Passing it as None initially and in the recurssive call the last visited will be simply the node
    # passed
    valid = validate(graph, 0, visited, None)
    # Check if we get returned True from the DFS and if the length of the visited set is the same as 
    # the number of cities as in the input
    return valid and len(visited) == n


def validate(graph, node, visited, last_node):
    # If we have visited the node earlier then return False 
    if node in visited:
        return False 
    # Otherwise add it to the visited set
    visited.add(node)

    # Recursive call to check for neighboring nodes
    for neighbor in graph[node]:
        # neighbor != last_node makes sure that we don't back to the node we just visited
        if neighbor != last_node and validate(graph, neighbor, visited, node) == False:
            return False 

    return True 

# test case 01
print(rare_routing(4, [
  (0, 1),
  (3, 2),
]))
    
# test case 02
print(rare_routing(4, [
  (0, 1),
  (0, 2),
  (0, 3)
]))

# test case 03 
print(rare_routing(6, [
  (1, 2),
  (4, 1),
  (5, 4),
  (3, 0),
  (0, 1),
  (0, 4),
]))

# test case 04
print(rare_routing(6, [
  (1, 2),
  (5, 4),
  (3, 0),
  (0, 1),
  (0, 4),
]))

    


