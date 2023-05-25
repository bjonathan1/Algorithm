'''
input example:
7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4
'''
import sys

def find_parent(parent_table, x):
    if parent_table[x] != x:
        parent_table[x] = find_parent(parent_table, parent_table[x])
    return parent_table[x]

def union_parent(parent_table, a, b):
    a = find_parent(parent_table, a)
    b = find_parent(parent_table, b)

    if a < b:
        parent_table[b] = a
    else:
        parent_table[a] = b

input = sys.stdin.readline

v, e = map(int, input().split())

parent_table = [0] * (v + 1)
for i in range(1, v + 1):
    parent_table[i] = i

result_costs = []
edges = []

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()
for edge in edges:
    cost, a, b = edge
    if find_parent(parent_table, a) != find_parent(parent_table, b):
        union_parent(parent_table, a, b)
        result_costs.append(cost)

print(sum(result_costs[:-1]))