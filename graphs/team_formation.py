'''
input example:
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1
'''
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

n, m = map(int, input().split())
parent_table = [0] * (n + 1)

for i in range(n + 1):
    parent_table[i] = i

for _ in range(m):
    op, a, b = map(int, input().split())
    # union
    if op == 0:
        union_parent(parent_table, a, b)
    elif op == 1:
        if find_parent(parent_table, a) == find_parent(parent_table, b):
            print('YES')
        else:
            print('NO')
