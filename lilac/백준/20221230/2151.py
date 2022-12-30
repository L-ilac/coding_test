# 한쪽 문에서 다른 쪽 문을 볼 수 있게하는 거울 설치의 최솟값.
import sys
import heapq
from collections import deque
# 방의 크기
n = int(input())
room = []
doors = []
mirrors = []
queue = deque()
visit = {}

d = [(0, -1), (-1, 0), (0, 1), (1, 0)]  # 상좌하우(0,1,2,3) -> 빛의 이동 방향
# 빛이 상 or 하 방향으로 이동 중 거울을 만나면 좌 or 우로만 갈 수 있고, 반대도 그렇다.

for _ in range(n):
    room.append(list(sys.stdin.readline().rstrip()))

# 문 위치, 거울 설치 가능한 곳 찾기(필요 없을지도?)
for y in range(n):
    for x in range(n):
        if room[y][x] == '#':
            doors.append((x, y))
        elif room[y][x] == '!':
            mirrors.append((x, y))

# # 문으로부터 갈 수 있는 방향 찾기
min_mirror = sys.maxsize
start_x, start_y = doors[0]
end_x, end_y = doors[1]
for i in range(4):
    # 순서대로 새로운 x, 새로운 y, 현재 이동 방향, 거울을 마주쳐서 꺾은 횟수, 지나온 경로
    # heapq.heappush(queue, (0, start_x, start_y, i))
    queue.append((0, start_x, start_y, i))
    visit[(start_x, start_y, i)] = 0


while queue:
    # mirror_visit, now_x, now_y, now_direction = heapq.heappop(queue)
    mirror_visit, now_x, now_y, now_direction = queue.popleft()

    new_x, new_y = now_x + d[now_direction][0], now_y + d[now_direction][1]

    if -1 < new_x < n and -1 < new_y < n:

        if visit.get((new_x, new_y, now_direction)) is None or visit[(new_x, new_y, now_direction)] > mirror_visit:
            visit[(new_x, new_y, now_direction)] = mirror_visit

            if new_x == end_x and new_y == end_y:  # 다른 문에 도달 했을 경우
                min_mirror = min(min_mirror, mirror_visit)

                # 이동 방향에 있는 곳이 벽이라면 더 못감
            if room[new_y][new_x] == '*':
                continue
            # 이동 방향이 빈칸이라면, 이동방향을 유지한채로 갈 수 있음
            elif room[new_y][new_x] == '.':
                queue.append((mirror_visit, new_x, new_y, now_direction))
            # 이동 방향이 거울을 설치 할 수 있는 위치라면, 선택해야함
            else:
                # 거울을 설치 안했다고 가정할 경우(그냥 직진)
                queue.append((mirror_visit, new_x, new_y, now_direction))
                # 거울을 설치했다고 가정할 경우
                queue.append((mirror_visit+1, new_x,
                              new_y, (now_direction+1) % 4))
                queue.append((mirror_visit+1, new_x,
                              new_y, (now_direction+3) % 4))

        # 현재 빛이 이동하는 방향을 지속적으로 저장해야함

        # 1. 문 두개 중 하나에서 출발.
        # 2. 빛이 이동하는 방향으로 계속 움직이되, !(거울) 만나기 전까지 계속 직진
        # 3-1. '.' 을 만날 경우 이동방향은 변하지 않음.
        # 3. !을 만날 경우 이동방향 기준 왼쪽/오른쪽 90도 방향으로 밖에 못움직임.(bfs 형태로 추가 + 방향 변경)
        # 4.

print(min_mirror)

# * solution2 -> 또다른 방법
N = int(input())

listMap = []
listPos = []
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for _ in range(N):
    listMap.append(list(map(lambda x: x, input())))

for i in range(N):
    for j in range(N):
        if listMap[i][j] == '#':
            listPos.append((i, j))

startPosX, startPosY, endPosX, endPosY = listPos[0][0], listPos[0][1], listPos[1][0], listPos[1][1]
q = deque()
q.append((listPos[0], 0, 2))
q.append((listPos[0], 0, 3))
q.append((listPos[0], 0, 1))
q.append((listPos[0], 0, 0))

while q:
    (posX, posY), mirrorCount, direction = q.popleft()

    movePosX = posX+dx[direction]
    movePosY = posY+dy[direction]

    while 0 <= movePosX < N and 0 <= movePosY < N and listMap[movePosX][movePosY] != '*':
        if listMap[movePosX][movePosY] == "!":
            if direction == 0 or direction == 2:
                q.append(((movePosX, movePosY), mirrorCount+1, 1))
                q.append(((movePosX, movePosY), mirrorCount+1, 3))
            else:
                q.append(((movePosX, movePosY), mirrorCount+1, 0))
                q.append(((movePosX, movePosY), mirrorCount+1, 2))

        if movePosX == endPosX and movePosY == endPosY:
            q.clear()
            break

        movePosX += dx[direction]
        movePosY += dy[direction]

print(mirrorCount)
