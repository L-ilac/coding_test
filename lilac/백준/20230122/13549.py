import heapq
import sys
n, k = map(int, input().split())

# 순간이동은 x -> 2x 0초
# 걷기는 x-1 <- x -> x+1 1초

# 가장 최단시간에 움직이려면, 순간이동을 최대한 잘 사용


q = []
time = [sys.maxsize] * 100001

heapq.heappush(q, (0, n))
time[n] = 0

while q:
    cost, now = heapq.heappop(q)

    if now == k:
        print(cost)
        break

    if cost > time[now]:
        continue

    tmp, new = cost+1, now+1
    if 0 <= new <= 100000 and tmp < time[new]:
        time[new] = tmp
        heapq.heappush(q, (tmp, new))

    tmp, new = cost+1, now-1
    if 0 <= new <= 100000 and tmp < time[new]:
        time[new] = tmp
        heapq.heappush(q, (tmp, new))

    tmp, new = cost, now*2
    if 0 <= new <= 100000 and tmp < time[new]:
        time[new] = tmp
        heapq.heappush(q, (tmp, new))

# ! 다익스트라 or 0-1 bfs
