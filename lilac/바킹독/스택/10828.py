import sys

n = int(input())

stack = []

for _ in range(n):
    op = list(sys.stdin.readline().rstrip().split())

    if op[0] == "push":
        stack.append(op[1])
    elif op[0] == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif op[0] == "size":
        print(len(stack))
    elif op[0] == "empty":
        if stack:
            print(0)
        else:
            print(1)
    elif op[0] == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)
