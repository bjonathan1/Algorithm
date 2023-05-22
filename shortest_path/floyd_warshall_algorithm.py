'''
input example:
4
7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2
'''
INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    graph[a][a] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j == i:
            continue
        for k in range(1, n + 1):
            if k == i or k == j:
                continue
            graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == INF:
            print("INF", end=' ')
        else:
            print(graph[i][j], end=' ')
    print()