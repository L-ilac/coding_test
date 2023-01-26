
# !  가방에는 최대 한개의 보석만 넣을 수 있다.
import sys
import heapq
n, k = map(int, input().split())

jewels = []
bags = []

for _ in range(n):
    m, v = map(int, sys.stdin.readline().rstrip().split())
    heapq.heappush(jewels, (m, v))

for _ in range(k):
    c = int(sys.stdin.readline().rstrip())
    bags.append(c)

bags.sort()

result = 0
tmp = []
for b in bags:
    while jewels:
        if b >= jewels[0][0]:
            m, v = heapq.heappop(jewels)
            heapq.heappush(tmp, (-v, m))
        else:
            break

    if tmp:
        result -= heapq.heappop(tmp)[0]


print(result)


# ! 가방을 기준으로, 가방무게 이하의 모든 보석들중에 가장 비싼거를 골라서 넣는다.
# ! 넣은 보석은 다시 넣을 수 없음
