# Dynamic Programming
> Dynamic : Multistage, time varying

> Dynamic Programming : Method of solving problems by re-defining it
  to subproblems.  

`Dynamic programming` is one of the most important and popular technique today. 
It can be used when it can _break down to recurring sub-problems_. The idea of
`Dynamic Programming` is to solve every sub-problems **just once**, and stores into
table in case you need to use it again. 

Also, `Dynamic Programming` is one of the representatives figure of `Bottom-Up` method. 
It starts from solving the smallest sub-problem by choosing the optimal, and
eventually up to the point where it is solving the overall problem. Nevertheless,
`Dynamic Programming` technique cannot be used in every situations. It has to satisfy
the standard below:

A problem that 
- Can break down to Recurring small sub-problems
- Is applicable for Optimization problem. (Finding Maximum or Minimum value)
- Sub-problems are not independent - sub-problems share sub-sub-problems.

The key of solving `Dynamic Programming` questions is to **define the sub-problems
accurately**. Sometimes there are multiple ways of defining the sub-problem. So it
is necessary to solve various types of questions of `Dynamic Programming` and get
use to right ideas of different kinds of sub-problems.    

> Memoization : One of techniques to implement Dynamic Programming. It is a concept
  of saving the result of once solved problem to the memory space, in order to call
  back when the same equation has revealed. It is also referred as "Caching". 

By using a little bit of _Memory Space_ (Storing into table), it can increase 
the performance of some problem. 

Some well-known problems of `Dynamic Programming` include:
- Fibonacci Problem 
- Longest Common Sequence (LCS) Problem
- 0-1 Knapsack Problem