from collections import deque
N, L, R = map(int, input().split())

board = []

for _ in range(N):
    board.append(list(map(int, input().split())))

r = len(board)
c = len(board[0])


d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
visited = []


def bfs(start, cnt):
    q = deque()
    q.append(start)
    visited[start[0]][start[1]] = cnt

    total_pop = 0
    total_pop += board[start[0]][start[1]]
    unified = 1

    while q:
        now_x, now_y = q.popleft()

        for dx, dy in d:
            new_x, new_y = now_x + dx, now_y+dy

            if 0 <= new_x <= r-1 and 0 <= new_y <= c-1:
                if visited[new_x][new_y] == -1 and L <= abs(board[now_x][now_y]-board[new_x][new_y]) <= R:
                    unified += 1
                    visited[new_x][new_y] = cnt
                    total_pop += board[new_x][new_y]
                    q.append((new_x, new_y))

    # 통합한 나라가 없을 경우
    if unified == 1:
        pass
    else:
        for i in range(r):
            for j in range(c):
                if visited[i][j] == cnt:
                    board[i][j] = total_pop//unified


day = 0
while True:
    visited = [[-1]*c for _ in range(r)]
    cnt = 0
    flag = 0
    for i in range(r):
        for j in range(c):
            if visited[i][j] == -1:
                bfs((i, j), cnt)
                flag += 1
                cnt += 1

                # print(board)
                # print(visited)

    if flag == r*c:
        print(day)
        break

    day += 1
