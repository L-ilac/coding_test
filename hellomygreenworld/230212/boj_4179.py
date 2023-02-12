# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 4179 불!

from collections import deque

r, c = map(int, input().split())
graph = []
for i in range(r):
    graph.append(list(input().strip()))

for i in range(r):
    for j in range(c):
        if graph[i][j] == 'J':
            loc_j = (i, j)
        elif graph[i][j] == 'F':
            graph[i][j] = 1
            loc_f = (i, j)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(j, f):
    result = 0
    queue_j = deque([j])
    queue_f = deque([f])

    # J가 맵을 빠져나갈 때까지
    while queue_j:
        j_x, j_y = queue_j.popleft()

        for i in range(4):

            j_nx = j_x + dx[i]
            j_ny = j_y + dy[i]

            if j_nx < 0 or j_ny < 0 or j_nx > r - 1 or j_ny > c - 1:
                result += 1
                return result

            if graph[j_nx][j_ny] == '.':
                graph[j_nx][j_ny] = 'J'
                graph[j_x][j_y] = '.'
                queue_j.append((j_nx, j_ny))
                result += 1

        # 이전에 확산된 불을 모두 4방향으로 확산시켜야 함
        cur_fire_value = graph[queue_f[0][0]][queue_f[0][1]]
        while graph[queue_f[0][0]][queue_f[0][1]] == cur_fire_value:
            f_x, f_y = queue_f.popleft()

            for i in range(4):
                f_nx = f_x + dx[i]
                f_ny = f_y + dy[i]

                if f_nx < 0 or f_ny < 0 or f_nx > r - 1 or f_ny > c - 1:
                    continue

                if graph[f_nx][f_ny] != '#':
                    graph[f_nx][f_ny] = graph[f_x][f_y] + 1
                    queue_f.append((f_nx, f_ny))

    return "IMPOSSIBLE"

print(bfs(loc_j, loc_f))
