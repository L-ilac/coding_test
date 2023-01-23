import sys
from collections import deque

n, m = map(int, input().split())

board = []

for i in range(n):
    tmp = list(map(int, sys.stdin.readline().rstrip()))
    board.append(tmp)

# ! 3차원 배열을 이용한 풀이.... 아이디어가 신박하다.


def bfs():
    q = deque()
    d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    # visited[0][x][y] and visited[1][x][y]
    visited = [[[-1]*m for _ in range(n)] for _ in range(2)]

    q.append((0, 0, 1, 0))  # x좌표, y좌표, step, 벽 뚫고 왔는가 유무

    visited[0][0][0] = 1

    while q:
        nowx, nowy, step, wallbreak = q.popleft()

        # bfs 탐색이기때문에, 가장 먼저 도착지점에 도착하는 경로가 최단거리이다.
        if nowx == n-1 and nowy == m-1:
            break

        for dx, dy in d:

            newx, newy = nowx+dx, nowy+dy

            if 0 <= newx <= n-1 and 0 <= newy <= m-1:
                if board[newx][newy] == 0 and visited[wallbreak][newx][newy] == -1:
                    visited[wallbreak][newx][newy] = step+1
                    q.append((newx, newy, step+1, wallbreak))

                if board[newx][newy] == 1:
                    if wallbreak == 0:
                        visited[1][newx][newy] = step+1
                        q.append((newx, newy, step+1, 1))
                    # 이미 벽을 한번 뚫고 와서 갈 수 없음
                    else:
                        pass

    return max(visited[0][-1][-1], visited[1][-1][-1])


min_route = bfs()

if min_route == -1:
    print(-1)
else:
    print(min_route)


# ! bfs 2번을 이용한 신박한 풀이
# ! 출발점 -> 모든지점까지의 최단거리, 도착점 -> 모든지점까지의 최단거리
# ! 벽(i,j)를 뚫고가는 최단거리 -> 출발점 -> (i,j) 까지 최단거리 + (i,j) -> 도착점 까지 최단거리 -1

input = sys.stdin.readline

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
n, m = map(int, input().split())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().strip())))


def bfs(x, y):
    q = deque()
    q.append((x, y))
    dist = [[int(1e9)] * m for _ in range(n)]
    dist[x][y] = 0
    while q:
        x, y = q.popleft()
        for a, b in d:
            nx, ny = x + a, y + b
            # ! dist가 visited, 거리저장 의 역할을 함.
            if 0 <= nx < n and 0 <= ny < m and dist[nx][ny] == 1e9:
                # ! 벽일 경우 거리만 업데이트해주고, 탐색하진 않음.
                dist[nx][ny] = dist[x][y]+1

                # ! 지나갈 수 있는 공간에 대해서만 탐색함.
                if arr[nx][ny] == 0:
                    q.append((nx, ny))

    return dist


zero = bfs(0, 0)
end = bfs(n-1, m-1)
ans = zero[n-1][m-1]

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            ans = min(ans, zero[i][j] + end[i][j])

if ans == 1e9:
    print(-1)
else:
    print(ans + 1)
