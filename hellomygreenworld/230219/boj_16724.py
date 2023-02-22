# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 16724 피리 부는 사나이


from collections import deque

n, m = map(int, input().split())

board = []
for _ in range(n):
    board.append(list(map(str, input())))

# 방향 설정
movements = [(-1, 0), (1, 0), (0, -1), (0, 1)]

parent = [i for i in range(n * m)]

def find(x):
    global parent
    if parent[x] != x:
        parent[x] = find(parent[x])
        return parent[x]
    return x

def union(x, y):
    global parent
    visited[x], visited[y] = True, True
    x = find(x)
    y = find(y)
    if x == y:
        return
    if x > y:
        parent[x] = y
        parent = [y if i == x else i for i in parent]
    else:
        parent[y] = x
        parent = [x if i == y else i for i in parent]

queue = deque()
visited = [False for _ in range(n * m)]

while False in visited:
    idx = [idx for idx, t in enumerate(visited) if t == False][0]
    queue.append((idx // m, idx % m))
    while queue:
        x, y = queue.popleft()
        cur = x * m + y
        if board[x][y] == 'U':
            dx, dy = movements[0]
            n = -m
        elif board[x][y] == 'D':
            dx, dy = movements[1]
            n = +m
        elif board[x][y] == 'L':
            dx, dy = movements[2]
            n = -1
        else:
            dx, dy = movements[3]
            n = +1

        nx, ny = x + dx, y + dy

        if visited[nx * m + ny] == False:
            queue.append((nx, ny))
        visited[x * m + y] = True
        visited[nx * m + ny] = True
        union(cur, cur + n)


# for i in range(n):
#     for j in range(m):
#         cur = i * m + j
#         # if visited[cur] == True:
#             # continue
#         if board[i][j] == 'U':
#             union(cur, cur - m)
#         elif board[i][j] == 'D':
#             union(cur, cur + m)
#         elif board[i][j] == 'R':
#             union(cur, cur + 1)
#         else:
#             union(cur, cur - 1)

print(len(set(parent)))