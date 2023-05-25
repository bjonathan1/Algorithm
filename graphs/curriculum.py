'''
input example:
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1

This question is kind of tricky because of few reasons:
1. How input has defined: time prev_node prev_node ... -1
   It gets easily confused because it is not a format such as (a, b)
   I used 'a' and 'b' to clarify prev_node and next_node and it helped a lot.

2. Difficulty of defining dynamic programming
   relation equation : result[b] = max(result[b], result[a] + time[b])
'''
from collections import deque
import copy

n = int(input())
degree = [0] * (n + 1)
graph = [[] for i in range(n + 1)]
time = [0] * (n + 1)

for i in range(1, n + 1):
    temp = list(map(int, input().split()))
    time[i] = temp[0]
    for a in temp[1:-1]:
        graph[a].append(i)
        degree[i] += 1

q = deque()
result = copy.deepcopy(time) #Deep copy does not change the time list var value
for i in range(1, n + 1):
    if degree[i] == 0:
        q.append(i)

while q:
    cur = q.popleft()
    for b in graph[cur]:
        degree[b] -= 1
        result[b] = max(result[b], result[cur] + time[b])

        if degree[b] == 0:
            q.append(b)

for i in range(1, n + 1):
    print(result[i])
