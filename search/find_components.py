import sys

def binary_search_byRecursion(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    # If target is smaller that pivot value:
    elif target < array[mid] :
        return binary_search_byRecursion(array, target, start, mid - 1)
    else:
        return binary_search_byRecursion(array, target, mid + 1, end)

# Solution using Binary Search
N = int(input())
data = sys.stdin.readline().rstrip()
array_n = list(map(int, data.split()))
array_n.sort() #Sorting takes O(NlogN)

M = int(input())
data = sys.stdin.readline().rstrip()
array_m = list(map(int, data.split()))

# Binary search of each M takes O(MlogN)
for m in array_m:
    result = binary_search_byRecursion(array_n, m, 0, N - 1)
    if result == None:
        print('no', end=' ')
    else:
        print('yes', end=' ')

#Final time-complexity using Binary Search : O((M+N)logN)
#By using Count Sort : O(M + N), with array = [0] * 1000001 which is sizeof(int) * 1000001 byte
