# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 2252 줄 세우기

import sys
from collections import deque
from collections import defaultdict

input = sys.stdin.readline

# ! 시간 초과난 풀이
n, m = map(int, input().split())
parent = [[i] for i in range(n + 1)]

for i in range(m):
    small, big = map(int, input().split())
    parent[small].append(big)

# parent 확정하기
for i in range(1, len(parent)):
    if len(parent[i]) == 1:
        parent[i] = parent[i][0]
    else:
        parent[i].remove(i)
        if len(parent[i]) != 1:
            for x in parent[i]:
                if parent[x] in parent[i]:
                    parent[i].remove(parent[x])
        parent[i] = parent[i][0]

queue = deque()
result = []
for i in range(1, len(parent)):
    if parent[i] == i:
        queue.append(i)

while queue:
    v = queue.popleft()
    result.append(v)
    for i in range(1, len(parent)):
        if parent[i] == v and i != v:
            queue.append(i)

result.reverse()
print(*result)


# * 위상 정렬 알고리즘을 이용한 풀이
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
in_degree = defaultdict(int)

for i in range(m):
    small, big = map(int, input().split())
    graph[small].append(big)
    in_degree[big] += 1

queue = deque()
for i in range(1, len(graph)):
    if in_degree[i] == 0:
        queue.append(i)

while queue:
    v = queue.popleft()
    print(v, end = ' ')
    for i in graph[v]:
        in_degree[i] -= 1
        if in_degree[i] == 0:
            queue.append(i)