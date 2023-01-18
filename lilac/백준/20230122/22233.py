from collections import defaultdict
import sys
n, m = map(int, input().split())

memo = set()
for _ in range(n):
    memo.add(sys.stdin.readline().rstrip())

for _ in range(m):
    words = sys.stdin.readline().rstrip().split(',')

    for w in words:
        memo.discard(w)  # ! discard 는 집합내에 원소가 없어도 에러를 일으키지 않음

    # ! words를 set으로 만들어서 memo -= words 하면 차집합 연산으로 간단하게 가능

    print(len(memo))
