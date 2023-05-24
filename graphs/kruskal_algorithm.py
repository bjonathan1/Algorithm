'''
input example:
7 9
1 2 29
1 5 75
2 3 35
2 6 34
3 4 7
4 6 23
4 7 13
5 6 53
6 7 25

Time-Complexity : O(ElogE)
'''

def find_parent(parent_table, x):
    if parent_table[x] != x:
        parent_table[x] = find_parent(parent_table, parent_table[x])
    return parent_table[x]

def union_parent(parent_table, a, b):
    a = find_parent(parent_table, a)
    b = find_parent(parent_table, b)

    if a < b :
        parent_table[b] = a
    else:
        parent_table[a] = b

v, e = map(int, input().split())
edges = []
spanning_tree = []

parent_table = [0] * (v + 1)
for i in range(1, v + 1):
    parent_table[i] = i

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()
total_cost = 0
for edge in edges:
    cost, a, b = edge
    # Cycle Detection
    if find_parent(parent_table, a) == find_parent(parent_table, b):
        continue
    union_parent(parent_table, a, b)

    spanning_tree.append((a, b, cost))
    total_cost += cost

print(spanning_tree)
print(total_cost)