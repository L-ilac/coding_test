# bfs 를 돌면서 외부공기가 치즈에 닿으면 +1 해주고, +2 이상인 값을 가지는 치즈에 대해서만 녹이기
from collections import deque
n, m = map(int, input().split())

cheese = []

for _ in range(n):
    data = list(map(int, input().split()))
    cheese.append(data)


def bfs():
    q = deque()

    d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    visited = [[0]*m for _ in range(n)]

    q.append((0, 0))

    while q:
        nowx, nowy = q.popleft()

        for dx, dy in d:
            newx, newy = nowx+dx, nowy+dy

            if 0 <= newx <= n-1 and 0 <= newy <= m-1:
                if cheese[newx][newy] == 0 and visited[newx][newy] == 0:
                    visited[newx][newy] = 1
                    q.append((newx, newy))
                elif cheese[newx][newy] == 1:
                    visited[newx][newy] += 1

    # 외부공기로부터 2번이상 접촉당한 치즈는 녹는다.
    cnt = 0

    for i in range(n):
        for j in range(m):
            if visited[i][j] >= 2:
                cheese[i][j] = 0

            if cheese[i][j] == 1:
                cnt += 1

    return cnt


time = 0
while True:
    flag = bfs()

    time += 1

    if flag == 0:
        break

print(time)


# ! 2636 풀때 사용했던 방법으로도 맞긴했음. 근데 bfs로 푸는게 더 간결함
# ! bfs의 visited를 굳이 false,true 2분법적인 값이 아닌, 정수의 형태로 사용하면 편한 경우가 있음.
