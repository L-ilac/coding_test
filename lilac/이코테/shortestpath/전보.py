import sys
import heapq
n, m, c = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

distance = [sys.maxsize] * (n+1)
distance[c] = 0
q = []

heapq.heappush(q, (0, c))  # 도시까지 최단거리, 도시

while q:
    dist, now = heapq.heappop(q)

    if dist > distance[now]:
        continue

    for i, d in graph[now]:
        tmp_dist = dist + d

        if tmp_dist < distance[i]:
            distance[i] = tmp_dist
            heapq.heappush(q, (tmp_dist, i))

print(distance)

received = n - distance.count(sys.maxsize) + 1 - 1
time = max([i for i in distance if i != sys.maxsize])

print(received, time)
