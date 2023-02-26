from bisect import bisect_right
from itertools import combinations
n, c = map(int, input().split())

items = list(map(int, input().split()))

items_1 = items[:n//2]
items_2 = items[n//2:]

sum_1 = []
sum_2 = []

for i in range(len(items_1)+1):
    comb = combinations(items_1, i)

    for cb in comb:
        sum_1.append(sum(cb))

for i in range(len(items_2)+1):
    comb = combinations(items_2, i)

    for cb in comb:
        sum_2.append(sum(cb))

sum_1.sort()

answer = 0
for s in sum_2:

    if s > c:
        continue

    cnt = bisect_right(sum_1, c-s)
    answer += cnt


print(answer)
