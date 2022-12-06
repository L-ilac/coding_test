# 쉬운 최단거리

from collections import deque

n, m = map(int, input().split())
zido = []

start_x, start_y = 0, 0
for i in range(n):
    tmp = list(map(int, input().split()))
    if 2 in tmp:
        start_x, start_y = i, tmp.index(2)
        tmp[start_y] = 0
    zido.append(tmp)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
queue = deque([(start_x, start_y)])
visited = [[0] * m for _ in range(n)]
visited[start_x][start_y] = 1

while queue:
    x, y = queue.popleft()
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if 0<= tx < n and 0 <= ty < m and visited[tx][ty] == 0 and zido[tx][ty] == 1:
            zido[tx][ty] += zido[x][y]
            visited[tx][ty] = 1
            queue.append((tx, ty))

for i in range(n):
    for j in range(m):
        if visited[i][j] == 0 and zido[i][j] >= 1:
            zido[i][j] = -1

for x in zido:
    print(*x)


