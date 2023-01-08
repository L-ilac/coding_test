from collections import deque
n, m = map(int, input().split())

answer = 0
board = []
visited = [[False]*m for _ in range(n)]
q = deque()
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

start_x, start_y = 0, 0
exit_x, exit_y = n-1, m-1

for _ in range(n):
    board.append(list(map(int, list(input()))))

# 최단거리는 bfs, dfs도 구할 수는 있지만, 최솟값을 구할때마다 갱신해야함 + 해봤는데 안됌

# x좌표, y좌표, 방문한 노드 갯수
q.append((start_x, start_y, 1))
visited[start_x][start_y] = True

while q:
    now_x, now_y, visited_node = q.popleft()

    if now_x == exit_x and now_y == exit_y:
        answer = visited_node
        break

    for dx, dy in d:
        new_x, new_y = now_x+dx, now_y+dy

        if 0 <= new_x <= n-1 and 0 <= new_y <= m-1:
            # 괴물이 있는 칸(0) 은 갈 수 없음
            if board[new_x][new_y] == 1 and not visited[new_x][new_y]:
                q.append((new_x, new_y, visited_node + 1))

print(answer)
