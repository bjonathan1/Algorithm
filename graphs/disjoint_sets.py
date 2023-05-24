'''
Input example:
6 4
1 4
2 3
2 4
5 6

Time-complexity of find: O(V)
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

# v : number of Nodes, e : edge (# of unions)
v, e = map(int, input().split())
parent_table = [0] * (v + 1)

# Initialize Parent Node to itself
for i in range(1, v + 1):
    parent_table[i] = i

cycle = False

for i in range(e):
    a, b = map(int, input().split())
    if find_parent(parent_table, a) == find_parent(parent_table, b):
        cycle = True
    union_parent(parent_table, a, b)

# Sets of each elements
print('Sets of each elements : ')
for i in range(1, v + 1):
    print(find_parent(parent_table, i), end=' ')
print()


# Result of Parent Table
print('Parent Table : ')
for i in range(1, v + 1):
    print(parent_table[i], end=' ')

print()
print('Cycle : ', cycle)

