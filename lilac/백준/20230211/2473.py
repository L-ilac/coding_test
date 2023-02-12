import sys
from bisect import bisect_left
n = int(input())
solutions = list(map(int, input().split()))

solutions.sort()

# ! 서로 다른 세 개의 용액을 더해서 0에 가장 가까운 용액 만들기
# ! 세 용액
