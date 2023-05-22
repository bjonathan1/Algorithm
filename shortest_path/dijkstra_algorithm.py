'''
입력 예시 :
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

Time-Complexity : O(V^2)
  - From Node(V) * To Node(V)
  - len(Node) < 5,000 : Okay
  - len(Node) > 10,000 : Not Okay
'''

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

def get_smallest_node(distance_table):
    min_value = INF
    index = 0

    for i in range(1, n + 1):
        if distance_table[i] < min_value and not visited[i]:
            min_value = min(distance_table[i], min_value)
            index = i

    return index

def dijkstra(start):
    distance_table = [INF] * (n + 1)
    # Init Starting Node
    distance_table[start] = 0
    visited[start] = True
    for bc in graph[start]:
        distance_table[bc[0]] = bc[1]

    # Start traversing
    for _ in range(n-1):
        cur = get_smallest_node(distance_table)
        visited[cur] = True
        for bc in graph[cur]:
            cost = distance_table[cur] + bc[1]
            if distance_table[bc[0]] > cost:
                distance_table[bc[0]] = cost
    return distance_table

distance = dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])