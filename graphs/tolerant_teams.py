""" 
Write a function, tolerant_teams, that takes in a list of rivalries as an argument. A rivalry is 
a pair of people who should not be placed on the same team. The function should return a boolean 
indicating whether or not it is possible to separate people into two teams, without rivals being 
on the same team. The two teams formed do not have to be the same size.

This problem is more commonly known as 'is graph bipartite' meaning capable of divided into two groups
"""
import collections
def tolerant_teams(team_list):
    # Creating a default dictionary with list as it's values
    graph = collections.defaultdict(list)

    # Since this is an acyclic graph, we append x nodes with y and vice-versa
    for x,y in team_list:
        graph[x].append(y)
        graph[y].append(x)

    # Empty dictionary to begin with, where keys will be the nodes of the graph and 
    # values will be boolean values representing alternating colors. 
    coloring = {}

    # Itertive logic to color each node of the graph
    for node in graph:
        if node not in coloring:
            if validate(graph, node, coloring, False) == False:
                return False 

    return coloring 

def validate(graph, node, coloring, current_color):
    # Base case if the node that I am currently visiting has already been visited before 
    # And if the current color that I am assigning is the color that is previously assigned.
    if node in coloring:
        return current_color == coloring[node]

    # Otherwise the node has not been previously colored, and we should color it 
    coloring[node] = current_color

    # Now I am visiting all the neighbors of the current node, recursively call the validate function
    # and importantly flip the color using the boolean not 
    for neighbor in graph[node]:
        if validate(graph, neighbor, coloring, not current_color) == False:
            return False 

    return True 

# test case 01:
team_list = [
  ('philip', 'seb'),
  ('raj', 'nader')
] 
print(tolerant_teams(team_list))

# test case 02:
team_list = [
  ('philip', 'seb'),
  ('raj', 'nader'),
  ('raj', 'philip'),
  ('seb', 'raj')
] 
print(tolerant_teams(team_list))

# test case 03:
team_list = [
  ('cindy', 'anj'),
  ('alex', 'matt'),
  ('alex', 'cindy'),
  ('anj', 'matt'),
  ('brando', 'matt')
]
print(tolerant_teams(team_list))

# test case 04:
team_list = [
  ('alex', 'anj'),
  ('alex', 'matt'),
  ('alex', 'cindy'),
  ('anj', 'matt'),
  ('brando', 'matt')
]
print(tolerant_teams(team_list))