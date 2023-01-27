# -*- coding: utf-8 -*-
# boj 1743 문서 검색

import sys

if __name__ == "__main__":
    document = sys.stdin.readline().strip()
    word = sys.stdin.readline().strip()
    result = 0
    i = 0

    while i <= len(document) - len(word):
        if (document[i : len(word) + i] == word):
            result += 1
            i += len(word)
        else:
            i += 1
            
    print(result)

