'''
heapq

시간복잡도 : O(NlogN)
'''
import heapq

def heapsort(iterable):
    h = []
    result = []
    #heap push
    for value in iterable:
        heapq.heappush(h, -value)
        print(h)
    #heap pop
    for _ in range(len(h)):
        result.append(-heapq.heappop(h))
    return result # heap result return

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)

'''
bisect를 통해
정렬된 리스트에서 특정 값의 원소의 개수 구하기

시간복잡도 : O(logN)
'''
from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
    right_index = bisect_left(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]
print(count_by_range(a, 4, 4)) # 값이 4인 개수 출력
print(count_by_range(a, -1, 3)) # [-1, 3] 범위의 데이터 개수 출력