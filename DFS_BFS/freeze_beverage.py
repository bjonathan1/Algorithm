N, M = map(int, input().split())
array = []
for _ in range(N):
    array.append(list(map(int, input())))

count = 0
isVisited = [[0] * M for _ in range(N)]
dfs_stack = []
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

def dfs(dfs_stack):
    while len(dfs_stack) > 0:
        (cx, cy) = dfs_stack.pop()
        for k in range(4):
            nx = cx + dx[k]
            ny = cy + dy[k]

            if nx >= 0 and nx < N and ny >= 0 and ny < M and array[nx][ny] == 0 and not isVisited[nx][ny]:
                dfs_stack.append((nx, ny))
                isVisited[nx][ny] = 1

for i in range(N):
    for j in range(M):
        if array[i][j] == 0 and isVisited[i][j] == 0:
            dfs_stack.append((i, j))
            isVisited[i][j] = 1
            count += 1
            dfs(dfs_stack)


print(count)