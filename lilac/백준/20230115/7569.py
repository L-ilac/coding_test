# y x z
import sys
from collections import deque
m, n, h = map(int, input().split())

tomato = []
ripe = []  # 맨처음에 익어있던 토마토 위치
remain = 0  # 맨처음에 남아있던 안익은 토마토 갯수
d = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

for k in range(h):
    rack = []
    for i in range(n):
        data = list(map(int, sys.stdin.readline().split()))
        for j in range(m):
            if data[j] == 1:
                ripe.append((k, i, j))

        remain += data.count(0)
        rack.append(data)
    tomato.append(rack)


def bfs(ripe):
    q = deque(ripe)
    tmp = set()

    while q:
        nowz, nowx, nowy = q.popleft()
        # visited[nowz][nowx][nowy] = True

        for dz, dx, dy in d:
            newz, newx, newy = nowz+dz, nowx+dx, nowy+dy

            if 0 <= newz <= h-1 and 0 <= newx <= n-1 and 0 <= newy <= m-1:
                if tomato[newz][newx][newy] == 0:
                    tomato[newz][newx][newy] = 1
                    tmp.add((newz, newx, newy))

    # 현재 단계에서 익은 토마토 반환

    return tmp


time = 0
past = 0
visited = [[[False]*m for _ in range(n)] for _ in range(h)]

while True:
    # 안익은 토마토 갯수가 0개, 즉 모든 토마토가 전부 익었다면 탈출
    if remain == 0:
        print(time)
        break
    #
    past = remain
    ripe = bfs(ripe)
    print(ripe)
    remain -= len(ripe)

    # print(remain)

   # 토마토가 모두 익지 못하는 상황이라면?
    if past == remain:
        print(-1)
        break

    time += 1

# ! tomato 배열에 누적으로 +1 씩해서 최종적으로 나온 최댓값이 걸린 시간임을 이용할 것. 토마토가 언제 익었는지를 기록할수 있다.
# ! 그렇게하면, 나처럼 시간초별로 bfs를 돌릴필요 없이 한번만 bfs를 돌리면 된다.
