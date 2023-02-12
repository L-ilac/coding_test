from itertools import combinations
from collections import deque

import copy
n, m = map(int, input().split())

board = []
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
virus = []
vacant = []

for i in range(n):
    data = list(map(int, input().split()))
    board.append(data)
    for j in range(m):
        if data[j] == 2:
            virus.append((i, j))
        elif data[j] == 0:
            vacant.append((i, j))

# print(vacant)


def dfs(x, y, board):
    visited[x][y] = True

    for dx, dy in d:
        new_x, new_y = x+dx, y + dy

        if 0 <= new_x <= n-1 and 0 <= new_y <= m-1:
            if board[new_x][new_y] == 0 and not visited[new_x][new_y]:
                board[new_x][new_y] = 2
                dfs(new_x, new_y, board)


def bfs(x, y, board):
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    while q:
        now_x, now_y = q.popleft()

        for dx, dy in d:
            new_x, new_y = now_x+dx, now_y + dy

            if 0 <= new_x <= n-1 and 0 <= new_y <= m-1:
                if board[new_x][new_y] == 0 and not visited[new_x][new_y]:
                    board[new_x][new_y] = 2
                    visited[new_x][new_y] = True
                    q.append((new_x, new_y))


max_safe = 0

for comb in list(combinations(vacant, 3)):
    visited = [[False] * m for _ in range(n)]
    tmp = copy.deepcopy(board)

    for x, y in comb:
        tmp[x][y] = 1

    for x, y in virus:
        #dfs(x, y, tmp)
        bfs(x, y, tmp)

    cnt = 0
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 0:
                cnt += 1

    max_safe = max(max_safe, cnt)

print(max_safe)
