'''
Advanced Dijkstra Algorithm use "Heap" to overcome its defect of Time-Complexity.

Time-Complexity : O(E * log(V))
-> Time-complexity of inserting and removing N data : NlogN
Input Example :
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
'''

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input()) #Starting Node
graph = [[] for i in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    #From a, to b, distance : c
    graph[a].append((b,c))

def dijkstra(start):
    distance_table = [INF] * (n + 1)
    q = []
    # Init Starting Node
    heapq.heappush(q, (0, start))
    distance_table[start] = 0

    while q: # heap q max : E
        cur_val, cur_node = heapq.heappop(q)
        # If it had already visited
        if distance_table[cur_node] < cur_val:
            continue
        for bc in graph[cur_node]:
            cost = cur_val + bc[1]
            if distance_table[bc[0]] > cost:
                distance_table[bc[0]] = cost
                heapq.heappush(q, (cost, bc[0]))

    return distance_table

distance = dijkstra(start)

print(f"Distance from Node {start} : ")
for i in range(1, n + 1):
    if distance[i] == INF:
        print(i, ": INFINITY")
    else:
        print(i, " : ", distance[i])