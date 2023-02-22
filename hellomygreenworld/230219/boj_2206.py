# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 2206 벽 부수고 이동하기

import sys
from collections import deque
from copy import deepcopy

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

visited = [[[0, 0] for _ in range(m)] for __ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    queue = deque([(0, 0, 0)])
    visited[0][0][0] = 1

    while queue:
        x, y, wall = queue.popleft()
        if x == n - 1 and y == m - 1:
            return visited[x][y][wall]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx > n - 1 or ny > m - 1:
                continue

            # 벽을 부수지 않고 이동 (통로)
            if graph[nx][ny] == 0 and visited[nx][ny][wall] == 0:
                queue.append((nx, ny, wall))
                visited[nx][ny][wall] = visited[x][y][wall] + 1

            # 벽을 부수고 이동 (벽)
            if wall == 0 and graph[nx][ny] == 1:
                queue.append((nx, ny, 1))
                visited[nx][ny][1] = visited[x][y][wall] + 1

    return -1

print(bfs())