# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 1670 정상회담2

import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * 10001
dp[0] = 1
dp[2] = 1
dp[4] = 2
i = 6

while (i <= n):
    total = 0
    for idx in range(n // 2):
        idx = idx * 2
        total += dp[idx] * dp[i - idx - 2]
    dp[i] = total % 987654321
    i += 2

print(dp[n])