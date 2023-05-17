import sys
N, M = map(int, input().split())
data = sys.stdin.readline().rstrip()
array = list(map(int, data.split()))

# binary search
start = 0
end = max(array)

result = 0
while start <= end:
    mid = (start + end) // 2
    total = 0

    for x in array:
        if x > mid:
            total += x - mid

    if total < M :
        end = mid - 1
    else:
        result = mid # Answer would be
        start = mid + 1

print(result)