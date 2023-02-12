from collections import deque
import sys
r, c = map(int, input().split())

board = []
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

jihun = (0, 0)
fire = []


for i in range(r):
    data = list(input())
    board.append(data)
    for j in range(c):
        if data[j] == "J":
            jihun = (i, j)
        if data[j] == "F":
            fire.append((i, j))


def bfs(start, visited):
    q = deque()
    for start_x, start_y in start:
        q.append((start_x, start_y, 0))
        visited[start_x][start_y] = 0

    while q:
        now_x, now_y, steps = q.popleft()

        for dx, dy in d:
            new_x, new_y = now_x+dx, now_y+dy

            if 0 <= new_x <= r-1 and 0 <= new_y <= c-1 and visited[new_x][new_y] == -1 and board[new_x][new_y] != "#":
                visited[new_x][new_y] = steps+1
                q.append((new_x, new_y, steps+1))


jihun_visited = [[-1]*c for _ in range(r)]
fire_visited = [[-1]*c for _ in range(r)]

bfs([jihun], jihun_visited)
bfs(fire, fire_visited)

# print(jihun_visited)
# print(fire_visited)


min_escape = sys.maxsize
for i in range(0, r):
    if fire_visited[i][0] != -1:
        if jihun_visited[i][0] < fire_visited[i][0] and jihun_visited[i][0] != -1:
            min_escape = min(min_escape, jihun_visited[i][0])
    else:
        if jihun_visited[i][0] != -1:
            min_escape = min(min_escape, jihun_visited[i][0])

    if fire_visited[i][-1] != -1:
        if jihun_visited[i][-1] < fire_visited[i][-1] and jihun_visited[i][-1] != -1:
            min_escape = min(min_escape, jihun_visited[i][-1])
    else:
        if jihun_visited[i][-1] != -1:
            min_escape = min(min_escape, jihun_visited[i][-1])

for j in range(0, c):
    if fire_visited[0][j] != -1:
        if jihun_visited[0][j] < fire_visited[0][j] and jihun_visited[0][j] != -1:
            min_escape = min(min_escape, jihun_visited[0][j])
    else:
        if jihun_visited[0][j] != -1:
            min_escape = min(min_escape, jihun_visited[0][j])

    if fire_visited[-1][j] != -1:
        if jihun_visited[-1][j] < fire_visited[-1][j] and jihun_visited[-1][j] != -1:
            min_escape = min(min_escape, jihun_visited[-1][j])
    else:
        if jihun_visited[-1][j] != -1:
            min_escape = min(min_escape, jihun_visited[-1][j])

if min_escape == sys.maxsize:
    print("IMPOSSIBLE")
else:
    print(min_escape+1)
