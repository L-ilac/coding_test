from collections import deque
import sys

initial = list(input())

left = deque(initial)
right = deque()


m = int(input())

for _ in range(m):
    op = list(sys.stdin.readline().rstrip().split())
    
    if op[0] == "P":
        left.append(op[1])
    elif op[0] == "L":
        if not left:
            continue
        right.appendleft(left.pop())
    elif op[0] == "D":
        if not right:
            continue
        left.append(right.popleft())
    else:
        if not left:
            continue
        left.pop()
        

print(''.join(left) + ''.join(right))