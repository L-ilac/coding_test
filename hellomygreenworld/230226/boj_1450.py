# usr/bin/env python
# -*- coding: utf8 -*-
# boj 1450 냅색 문제

import sys
from itertools import combinations
input = sys.stdin.readline

n, c = map(int, input().split())
obj = list(map(int, input().split()))
left, right = obj[:n//2], obj[n//2:]
sum_combination_left, sum_combination_right = [0], [0]

if n == 1 and obj[0] <= c:
    print(2)
    exit()
if n == 1 and obj[0] > c:
    print(1)
    exit()

for i in range(1, len(left) + 1):
    for sub in combinations(left, i):
        sum_combination_left.append(sum(sub))
sum_combination_left.sort()

for i in range(1, len(right) + 1):
    for sub in combinations(right, i):
        sum_combination_right.append(sum(sub))
sum_combination_right.sort()

answer = 0

# 오른쪽 물건 돌면서 왼쪽 물건 가져올 수 있는 경우의 수 합하기
for i in sum_combination_right:
    if i > c:
        continue
    start = 0
    end = len(sum_combination_left)
    while start < end:
        mid = (start + end) // 2
        # 왼쪽 물건과 오른쪽 물건을 더했을 때 c보다 크면
        if sum_combination_left[mid] + i > c:
            end = mid # 왼쪽 물건에서 가져오는 물건의 무게를 줄이기
        else:
            start = mid + 1 # 왼쪽 물건에서 가져오는 물건의 무게 늘리기
    answer += end # end 인덱스의 값이 가져올 수 있는 물건의 경우의 수

print(answer)