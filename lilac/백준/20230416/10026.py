from collections import deque

n = int(input())


board = []

d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
visited = [[False]*n for _ in range(n)]
visited_rg = [[False]*n for _ in range(n)]

for _ in range(n):
    board.append(list(input()))


def bfs(starting_color, start_pos):
    q = deque()
    q.append(start_pos)

    start_x, start_y = start_pos
    visited[start_x][start_y] = True

    while q:
        now_x, now_y = q.popleft()

        for dx, dy in d:
            new_x, new_y = now_x + dx, now_y + dy

            if 0 <= new_x <= n-1 and 0 <= new_y <= n-1 and not visited[new_x][new_y] and board[new_x][new_y] == starting_color:
                visited[new_x][new_y] = True
                q.append((new_x, new_y))


def bfs_rg(starting_color, start_pos):
    q = deque()
    q.append(start_pos)

    start_x, start_y = start_pos
    visited_rg[start_x][start_y] = True

    while q:
        now_x, now_y = q.popleft()

        for dx, dy in d:
            new_x, new_y = now_x + dx, now_y + dy

            if 0 <= new_x <= n-1 and 0 <= new_y <= n-1 and not visited_rg[new_x][new_y]:
                if starting_color == 'B':
                    if board[new_x][new_y] == starting_color:
                        visited_rg[new_x][new_y] = True
                        q.append((new_x, new_y))
                else:
                    if board[new_x][new_y] == "R" or board[new_x][new_y] == "G":
                        visited_rg[new_x][new_y] = True
                        q.append((new_x, new_y))


normal = 0
rg = 0

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(board[i][j], (i, j))
            normal += 1
        if not visited_rg[i][j]:
            bfs_rg(board[i][j], (i, j))
            rg += 1


print(normal, rg)
