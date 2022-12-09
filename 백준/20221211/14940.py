from collections import deque

n, m = map(int, input().split())
q = deque()

graph = []
start_x = 0
start_y = 0
direction = [(0, 1), (0, -1), (-1, 0), (1, 0)]  # 상하좌우
distance = [[0] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]


for _ in range(n):
    graph.append(list(map(int, input().split())))


for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            start_x = j
            start_y = i


visited[start_y][start_x] = True
q.append((start_x, start_y))

while q:
    now_x, now_y = q.popleft()

    for dx, dy in direction:
        new_x, new_y = now_x + dx, now_y + dy

        if -1 < new_x < m and -1 < new_y < n:
            if not visited[new_y][new_x] and graph[new_y][new_x] == 1:
                distance[new_y][new_x] = distance[now_y][now_x] + 1
                q.append((new_x, new_y))
                visited[new_y][new_x] = True


for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            distance[i][j] = -1

for i in distance:
    print(" ".join(list(map(str, i))))
