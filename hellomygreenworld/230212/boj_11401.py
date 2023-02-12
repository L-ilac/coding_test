# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 11401 이항계수3

import sys
input = sys.stdin.readline

div = 1000000007

def power(base, exponent):
    if exponent == 0:
        return 1
    if exponent == 1:
        return base

    x = power(base, exponent // 2)
    if exponent % 2 == 0:
        return x * x % div
    else:
        return x * x * base % div

n, k = map(int, input().split())
permutation = [1 for _ in range(n + 1)]

for i in range(2, n + 1):
    permutation[i] = (permutation[i - 1] * i) % div

print(int(permutation[n] * power(permutation[n - k] * permutation[k], div - 2) % div))
 # power(permutation[n - k] * permutation[k], div - 2) % div == permunation[n - k] * permuataion[k] % div