from collections import deque

n, m = map(int, input().split())

board = []
visited = [[False] * m for _ in range(n)]

for _ in range(n):
    board.append(list(map(int, list(input()))))


def bfs(i, j):
    q = deque()
    d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    visited[i][j] = True
    q.append((i, j))

    while q:
        now_x, now_y = q.popleft()

        for dx, dy in d:
            new_x, new_y = now_x + dx, now_y + dy

            if 0 <= new_x <= n - 1 and 0 <= new_y <= m - 1:
                if board[new_x][new_y] == 0 and not visited[new_x][new_y]:
                    visited[new_x][new_y] = True
                    q.append((new_x, new_y))


def dfs_stack(i, j):
    q = []
    d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    print(i, j)

    # 현재 방문하는 지점 방문 처리
    visited[i][j] = True
    q.append((i, j))

    # 다음 방문지는 어디?
    while q:
        now_x, now_y = q.pop()
        for dx, dy in d:
            new_x, new_y = now_x + dx, now_y + dy

            # 보드 범위 벗어나지 않고, 0 이면서, 아직 방문 안했으면 거기로 옮겨서 dfs
            if 0 <= new_x <= n - 1 and 0 <= new_y <= m - 1:
                if board[new_x][new_y] == 0 and not visited[new_x][new_y]:
                    visited[new_x][new_y] = True
                    q.append((new_x, new_y))


def dfs_recursive(i, j):
    print(i, j)
    d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # 현재 방문하는 지점 방문 처리
    visited[i][j] = True

    # 다음 방문지는 어디?
    for dx, dy in d:
        new_x, new_y = i + dx, j + dy

        # 보드 범위 벗어나지 않고, 0 이면서, 아직 방문 안했으면 거기로 옮겨서 dfs
        if 0 <= new_x <= n - 1 and 0 <= new_y <= m - 1:
            if board[new_x][new_y] == 0 and not visited[new_x][new_y]:
                dfs_recursive(new_x, new_y)


cnt = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 0 and not visited[i][j]:
            # bfs(i, j)
            # dfs_recursive(i, j)
            # dfs_stack(i, j)
            cnt += 1

print(cnt)
