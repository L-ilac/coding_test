from collections import deque
n = int(input())
towers = list(map(int, input().split()))

stack = []
received = [0] * n


while towers:
    now = towers.pop()

    if not stack:
        stack.append((now, len(towers)))
    else:
        if stack[-1][0] <= now:
            while stack and stack[-1][0] <= now:
                h, idx = stack.pop()
                received[idx] = len(towers)+1

            stack.append((now, len(towers)))
        else:
            stack.append((now, len(towers)))


# print(stack)

while stack:
    h, idx = stack.pop()
    received[idx] = 0

print(*received)
