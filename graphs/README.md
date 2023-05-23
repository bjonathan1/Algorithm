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

`Disjoint Sets` is a Data Structure that handles disjoint sets with separate element data. 
It is also referred as `union-find` Data Structure, because it uses operations of `union` and 
`find` to utilize this Data Structure. In normal case, `Tree` Data Structure is used 
to implement `Disjoint Sets`. 

For example, on `union` operation, larger 'Node A' sets smaller 'Node B' as 
**Parent Node**. (e.g union 1, 4 : Node 4 → Node 1)

'Parent Table' is normally used to implement the `union` operation effectively. 
After `union` operation had been implemented, by finding out the 'Parent Node' of each Nodes
from the 'Parent Table'.  
