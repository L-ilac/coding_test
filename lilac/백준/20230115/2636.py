from collections import deque
n, m = map(int, input().split())


cheese = []
for _ in range(n):
    data = list(map(int, input().split()))
    cheese.append(data)


def count_cheese():
    n, m = len(cheese), len(cheese[0])

    cnt = 0
    for i in range(n):
        for j in range(m):
            if cheese[i][j] == 1:
                cnt += 1

    return cnt


def bfs():
    q = deque()
    q.append((0, 0))
    visited[0][0] = True
    d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while q:
        x, y, = q.popleft()

        for dx, dy in d:
            newx, newy = x+dx, y+dy

            if 0 <= newx <= n-1 and 0 <= newy <= m-1 and not visited[newx][newy]:
                if cheese[newx][newy] == 0:
                    visited[newx][newy] = True
                    q.append((newx, newy))
                elif cheese[newx][newy] == 1:
                    visited[newx][newy] = True
                    cheese[newx][newy] = 0


def melt():
    n, m = len(cheese), len(cheese[0])
    d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    # 내부 구멍은 외부 격자와 이어지지 않음 -> 내부 구멍을 찾아야함
    visited = [[False]*m for _ in range(n)]
    holes = []

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and cheese[i][j] == 0:
                hole = []
                q = deque()
                q.append((i, j))
                visited[i][j] = True

                while q:
                    nowx, nowy = q.popleft()
                    hole.append((nowx, nowy))

                    for dx, dy in d:
                        newx, newy = nowx+dx, nowy+dy
                        if 0 <= newx <= n-1 and 0 <= newy <= m-1:
                            if not visited[newx][newy] and cheese[newx][newy] == 0:
                                visited[newx][newy] = True
                                q.append((newx, newy))

                holes.append(hole)

    for hole in holes[:]:
        if all(1 <= x <= n-2 and 1 <= y <= m-2 for x, y in hole):
            continue
        holes.remove(hole)

    # holes -> 치즈 내부에 있는 구멍
    # 내부 구멍을 전부 1로 채움
    for hole in holes:
        for x, y in hole:
            cheese[x][y] = 1

    # 겉 테두리에 있는 치즈들은 녹는다.
    melted = []
    for i in range(1, n-1):
        for j in range(1, m-1):
            if all(cheese[i+dx][j+dy] == 1 for dx, dy in d):
                continue
            melted.append((i, j))

    for x, y in melted:
        cheese[x][y] = 0

    # 임시로 채워놨던 내부 구멍을 다시 뚫는다.
    for hole in holes:
        for x, y in hole:
            cheese[x][y] = 0


time = 0
remain = []
while True:
    visited = [[False]*m for _ in range(n)]

    # 녹기전 남아있는 치즈 갯수
    remain.append(count_cheese())
    # 치즈가 녹음
    melt()
    # bfs()
    # 1시간 증가
    time += 1
    # 치즈가 없다면 반복문 탈출
    if count_cheese() == 0:
        break


print(time)
print(remain[-1])

# ! 외부공기는 전부 이어져있으므로, 외부 공기를 따라서 bfs를 돌리고, bfs를 돌리다가 외부공기와 만나는 치즈는 가장 겉면 치즈일 것이다.
# ! 따라서 외부공기를 따라 bfs하다가 만나는 치즈들은 녹아서 없어질 것이다.
