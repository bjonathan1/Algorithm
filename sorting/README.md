# Sorting
> Sorting is arranging data into a specific order

Normally we sort data into `Ascending` or `Descending` order.
Although there are lots of `Sorting Algorithms`, we will go through
few algorithms in this chapter: `Selection Sort`, `Insertion Sort`, 
`Quick Sort`, and `Count Sort`. 

`Sorting` is so important not only
because it is used everywhere in today's lives, but also it matters 
a lot in terms of efficiency. Data is increasing exponentially in today's
world. Thus, in order to manipulate this enormous data size, choosing
a right `Sorting Algorithm` is critical to optimize te result. 

Now that we know the basic idea of sorting, let's go through each `Sorting Algorithms`.

## Selection Sort
> Primitive method of finding the smallest value data and exchanging from the left of the list. 

By continually repeating the method above, it will sort data in the time-complexity of O(N²). 
One feature of this Algorithm is that, it uses a lot of `Comparing Operation`, but small number
of `Swapping Operation`. If the cost of `Swapping` data is very big, `Selection Sort` can be 
an option of choosing for the `Sorting Algorthim`. 

## Insertion Sort
> Method of swapping to a right position one item at a time by comparison.

Starting from the second item from left, we insert into the appropriate position up to the point
of pivot position. Even though the time-complexity of this algorithm is `O(N²)`, 
one big advantage of this algorithm is that it takes only `O(N)` of time-complexity of
sorting if **the list is already sorted**. In this case, it is even faster than
using the `Quick Sort` which will learn next. 

## Quick Sort
> Quick Sort is a `divide-and-conquer` method algorithm that sorts by continuously cutting the list
> into halves.   

Here are some explanation of how `Quick Sort` works. Three variables are used 
in every step : `Pivot`, `Right`, `Left`. 

1. `Pivot` will be the first data of the list. 
2. `Left` starts from the data after `pivot` moving toward right direction. 
3. `Right` starts from the end data of the list moving toward left direction.
4. If `Left` value is larger than `Pivot` value, and `Right` value is smaller than `Pivot` value, 
   exchange the value of `Left` and `Right`. 
5. If the position of `Left` and `Right` has changed, we divide(or Partition) the list, 
   place `Pivot` on that position, and continue previous steps for splited left list, and right list. 
   
When the size of the list is one, it is impossible to divide, thus terminated. 
`Quick Sort` is one of the fastest `Sorting Algorithm` that has average time-complexity
of O(NlogN) ≈ 1.39(NlogN). Even c value is very small! C++, One of the most used language, 
use `Quick Sort` for its `Sorting Algorithm`.

## Count Sort
> Count Sort is used when there are many overlapping numbers in a list.   

`Count Sort` can be only used in restricted cases, but it is one of extremely
fast `Sorting Algorithm`. If data number is N, and the biggest value in the list is K, 
**the worst case** of time-complexity of `Count Sort` is `O(N + K)`. However, 
it can be utilized only if the data size is limited and in integer form. 
Normally, it is said that range of the smallest number of the data and the
largest number of data should not exceed 1,000,000 to use `Count Sort` effectively. 
 
Unlike other `Sorting Algorithms` above, it does not compare data but 
uses counting table to count the number of each data and print the data
in the order of the table. 

Some of you might already assumed that it will take big `space-complexity`
over `time-complexity`. Space-complexity of `Count Sort` is also `O(N + K)`. 


### Conclusion
At last, I was quite curious which `Sorting Algorithm` does each language supports. 
So here are some result which I have found : 
- Python : hybrid Algorithm of `Merge and Quick Sort`
- Java : `Merge Sort`
- C++ : `Quick Sort`

Why do they use different `Sorting Algorithms`? There are two important factors that makes differences. 
1. Comparability : Comparing `Key` and `Value`
2. Exchange : Swap occuring when switching orders

There are more `Comparability` and less `Exchange`  in `Quick Sort` where as
lest `Comparability` and more `Exchange` in `Merge Sort`. Since `Java` has 
higher cost on `Comparability` whereas `C++` has higher cost on `Exchange`, 
`Java` is more efficient on `Merge Sort` and `C++` is more efficient on `Quick Sort`.   