from collections import deque
n, m = map(int, input().split())


before_board = []
diff_board = [[0]*m for _ in range(n)]

for _ in range(n):
    before_board.append(list(map(int, input().split())))

for i in range(n):
    tmp2 = list(map(int, input().split()))
    for j in range(m):
        diff_board[i][j] = before_board[i][j] - tmp2[j]


def bfs(start_val, start_pos, board, visited):
    d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    q = deque()

    result = set()

    start_x, start_y = start_pos

    visited[start_x][start_y] = True
    q.append((start_x, start_y))

    while q:
        now_x, now_y = q.popleft()
        result.add((now_x, now_y))

        for dx, dy in d:
            new_x, new_y = now_x + dx, now_y + dy

            if 0 <= new_x <= n-1 and 0 <= new_y <= m-1 and not visited[new_x][new_y] and board[new_x][new_y] == start_val:
                visited[new_x][new_y] = True
                q.append((new_x, new_y))

    return result


before_visited = [[False]*m for _ in range(n)]
diff_visited = [[False]*m for _ in range(n)]

before_result = []
diff_result = []

for i in range(n):
    for j in range(m):
        if not before_visited[i][j]:
            before_result.append(
                bfs(before_board[i][j], (i, j), before_board, before_visited))

        if not diff_visited[i][j] and diff_board[i][j] != 0:
            diff_result.append(
                bfs(diff_board[i][j], (i, j), diff_board, diff_visited))

print(before_result)
print(diff_result)


flag = True
diff = 0

for d in diff_result:
    if d not in before_result:
        flag = False
    else:
        diff += 1


if flag and diff <= 1:
    print("YES")
else:
    print("NO")
