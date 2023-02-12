# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 14226 이모티콘

import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
result = 0

graph = [[0 for _ in range(n + 1)] for __ in range(n + 1)]
graph[1][0] = 0
queue = deque([(1, 0)])

while queue:
    s, c = queue.popleft()

    # 복사하기
    if graph[s][s] == 0:
        graph[s][s] = graph[s][c] + 1
        queue.append((s, s))

    # 붙여넣기
    if s + c <= n and graph[s + c][c] == 0:
        graph[s + c][c] = graph[s][c] + 1
        queue.append((s + c, c))

    # 삭제하기
    if s > 0 and graph[s - 1][c] == 0:
        graph[s - 1][c] = graph[s][c] + 1
        queue.append((s - 1, c))

print(min([i for i in graph[n] if i != 0]))