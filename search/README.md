# Search
> Method of searching a targeted data.  

There are out-numbered of data to deal with nowadays. Thus, 
it is very important to use a `right algorithm` to manipulate
 large amount of data. 
 
 `Sequential Search` is the most basic Searching algorithm you
 can think of. Searching the target data from the start until
 you find the data, the time complexity would be `O(n)`, **n**
 in terms of total number of data. 
 
However, there is a better searching algorithm to search in a 
better performance. In this chapter we will use `Binary Search`
algorithm to search the data in the time complexity of `O(log n)`.

## Binary Searching
> Prerequisite : In order to use this algorithm, data of the array has to be sorted. 

`Binary Searching` is an algorithm that keeps on looking for 
the **center** of an array. If the targeted number is smaller
that the centered number of the array, you will continue to 
search the center of the first half of the array and so on. 

As I mentioned above, the time complexity of `Binary Search`
is O(log n) which gets really powerful as the data gets BIG. 
There are two ways of implementing `Binary Search` : 
1. Recursion
2. Iteration

It is easier to get the concept of `Binary Search` by the
example of _Recursion_, however, it will be better to use
_Iteration_ when it comes to solve a real example. 