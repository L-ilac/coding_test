from itertools import combinations


height = []

for _ in range(9):
    height.append(int(input()))

comb = list(combinations(height, 7))

for c in comb:
    if sum(c) == 100:
        for i in sorted(list(c)):
            print(i)
        break
