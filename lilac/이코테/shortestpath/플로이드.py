import sys
n = int(input())
m = int(input())

distance = [[sys.maxsize]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a, b, c, = map(int, sys.stdin.readline().rstrip().split())
    distance[a][b] = min(distance[a][b], c)

for i in range(1, n+1):
    distance[i][i] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            distance[i][j] = min(
                distance[i][j], distance[i][k] + distance[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        if distance[i][j] == sys.maxsize:
            distance[i][j] = 0


for i in range(1, n+1):
    print(*distance[i][1:])
