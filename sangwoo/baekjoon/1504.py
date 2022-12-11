# 특정한 최단 경로
from heapq import heappop, heappush

N, E = map(int, input().split())
graph = {x: [] for x in range(1, N+1)}

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1,v2 = map(int, input().split())

route = [[1, v1, v2, N], [1, v2, v1, N]]

res = float('inf')
for r in route:
    
    tmp_res = 0
    for i in range(len(r)-1):
        queue = []
        x, y = r[i], r[i+1]

        distance = {node: float('inf') for node in graph}
        distance[x] = 0
        heappush(queue, (distance[x], x))

        while queue:
            dist, node = heappop(queue)
            if distance[node] < dist:
                continue
            
            if node in r[:i]:
                continue

            for new_n, new_dist in graph[node]:
                tmp_dist = dist + new_dist
                if tmp_dist < distance[new_n]:
                    distance[new_n] = tmp_dist
                    heappush(queue, (distance[new_n], new_n))
        
        tmp_res += distance[y]
    res = min(tmp_res, res)

if res == float('inf'):
    print(-1)
else:
    print(res)


# 경로를 2가지로 나눠서 생각해봄
# 1. 1 -> v1 -> v2 -> N
# 2. 1 -> v2 -> v1 -> N

# 1에서 v1으로 가는 최단경로, v1에서 v2로 가는 최단경로 ... 
# 이런식으로 각 경우의 최단 경로를 모두 구하고

# 두가지 경로중 최소를 출력