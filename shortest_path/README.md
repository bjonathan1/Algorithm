# Shortest Path

Shortest Path problems mostly use **graphs** of _nodes_ and _edges_ to define their 
problems. There are three main Shortest Path algorithms that are being taught most commonly:

1. Dijkstra Shortest Path Algorithm
2. Floyd-Warshall Algorithm
3. Bellman-Ford Algorithm 

Note that `Greedy` and `Dynamic Programming` is used to solve Shortest Path Problems. 

## Dijkstra Shortest Path Algorithm
> Algorithm that find the shortest path of starting Node to each Nodes. 

`Dijkstra Shortest Path Alogorithm` finds the shortest path by continually finding 
the shortest path from starting node to next node and so on. By the end of traversing
all Nodes, _the result of the list will be the shortest path of each node from the
starting Node_. Dijkstra does NOT work on with _negative value edged path_. 

The algorithm follows the basic rule of `Greedy Algorithm`. It repeats to find
'the closest node' apart the current Node. By keeping and refreshing the 
_shortest distance_ information of the list, we can find the shortest path at last. 

_Time-Complexity_ of `Dijkstra Algorithm` is `O(V²)`. However, if
`heap` is used, it can be optimized to `O(ElogV)`.

## Floyd-Warshall Algorithm
> Algorithm that find the shortest path from 'every Node' to 'every other Node'. 

Unlike `Dijkstra Algorithm`, `Floyd-Warshall Algorithm` uses **2-Dimension Table** to 
save all shortest path of each Node to the other Nodes. Furthermore, 
unlike `Dijkstra Algorithm` which follows the rule of `Greedy Algorithm`, `Floyd-Warshall Algorithm`
follows the rule of `Dynamic Programming`. 

For example, if there are total of N Nodes, it iterates N times of renew its 2-dim array. 
 

_Time-Complexity_ of `Floyd-Warshall Algorithm` is `O(V³)`.