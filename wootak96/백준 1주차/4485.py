import heapq
import sys

INF = int(1e9)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dijkstra():
    q = []
    heapq.heappush(q, (graph[0][0], 0, 0))
    dis[0][0] = 0

    while q:
        cost, x, y = heapq.heappop(q)

        if x == n - 1 and y == n - 1:
            print(f'Problem {cnt}: {dis[x][y]}')
            break

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                newcost = cost + graph[nx][ny]

                if newcost < dis[nx][ny]:
                    dis[nx][ny] = newcost
                    heapq.heappush(q, (newcost, nx, ny))
cnt = 1
while True:
    n = int(input())
    if n == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(n)]
    dis = [[INF] * n for _ in range(n)]

    dijkstra()
    cnt += 1
