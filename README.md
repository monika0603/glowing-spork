# Python Data Structures & Algorithms

This repository is dedicated to Python data structures and algorithms for learning purposes. This youtube video (https://www.youtube.com/watch?v=tWVWeAqZ0WU) by Alvin Zablan is an awesome resource to learn graph algorithms specifically. Alvin explains the approach to a problem fluently and makes graph solution implementation like a piece of cake. 

**What is a graph?**

Graph = Nodes + Edges 

![](https://github.com/monika0603/glowing-spork/blob/main/graphs/graph.png)


Where a, b, c, d, e, and f are <ins> nodes </ins> and <ins> edges </ins> are the connections between the nodes. Nodes are vertices are interchangeably used. There can be many edges between the nodes. 

Graphs can be cyclic and/or acyclic where:

<ins> cyclic </ins>  = A path in the nodes where we can get back where we started from.

<ins> acyclic </ins>  = Where there is no such path. Or in other words there is only a certain direction to follow. 

Cyclic and acyclic are also known as directed and undirected, respectively. However, graphs can have cycle as well as a specific direction within it's nodes. 

**Breadth First Traversal**

BFS uses queue data structure where we add from the back and remove from the front. It uses FIFO concept, first-in-first-out. While DFS uses stack data structure and is based on LIFO concept. We always remove the last element we added. 

A BFS traversal will explore nodes in all the directions evenly. As show here ![alt text](https://github.com/monika0603/glowing-spork/blob/main/graphs/BFS.png)

**Important** 
BFS is implemented iteratively and DFS is implemented recursively. The reason for that is because BFS uses a queue data structure which has an inherent recursive stack call. 

**Graph Matrix**

In a graph, any position can be accessed using (row, col) and any position will at least have four neighbors. Up, down, left and right directions. Let's say we are at a position (r,c), and if we wanted to go up we are reducing the row by one, so up direction will be represented by (r-1,c). Similarly, if we wanted to go down we are increasing the row, so incrementing r by will give the down neighbor (r+1,c). Likewise, if wanted a neighbor to the right, we'd increment the col position by one, (r, c+1) and left will be represented by (r, c-1). These are the four direction shown in the diagram below. 

![alt text](https://github.com/monika0603/glowing-spork/blob/main/graphs/graph_matrix.png)
