
# ! n은 50 이하 , l<= r<= 100
from collections import deque
n, l, r = map(int, input().split())

board = []

for _ in range(n):
    data = list(map(int, input().split()))
    board.append(data)

# 접근법 -> 그래프 탐색해서
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
time = 0


def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = True

    group = []
    total_popularity = 0

    while q:
        now_x, now_y = q.popleft()
        total_popularity += board[now_x][now_y]

        group.append((now_x, now_y))

        for dx, dy in d:
            new_x, new_y = now_x+dx, now_y+dy

            if 0 <= new_x <= n-1 and 0 <= new_y <= n-1:
                if not visited[new_x][new_y] and l <= abs(board[now_x][now_y] - board[new_x][new_y]) <= r:
                    visited[new_x][new_y] = True
                    q.append((new_x, new_y))

    unified = total_popularity//len(group)
    for gx, gy in group:
        board[gx][gy] = unified


while True:
    # 지도에서 인구이동이 필요한 영역을 구함
    visited = [[False] * n for _ in range(n)]
    cnt = 0

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(i, j)
                cnt += 1
                print(board)

    print(cnt)

    if cnt == n*n:
        break

    time += 1

    # ! 통합된 나라에 대해서는 탐색을 할 필요가 없다.

print(time)
