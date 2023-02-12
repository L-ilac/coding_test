# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 16234 인구이동

from collections import deque

n, l, r = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(start):
    queue = deque([start])
    population, count = 0, 0

    while queue:
        united_group = deque()
        x, y = queue.popleft()
        visited[x][y] = True
        united_group.append((x, y))
        population += graph[x][y]
        count += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx > n - 1 or ny > n - 1:
                continue

            diff = abs(graph[x][y] - graph[nx][ny])
            if diff >= l and diff <= r and visited[nx][ny] == False:
                united_group.append((ny, ny))
                population += graph[nx][ny]
                count += 1

    while united_group:
        x, y = united_group.popleft()
        graph[x][y] = population // count

    if count == 1:
        return 0

    return 1

result = 0
while True:
    break_cnt = 0
    for i in range(n):
        for j in range(n):
            visited = [[False for _ in range(n)] for __ in range(n)]
            if visited[i][j] == 0:
                break_cnt += bfs((i, j))
    if break_cnt == 0:
        break
    else:
        result += 1

print(result)