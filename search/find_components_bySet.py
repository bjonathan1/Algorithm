import sys

# Solution using Set in Python
N = int(input())
data = sys.stdin.readline().rstrip()
array_n = set(map(int, data.split())) #Set insert : O(1) * N

M = int(input())
data = sys.stdin.readline().rstrip()
array_m = list(map(int, data.split()))

# Set search of each M takes O(1) * M
for m in array_m:
    if m in array_n:
        print('yes', end=' ')
    else:
        print('no', end=' ')

#Final time-complexity using set : O(M + N)