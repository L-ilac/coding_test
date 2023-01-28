# !usr/bin/env python
# -*- coding: utf-8 -*-
# boj 20437 문자열게임2

import sys
from collections import defaultdict

def boj_20437(string, k):

    character_idx = defaultdict(list)

    min = 100000
    max = 0

    for i in range(len(string)):
        if string.count(string[i]) >= k:
            character_idx[string[i]].append(i)

    for ch in character_idx:
        lst = character_idx[ch]
        for i in range(len(lst) - k + 1):
            cnt = lst[i + k - 1] - lst[i] + 1
            if cnt < min:
                min = cnt
            if cnt > max:
                max = cnt

    if (min == 100000 and max == 0):
        return (-1,)
    else:
        return (min, max)

if __name__ == "__main__":
    test_case = int(sys.stdin.readline().strip())

    for _ in range(test_case):
        string = sys.stdin.readline().strip()
        k = int(sys.stdin.readline().strip())
        print(*boj_20437(string, k))