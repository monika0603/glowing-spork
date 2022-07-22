""" 
Oh-no! You forgot the number combination that unlocks your safe. Luckily, you knew that you'd be 
forgetful so you previously wrote down a bunch of hints that can be used to determine the correct 
combination. Each hint is a pair of numbers 'x, y' that indicates you must enter digit 'x' before 
'y' (but not necessarily immediately before y).

The keypad on the safe has digits 0-9. You can assume that the hints will generate exactly one 
working combination and that a digit can occur zero or one time in the answer.

Write a function, safe_cracking, that takes in a list of hints as an argument and determines the 
combination that will unlock the safe. The function should return a string representing the combination.
"""
import collections 

def topological_order(graph):
  num_parents = {}
  for node in graph:
    num_parents[node] = 0
    
  for node in graph:
    for child in graph[node]:
      num_parents[child] += 1
  
  ready = [ node for node in graph if num_parents[node] == 0 ]
  order = []
  while ready:
    node = ready.pop()
    order.append(node)
    for child in graph[node]:
      num_parents[child] -= 1
      if num_parents[child] == 0:
        ready.append(child)
    
  return order


def safe_cracking(edges):
    graph = collections.defaultdict(list) 

    for x,y in edges:
        if x not in graph:
            graph[x] = []
        if y not in graph:
            graph[y] = []
        graph[x].append(y) 

    return topological_order(graph)

    
print(safe_cracking([
  (7, 1),
  (1, 8),
  (7, 8),
]))

print(safe_cracking([
  (3, 1),
  (4, 7),
  (5, 9),
  (4, 3),
  (7, 3),
  (3, 5),
  (9, 1),
]) )