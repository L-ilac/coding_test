# 문제 풀이 접근법
# 1. 목적지는 x로 정해져있음
# 2. 모든 집 -> x 로 가는 최단거리를 계산(다익스트라)
# 3. x -> 모든 집으로 가는 최단거리를 계산(다익스트라)
# 4. 2번과 3번의 결과를 합산(1 -> x -> 1: 1번 -> x 최단거리 + x -> 1번 최단거리)
# 시간제한 때문에 힙을 이용한 다익스트라 알고리즘을 사용해야함

import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, m, x = map(int, input().split())

graph = [[] for _ in range(n+1)]


for _ in range(m):
    start, end, c = map(int, input().split())
    graph[start].append((end, c))


def dijkstra(start):
    q = []
    costs = [INF] * (n+1)

    heapq.heappush(q, (0, start))
    costs[start] = 0
    while q:
        cost, now = heapq.heappop(q)

        if costs[now] < cost:
            continue

        for i in graph[now]:
            tmp = cost + i[1]
            if tmp < costs[i[0]]:
                costs[i[0]] = tmp
                heapq.heappush(q, (tmp, i[0]))

    return costs


toParty = []
fromParty = dijkstra(x)

for i in range(1, n+1):
    result = dijkstra(i)
    toParty.append(result[x])
    toParty[i-1] += fromParty[i]

print(max(toParty))
