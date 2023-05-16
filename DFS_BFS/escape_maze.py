from collections import deque

N, M = map(int, input().split())
array = []
for _ in range(N):
    array.append(list(map(int, input())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue :
        (cx, cy) = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if nx >= 0 and nx < N and ny >=0 and ny < M and array[nx][ny] == 1:
                queue.append((nx, ny))
                array[nx][ny] = array[cx][cy] + 1

    return array[N-1][M-1]

def dfs(x, y):
    dfs_stack = []
    dfs_stack.append((x, y))

    while dfs_stack :
        (cx, cy) = dfs_stack.pop()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if nx >= 0 and nx < N and ny >=0 and ny < M and array[nx][ny] == 1:
                dfs_stack.append((nx, ny))
                array[nx][ny] = array[cx][cy] + 1

    return array[N - 1][M - 1]

# print(bfs(0, 0))
print(dfs(0, 0))