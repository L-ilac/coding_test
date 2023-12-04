import sys

n = int(sys.stdin.readline().rstrip())


stack = []
op = []

pos = 1


for _ in range(n):
    tmp = int(sys.stdin.readline().rstrip())

    if stack and stack[-1] == tmp:
        stack.pop()
        op.append("-")
    else:
        if tmp < pos:
            print("NO")
            exit()
        for i in range(pos, tmp + 1):
            stack.append(i)
            op.append("+")

        stack.pop()
        op.append("-")

        pos = tmp + 1

for i in op:
    print(i)
