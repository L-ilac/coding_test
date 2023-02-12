# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 1543 문서 검색

import sys
input = sys.stdin.readline

document = input().strip()
word = input().strip()
result = 0
i = 0

while i < len(document) - len(word) + 1:
    if (document[i : len(word) + i] == word):
        result += 1
        i += len(word)
    else:
        i += 1

print(result)
