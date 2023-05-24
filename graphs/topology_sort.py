'''
Input Example:
7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4

Time-Complexity : O(V + E)
'''
from collections import deque

v, e = map(int, input().split())
graph = [[] for i in range(v + 1)]
indegree = [0] * (v + 1)

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort():
    result = []
    q = deque()

    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        cur = q.popleft()
        result.append(cur)

        for i in graph[cur]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in result:
        print(i, end=' ')

topology_sort()