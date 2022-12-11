# dijkstra + costs ?
# 최소비용이 갱신된 값에 대해서만 큐에 다시 넣는다
import heapq
import sys

INF = 1e9


def dijkstra(graph, n):
    q = []
    direction = [(0, 1), (0, -1), (-1, 0), (1, 0)]  # 상하좌우
    costs = [[INF] * n for _ in range(n)]

    heapq.heappush(q, (graph[0][0], 0, 0))  # 해당 좌표까지 잃은 돈(최소값), x좌표, y좌표

    costs[0][0] = graph[0][0]

    while q:
        cost, x, y = heapq.heappop(q)

        if cost < costs[y][x]:
            continue

        for dx, dy in direction:
            new_x, new_y = x+dx, y+dy

            if -1 < new_x < n and -1 < new_y < n:
                new_cost = cost + graph[new_y][new_x]

                if new_cost < costs[new_y][new_x]:
                    costs[new_y][new_x] = new_cost
                    heapq.heappush(q, (new_cost, new_x, new_y))

    return costs[-1][-1]


graphs = []

while True:
    n = int(input())  # 맵 사이즈

    if n == 0:
        break

    graph = []
    for _ in range(n):
        graph.append(list(map(int, sys.stdin.readline().split())))
    graphs.append(graph)


for idx, graph in enumerate(graphs, start=1):
    print('Problem', str(idx)+':', dijkstra(graph, len(graph)))
