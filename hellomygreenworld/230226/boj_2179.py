# usr/bin/env python
# -*- coding: utf8 -*-
# boj 2179 비슷한 단어

import sys
from collections import defaultdict

input = sys.stdin.readline
n = int(input().rstrip())
words = [input().rstrip() for _ in range(n)]

word_dict = defaultdict(list)

for word in words:
    word_dict[word[0]].append(word)

result = 0
for key, value in word_dict.items():
    if len(word_dict[key]) == 1:
        continue

    for i in range(len(value) - 1):
        for j in range(i + 1, len(value)):
            l = min(len(value[i]), len(value[j]))
            prefix = len([value[j][idx] for idx in range(l) if value[i][idx] == value[j][idx]])
            if prefix > result:
                result = prefix
                answer = [value[i], value[j]]

print(answer[0])
print(answer[1])