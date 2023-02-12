# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 1202 보석 도둑
# https://eunbin00.tistory.com/144

import sys
import heapq

input = sys.stdin.readline

n, k = map(int, input().split())

jewelries = [tuple(map(int, input().split())) for _ in range(n)]
bags = [int(input()) for _ in range(k)]

jewelries.sort()
bags.sort()

tmp = []
result = 0

for bag in bags:
    while jewelries and jewelries[0][0] <= bag:
        heapq.heappush(tmp, -jewelries[0][-1])
        heapq.heappop(jewelries)

    if tmp:
        result -= heapq.heappop(tmp)

print(result)