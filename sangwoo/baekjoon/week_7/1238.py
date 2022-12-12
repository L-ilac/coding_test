# 파티
from collections import defaultdict
from heapq import heappush, heappop

N, M, X = map(int, input().split())

graph = defaultdict(list)
for _ in range(M):
    A, B, T = map(int, input().split())
    graph[A].append((B, T))

distance_origin = {node: float('inf') for node in graph}

def get_distance(start, end):
    distance = distance_origin.copy()
    distance[start] = 0
    queue = []
    heappush(queue, [distance[start], start])

    while queue:
        dist, n = heappop(queue)
        if distance[n] < dist:
            continue

        for new_n, new_dist in graph[n]:
            tmp_distance = dist + new_dist
            if tmp_distance < distance[new_n]:
                distance[new_n] = tmp_distance
                heappush(queue, [distance[new_n], new_n])
    return  distance[end]

res = 0
for i in range(1, N+1):
    if i == X:
        continue

    num1 = get_distance(i, X)
    num2 = get_distance(X, i)

    res = max(res, num1 + num2)
print(res)