# 1 ~ N 으로 가는데, 두 정점을 무조건 지나야함. 두 정점을 a ,b 라고 했을 때,
# (1 ~ a) + (a ~ b) + (b ~ N) 나 (1 ~ b) + (b ~ a) + (a ~ N) 중 최솟값.
# 경로가 존재하지 않는다면, -1. 즉 저 3개의 항 중에 INF가 하나라도 있으면 -1
# 방향성이 없는 그래프이므로 a~b 와 b~a는 똑같다.

import sys
import heapq

INF = 1e9

n, e = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]

# graph setting
for _ in range(e):
    src, dst, cost = map(int, sys.stdin.readline().split())
    graph[src].append((dst, cost))
    graph[dst].append((src, cost))


a, b = map(int, sys.stdin.readline().split())  # 반드시 지나야하는 두 정점


def dijkstra(start):
    q = []
    distance = [INF] * (n+1)

    heapq.heappush(q, (0, start))  # (cost, node_index)
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if dist < distance[now]:
            continue

        for node in graph[now]:
            new_dist = distance[now] + node[1]

            if new_dist < distance[node[0]]:
                distance[node[0]] = new_dist
                heapq.heappush(q, (new_dist, node[0]))

    return distance

# dijkstra(start) -> dijkstra(start, end) 형태로 특정 출발점에서 특정 도착점까지 가는 거리를 반환하는 형태로 사용해도 된다.


distance_1 = dijkstra(1)
distance_a = dijkstra(a)
distance_b = dijkstra(b)

start_to_a = distance_1[a]
start_to_b = distance_1[b]

a_to_b = distance_a[b]

a_to_end = distance_a[n]
b_to_end = distance_b[n]

answer = min((start_to_a + a_to_b + b_to_end),
             (start_to_b + a_to_b + a_to_end))

if answer >= INF:
    print(-1)
else:
    print(answer)
