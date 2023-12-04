import sys

n = int(input())
A = list(map(int, sys.stdin.readline().rstrip().split()))

answer = []
stack = []
for i in range(n):
    if not stack:
        stack.append((i, A[i]))
    else:
        while stack and stack[-1][1] < A[i]:
            tmp = stack.pop()
            answer.append((tmp[0], A[i]))

        stack.append((i, A[i]))

while stack:
    tmp = stack.pop()
    answer.append((tmp[0], -1))

answer.sort()
print(*[a[1] for a in answer])
