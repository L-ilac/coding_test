from collections import deque

N, a, b = map(int, input().split())

buildings = deque()

if a >= b:
    for i in range(1, a+1):
        buildings.append(i)

    for i in range(b-1, 0, -1):
        buildings.append(i)

    for _ in range(N-len(buildings)):
        buildings.appendleft(1)
else:
    for i in range(b, 0, -1):
        buildings.append(i)

    for i in range(a-1, 0, -1):
        buildings.appendleft(i)

    if a == 1:
        for _ in range(N-len(buildings)):
            buildings.insert(1, 1)
    else:
        for _ in range(N-len(buildings)):
            buildings.appendleft(1)


if len(buildings) > N:
    print(-1)
else:
    print(*buildings)
