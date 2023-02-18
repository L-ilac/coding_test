# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 1062 가르침

# ! 단어 개수 50개 이하, 알파벳 26개

import sys
from itertools import combinations
from copy import deepcopy

input = sys.stdin.readline

n, k = map(int, input().split())
words = []
for i in range(n):
    words.append(input().rstrip()[4:-4])

def readable(word, alphabets):
    for c in word:
        if not alphabets[ord(c) - ord('a')]:
            return 0
    return 1

result = 0
cnt = k - 5
if cnt < 0:
    print(0)
    exit(0)

combinations = combinations([chr(i) for i in range(97, 97+26) if chr(i) not in "antic"], cnt)

result = 0
for combination in combinations:
    cnt = 0
    alphabets = [1 if chr(i + 97) in "antic" else 0 for i in range(26)]
    for c in combination:
        alphabets[ord(c) - ord('a')] = 1
    for word in words:
        cnt += readable(word, alphabets)
    if cnt > result:
        result = cnt

print(result)
