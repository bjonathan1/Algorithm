# Graph Algorithms

There are various of `Graph Algorithm` used in current world. And here are two ways of implementing
Graphs : 
- Adjacency Matrix : method of using 2-dim array
  - Need O(V²) of Memory Space
  - Searching time of Node A to Node B : O(1)
  - ex) Floyd-Warshall Algorithm
  
- Adjacency List : method of using list
  - Need O(E) of Memory Space
  - Searching time of Node A to Node B : O(E)
  - ex) Dijkstra Algorithm


## Disjoint Sets
> In math, it is defined as 'two Sets with no element in common'.
> 
> Disjoint Sets Algorithm distributes set of elements into Disjoint Sets.  

`Disjoint Sets` is a Data Structure that handles disjoint sets with separate element data. 
It is also referred as `union-find` Data Structure, because it uses operations of `union` and 
`find` to utilize this Data Structure. In normal case, `Tree` Data Structure is used 
to implement `Disjoint Sets`. 

For example, on `union` operation, larger 'Node A' sets smaller 'Node B' as 
**Parent Node**. (e.g union 1, 4 : Node 4 → Node 1)

'Parent Table' is normally used to implement the `union` operation effectively. 
After `union` operation had been implemented, by finding out the 'Parent Node' of each Nodes
from the 'Parent Table' by using `Recursion`, we can find the group of sets of Nodes. 

Time-Complexity : O(V + MlogV) (in large size of input)

> Disjoint Sets Algorithm can be used for Cycle Detection on a non-direction graph.


## Spanning Tree

`Spanning Tree` is a sub-graph of a graph that satisfies two conditions:
- include all Nodes of the graph
- Does NOT form a cycle

A typical example of `Spanning Tree` is `Kruskal Algorithm`.

### Kruskal Algorithm
> Kruskal Algorithm is an Algorithm that finds the Minimum cost Spanning Tree

By using `Kruskal Algorithm`, we can easily find the minimum-distanced Spanning Tree. 
Also, it is classified in `Greedy Algorithm`. This is how `Kruskal Algorithm` works :
1. Find the path(Edge) starting from the shortest-path to longest-path.  
2. Determine whether the **cycle** occurs
3. If not, add the path to the `Spanning Tree`

That's it! How simple is that! 

The core part of this problem is the _cycle determination_. In this example, 
since we have learned `Disjoint Sets Algorithm` can be used for _Cycle Detection_, 
we will use that to solve the `Kruskal Algorithm`.

Time-Complexity : O(ElogE)

## Topology Sort
> One of Sorting Algorithm that keeping all Nodes in an order that does not oppose its direction. 

`Topology Sort` is frequently used in real world. Everything that has to do with **Prerequisite**
uses `Topology Sort` to define its graph. Before we get to `Topology Sort`, we need to know the
concept of `Indegree`. 
> Indegree : Number of Edges that come IN to a certain Node. (Number of Prerequisites)

e.g If _Advanced Algorithm_ class has two prerequisite of _Data Structure_ and _Algorithm_,
the indegree of _Advanced Algorithm_ Node is defined as '2'. 

Now that we know the concept of Indegree. Here are some process of `Topology Sort Algorithm` :
1. Enque all nodes that have the indegree of 0 into a queue. 
2. Repeat the process below until the queue is empty. 
    1. Deque an element(node) from the queue, and delete edges that set out from that element(node).
    2. Enque all new nodes that became the indegree of 0. 
    
If queue is empty **before** all Nodes had visited, we know that the cycle has occurred.  

Time-Complexity : O(V + E)