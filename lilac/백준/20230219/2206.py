from collections import deque
n, m = map(int, input().split())

board = []

for _ in range(n):
    tmp = list(input())
    board.append(tmp)


# ! visited[wall_break][n][m]
visited = [[[False]*m for _ in range(n)] for _ in range(2)]


d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

q = deque()
q.append((0, 0, 0, 0))  # ! x,y,step,벽을 부순 경우


result = -1

while q:
    now_x, now_y, step, wall_break = q.popleft()

    if now_x == n-1 and now_y == m-1:
        result = step+1
        break

    for dx, dy in d:
        new_x, new_y = now_x + dx, now_y + dy

        if 0 <= new_x <= n-1 and 0 <= new_y <= m-1:
            if not visited[wall_break][new_x][new_y]:
                visited[wall_break][new_x][new_y] = True

                if board[new_x][new_y] == '0':
                    q.append((new_x, new_y, step+1, wall_break))
                else:
                    if wall_break == 0:
                        q.append((new_x, new_y, step+1, 1))


print(result)
