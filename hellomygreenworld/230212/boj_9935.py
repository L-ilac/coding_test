# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 9935 문자열 폭발

import sys
from collections import defaultdict
from collections import deque

input = sys.stdin.readline

str = list(input().strip())
bomb = list(input().strip())
check = True

while check == True:
    check = False
    for i in range(len(str)):
        ch = str.pop(0)
        str.append(ch)
        if ch == bomb[-1] and str[-len(bomb):] == bomb:
            str = str[:-len(bomb)]
            check = True

if not str:
    print("FRULA")
else:
    print(str)