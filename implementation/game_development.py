N, M = map(int, input().split())
cx, cy, dir = map(int, input().split())
array = []
for _ in range(N):
    array.append(list(map(int, input().split())))

isVisited = [[0] * M for _ in range(N)]
isVisited[cx][cy] = 1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left(dir):
    dir -= 1
    if dir == -1 :
        return 3
    return dir

count = 1
turn_time = 0
while True:
    dir = turn_left(dir)
    nx = cx + dx[dir]
    ny = cy + dy[dir]

    if isVisited[nx][ny] == 0 and array[nx][ny] == 0:
        isVisited[nx][ny] = 1
        cx, cy = nx, ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1

    if turn_time == 4:
        nx = cx - dx[dir]
        ny = cy - dy[dir]
        if array[nx][ny] == 0:
            cx, cy = nx, ny
        else:
            break
        turn_time = 0

print(count)
