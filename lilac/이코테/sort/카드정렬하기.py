import heapq
import sys
n = int(input())
data = []

for _ in range(n):
    heapq.heappush(data, int(sys.stdin.readline()))


total = 0
while len(data) > 1:
    n, m = heapq.heappop(data), heapq.heappop(data)
    total += n+m
    heapq.heappush(data, n+m)

print(total)
