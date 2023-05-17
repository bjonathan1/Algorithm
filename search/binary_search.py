# Binary Search Source Code O(logN)

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

def binary_search_byIteration(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        # If target is smaller that pivot value:
        elif target < array[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return None

# n(length of array), target input
n, target = list(map(int, input().split()))
# input array
array = list(map(int, input().split()))

result = binary_search_byIteration(array, target, 0, n - 1)
if result == None:
    print('target element not found')
else:
    print(result + 1)