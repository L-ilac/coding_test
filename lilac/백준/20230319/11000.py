import heapq
import sys

n = int(input())


lecture = []

for _ in range(n):
    s, t, = map(int, sys.stdin.readline().split())
    heapq.heappush(lecture, (s, t))

plan = []
while lecture:
    s, t = heapq.heappop(lecture)

    if plan:
        if plan[0][0] <= s:
            heapq.heappop(plan)

    heapq.heappush(plan, (t, s))


print(len(plan))
