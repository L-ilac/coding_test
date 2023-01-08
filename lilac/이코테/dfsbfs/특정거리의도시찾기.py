import heapq
import sys
from collections import deque

n, m, k, x = map(int, input().split())


graph = [[] for _ in range(n+1)]
visited = [False] * (n + 1)


inf = sys.maxsize
distance = [inf] * (n+1)

q = deque()

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

q.append((x, 0))
visited[x] = True

result = []
while q:
    now, dist = q.popleft()

    if dist == k:
        result.append(now)

    if dist > k:
        break

    for i in graph[now]:
        if not visited[i]:
            visited[i] = True
            q.append((i, dist+1))

# ! 다익스트라
# heapq.heappush(q, (0, x))
# distance[x] = 0

# result = []

# while q:
#     dist, now = heapq.heappop(q)

#     if dist == k:
#         result.append(now)

#     if dist > distance[now]:
#         continue

#     for i in graph[now]:
#         tmp = dist + 1

#         if tmp < distance[i]:
#             distance[i] = tmp
#             heapq.heappush(q, (tmp, i))


if not result:
    print(-1)
else:
    result.sort()
    for i in result:
        print(i)

# ! dfs + 백트래킹?
