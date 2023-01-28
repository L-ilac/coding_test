#!/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 1522 문자열교환

import sys

string = sys.stdin.readline().strip()
a_cnt = string.count('a')
str_len = len(string)
b_cnt = 1000

string += string[:-1]

for i in range(str_len):
    b_cnt_tmp = string[i : a_cnt + i].count('b')
    if b_cnt_tmp < b_cnt:
        b_cnt = b_cnt_tmp
print(b_cnt)