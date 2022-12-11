# 녹색 옷 입은 애가 젤다지?

from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

idx = 0
while True:

    N = int(input())
    if N == 0:
        break

    zido = []
    for _ in range(N):
        zido.append(list(map(int, input().split())))
    visited = [[float('inf')] * N for _ in range(N)]

    visited[0][0] = zido[0][0]
    queue = deque([(0, 0)])
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if 0 <= tx < N and 0 <= ty < N:
                cost = visited[x][y] + zido[tx][ty]
                if visited[tx][ty] > cost:
                    visited[tx][ty] = cost
                    queue.append((tx, ty))
    idx += 1
    print(f"Problem {idx}: {visited[N-1][N-1]}")