# usr/bin/env python
# -*- coding: utf8 -*-
# boj 2110 공유기 설치

import sys
input = sys.stdin.readline

n, c = map(int, input().split())
position = [int(input()) for _ in range(n)]
position.sort()

start,end = 1, position[n-1] - position[0]
result = 0

if c == 2:
    print(position[n - 1] - position[0])
else:
    while(start < end):
        mid = (start + end)//2

        # 첫번째 집에는 무조건 설치
        count = 1
        installed = position[0]

        for i in range(n):
            if position[i] - installed >= mid:
                count += 1
                installed = position[i]    # 공유기 설치
        if count >= c:
            result = mid
            start = mid + 1     # 간격 늘리기
        elif count < c:
            end = mid       # 간격 줄이기
    print(result)