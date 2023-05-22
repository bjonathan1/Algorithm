'''
Input example:
3 2 1
1 2 4
1 3 2
'''
import heapq
import sys

INF = int(1e9)
input = sys.stdin.readline

n, m, c = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

def dijkstra(start):
    h = []
    heapq.heappush(h, (0, start))
    time_table = [INF] * (n + 1)
    time_table[start] = 0

    while h:
        cur_time, cur_node = heapq.heappop(h)
        if time_table[cur_node] < cur_time:
            continue
        for yz in graph[cur_node]:
            cost = cur_time + yz[1]
            if cost < time_table[yz[0]]:
                time_table[yz[0]] = cost
                heapq.heappush(h, (cost, yz[0]))
    return time_table

distance = dijkstra(c)
count = 0
max_distance = 0

for i in range(1, n + 1):
    if distance[i] != INF:
        count += 1
        max_distance = max(max_distance, distance[i])

print(count - 1, max_distance)

