N = int(input())
array = []

for _ in range(N):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1])))

array = sorted(array, key=lambda student : student[1])
print(array)