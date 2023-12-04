from collections import deque
import sys

n = int(input())

building = deque()
for _ in range(n):
    building.append(int(sys.stdin.readline().rstrip()))

answer = 0
stack = []

while building:
    h = building.popleft()

    if not stack:
        stack.append(h)
    else:
        if stack[-1] > h:
            stack.append(h)
        else:
            cnt = 0
            while stack and stack[-1] <= h:
                answer += cnt
                cnt += 1
                stack.pop()

            answer += len(stack) * cnt

            stack.append(h)

if stack:
    for i in range(len(stack) - 1, 0, -1):
        answer += i

# print(stack)
print(answer)
