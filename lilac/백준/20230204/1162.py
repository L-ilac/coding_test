import heapq
import sys

n, m, k = map(int, sys.stdin.readline().rstrip().split())
# distance를 2차원 배열로 선언해서 해당 도로를 포장 했을 때와 안했을 때로 나눈다

q = []
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())

    # 양방향 도로
    graph[a].append((b, c))
    graph[b].append((a, c))


distance = [[sys.maxsize] * (n+1) for _ in range(k+1)]
# ! distance[k][n] -> 1번도시에서 n번 도시까지 k개의 도로를 포장해서 가는 최단거리

for i in range(k+1):
    distance[i][1] = 0

# 만약에 특정 도로를 포장하면 거리가 0이 된다.
# 출발은 무조건 1번 도시(서울)

heapq.heappush(q, (0, 1, 0))  # 거리, 도시번호, 통과한 포장 도로 갯수

while q:
    dist, now, paved = heapq.heappop(q)

    if dist > distance[paved][now]:
        continue

    for city, cost in graph[now]:
        tmp = dist+cost

        if tmp < distance[paved][city]:
            distance[paved][city] = tmp
            heapq.heappush(q, (tmp, city, paved))

        if paved < k:
            if dist < distance[paved+1][city]:
                distance[paved+1][city] = dist
                heapq.heappush(q, (dist, city, paved+1))


# print(distance)
#! 포장해하는 도로 수 k가 전체 도로 m보다 클수도 있다. 그래서 문제에서 k개 이하라고 한것.
print(min([distance[i][n] for i in range(0, k+1)]))


# 0 1 0
# 0 2 1
# 0 3 1
# 1 3 0
# 10 2 0
# 10 4 1
