# 트리에서 두 노드 사이의 경로 중 가장 긴 길이를 트리의 지름이라고 한다.
# 입력으로 루트가 있는 트리를 가중치가 있는 간선들로 줄 때, 트리의 지름을 구해서 출력하는 프로그램을 작성하시오.

# ! 접근법
# ! 지름의 양 끝점 중 둘중 하나는, 어떤 점에서든 가장 먼 점이다. (예시 그림을 보면 이해가 쉬움)
# ! 따라서 아무점(a)을 잡고, 가장 먼거리에 있는 점(b)을 구한다.
# ! b는 지름을 구성하는 점 중 하나이기때문에, b에서 가장 먼거리에 있는 점(c) 까지의 거리가 지름이다.

import sys
from collections import deque
sys.setrecursionlimit(10002)
n = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    # 부모, 자식, 가중치 순
    parent, child, weight = map(int, sys.stdin.readline().split())
    # 부모 노드
    # parent -> child 경로가 비용이 weight
    # 양방향으로 그래프 설정
    graph[parent].append((child, weight))
    graph[child].append((parent, weight))


visit = [False] * (n+1)
max_route = 0
far_node = 0


def dfs(start, total):
    global max_route, far_node
    visit[start] = True

    # ! 가장 먼거리에 있는 노드를 저장하는 로직
    if total > max_route:
        max_route = total
        far_node = start

    # ! 현재 방문 노드 기준으로 인접한 방문하지 않은 모든 노드에 대해 동일하게 dfs 수행
    for node, weight in graph[start]:
        if not visit[node]:
            dfs(node, total+weight)


def bfs(start):
    q = deque()
    visited = [False] * (n+1)

    q.append((start, 0))
    visited[start] = True

    far_node = 0
    max_route = 0

    while q:
        now, route = q.popleft()

        if route > max_route:
            max_route = route
            far_node = now

        for node, weight in graph[now]:
            if not visited[node]:
                visited[node] = True
                q.append((node, weight+route))

    return far_node, max_route


dfs(1, 0)
# far_node, max_route = bfs(1)

visit = [False] * (n+1)
max_route = 0
dfs(far_node, 0)
# far_node, max_route = bfs(far_node)

print(max_route)
