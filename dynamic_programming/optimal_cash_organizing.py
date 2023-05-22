n, m = map(int, input().split())
units = []
for _ in range(n):
    units.append(int(input()))

d = [0] + [10001] * m

for unit in units:
    for i in range(unit, m + 1):
        if d[i - unit] == 10001:
            continue
        else:
            d[i] = min(d[i], d[i - unit] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])