""" 
Depth-first-print of a graph
"""

graph = { 
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": []
}

def depth_first_print(graph, start):

    stack = [start] # Current stack [a]

    while stack:
        current = stack.pop()

        print(current)
        # FIFO operation will add b and c to the stack
        # [b, c]
        # Since is the end, it gets printed first and so on
        for neighbor in graph[current]: 
            stack.append(neighbor)

# Now instead of explicitly using a stack we can use a recursive function to call an 
# underlying stack
# Notice that the output is different in the below case
def depth_first_search(graph, current):
    print(current)

    for neighbor in graph[current]:
        depth_first_search(graph, neighbor)

print(depth_first_print(graph, "a"))
print(depth_first_search(graph, "a"))