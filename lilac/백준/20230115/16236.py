
# ! 한번 풀어봤던 문제라 훨씬 빠르게 풀 수 있었음
#  ! 이전에 풀 때 고집했던, 현 위치에서 가장 가까운 물고기만을 고르는게 아닌, 모든 물고기를 골라서 정렬하는 방식을 사용함.
from collections import deque
n = int(input())

board = []
shark_x, shark_y = 0, 0
shark_size = 2  # 아기상어 초기 사이즈
eaten = 0

for i in range(n):
    data = list(map(int, input().split()))
    board.append(data)

    for j in range(n):
        if data[j] == 9:
            shark_x, shark_y = i, j


# 아기상어는 자신의 크기보다 큰 물고기가 있는 칸은 못지나간다.(나머지는 전부 지나감)
# 아기상어는 자신의 크기보다 작은 물고기만 먹을수 있다


def select_fish(x, y):
    q = deque()
    visited = [[False]*n for _ in range(n)]
    d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited[x][y] = True
    q.append((x, y, 0))

    fishes = []

    while q:
        nowx, nowy, step = q.popleft()

        for dx, dy in d:
            newx, newy = nowx+dx, nowy+dy

            if 0 <= newx <= n-1 and 0 <= newy <= n-1:
                # 상어 크기 이하의 칸은 모두 지나갈 수 있음
                if not visited[newx][newy] and board[newx][newy] <= shark_size:
                    visited[newx][newy] = True
                    q.append((newx, newy, step+1))

                    # 상어 크기보다 작고 빈칸이 아닌 물고기는 먹을 수 있음.
                    if 0 < board[newx][newy] < shark_size:
                        fishes.append((newx, newy, step+1))

    fishes.sort(key=lambda x: (x[2], x[0], x[1]))

    return fishes


# 아기상어가 먹은 물고기 수
time = 0
board[shark_x][shark_y] = 0

while True:
    fish = select_fish(shark_x, shark_y)

    # 먹을 수 있는 물고기가 있으면
    if fish:
        now = fish[0]
        board[now[0]][now[1]] = 0

        shark_x, shark_y = now[0], now[1]

        eaten += 1

        if eaten == shark_size:
            shark_size += 1
            eaten = 0

        time += now[2]
    # 먹을 수 있는 물고기가 없으면, 엄마 상어에게 도움요청
    else:
        break

print(time)
