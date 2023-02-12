# 1번회사 -> k번회사 -> x번회사
from collections import deque
import sys

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]


for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


x, k = map(int, input().split())

distance = [[sys.maxsize]*(n+1) for _ in range(n+1)]


def floyd_warshall():
    for i in range(n+1):
        distance[i][i] = 0

    for i in range(1, len(graph)):
        for j in graph[i]:
            distance[i][j] = 1

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                distance[i][j] = min(
                    distance[i][j], distance[i][k] + distance[k][j])


def bfs(start, end):
    visited = [False]*(n+1)
    q = deque()
    q.append((start, 0))

    visited[start] = True

    while q:
        now, step = q.popleft()

        if now == end:
            return step

        for i in graph[now]:
            if not visited[i]:
                q.append((i, step+1))

    return -1


# a = bfs(1, k)
# b = bfs(k, x)


# if a == -1 or b == -1:
#     print(-1)
# else:
#     print(a+b)


floyd_warshall()
result = distance[1][k] + distance[k][x]
if result >= sys.maxsize:
    print(-1)
else:
    print(result)
