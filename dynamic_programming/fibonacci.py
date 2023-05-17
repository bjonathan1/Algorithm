# Time-Complexity : O(2^n)
def fibo(x):
    if x == 1 or x== 2:
        return 1
    return fibo(x - 1) + fibo(x - 2)

# using Dynamic Programming(Recursion) : O(n)
d = [0] * 100
def fibo_dynamic_recursion(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo_dynamic_recursion(x - 1) + fibo_dynamic_recursion(x - 2)
    return d[x]

# using Dynamic Programming(Iteration) : O(n)
def fibo_dynamic_iteration(x):
    d = [0] * 100

    d[1] = 1
    d[2] = 1

    for i in range(3, x + 1):
        d[i] = d[i - 1] + d[i - 2]

    return d[x]

print(fibo_dynamic_iteration(99))