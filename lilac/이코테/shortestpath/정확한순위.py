import heapq
import sys
n, m = map(int, input().split())


graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))


def dijkstra(start):
    distance = [sys.maxsize] * (n+1)
    q = []
    distance[start] = 0
    q.append((0, start))

    while q:

        dist, now = heapq.heappop(q)

        if dist > distance[now]:
            continue

        for i, cost in graph[now]:
            tmp = dist + cost

            if tmp < distance[i]:
                distance[i] = tmp
                heapq.heappush(q, (tmp, i))

    return distance


distances = []

for i in range(1, n+1):
    distances.append(dijkstra(i))

smaller = [set() for _ in range(n+1)]
larger = [set() for _ in range(n+1)]

# ! distances[i][j] -> i+1번에서 j번으로 가는 최단거리

for i in range(n):
    for j in range(1, n+1):
        if i+1 == j:
            continue

        if distances[i][j] != sys.maxsize:
            larger[j].add(i+1)
            smaller[i+1].add(j)

cnt = 0


for i in range(1, n+1):
    if len(larger[i]) + len(smaller[i]) == n-1:
        cnt += 1

print(cnt)

# ! 제한시간이 5초라서 플로이드-워셜로 풀어도 문제 없음
