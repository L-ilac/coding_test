n = int(input())

towers = list(map(int, input().split()))

answer = []
stack = []

while towers:
    now = towers.pop()

    if towers and now < towers[-1]:
        stack.append((now, len(towers) + 1))

        while stack and stack[-1][0] < towers[-1]:
            tmp = stack.pop()
            answer.append((len(towers), tmp[1]))
    else:
        stack.append((now, len(towers) + 1))

while stack:
    tmp = stack.pop()
    answer.append((0, tmp[1]))


answer.sort(key=lambda x: x[1])

print(*[a[0] for a in answer])
