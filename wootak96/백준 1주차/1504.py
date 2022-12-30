import sys
from heapq import heappush
from heapq import heappop
INF = int(1e9)
def dijkstra(start, end):
    dis = [INF] * (N + 1)
    dis[start] = 0
    q = [[0, start]]
    while q:
        k, u = heappop(q)
        if k <= dis[u]:
            for w, v in G[u]:
                if dis[v] > dis[u] + w:
                    dis[v] = dis[u] + w
                    heappush(q, [dis[v], v])
    return dis[end]

N, E = map(int, input().split())
G = [[] for _ in range(N + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    G[u].append([w, v]) 
    G[v].append([w, u])

destination1, destination2 = map(int, input().split())

# 1 -> destination1 -> destination2 -> N
path1 = dijkstra(1, destination1) + dijkstra(destination1, destination2) + dijkstra(destination2, N)
# 1 -> destination2 -> destination1 -> N
path2 = dijkstra(1, destination2) + dijkstra(destination2, destination1) + dijkstra(destination1, N)

if path1 >= INF and path2 >= INF:
    print(-1)
else:
    print(min(path1, path2))
