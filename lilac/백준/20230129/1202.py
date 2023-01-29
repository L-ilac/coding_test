
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
# ! 가방 무게를 기준으로, 가방무게 이하의 모든 보석들중에 가장 비싼거를 골라서 넣는다.
for b in bags:
    while jewels:
        # * 보석의 무게가 가방의 무게보다 작을 경우 후보군에 들어갈 수 있음.
        if b >= jewels[0][0]:
            m, v = heapq.heappop(jewels)

            # * 후보군에 넣을 때는 가치가 높은 순으로 넣는다.
            heapq.heappush(tmp, (-v, m))
        else:
            break

    # * 넣을 수 있는 보석이 없을 수도 있음.
    if tmp:
        result -= heapq.heappop(tmp)[0]


print(result)
