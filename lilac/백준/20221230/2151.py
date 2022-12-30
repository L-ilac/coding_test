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

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 8785cd6 (20221230 스터디 문제 추가 주석)
    # 거울을 어떻게 설치해도 한쪽 문에서 다른 쪽 문을 볼 수 없는 경우는 주어지지 않는다. 그렇다는건, 출발지점에서 도착지점으로의 경로는 무조건 존재한다는 것.
    # 문제의 요구는 거울설치의 최솟값이므로, 큐에 탐색경로가 거울 설치가 적은 순으로 들어가게 만들 수 있다면, 가장 먼저 도착하는 경로가 거울을 최소로 설치한 경로이다.

    # 새로 방문하는 지점은 빈공간이거나, 거울을 설치할수 있는 자리이거나, 벽이거나, 지도를 벗어나야한다.
    # 벽이거나 지도를 벗어나는 경우, 해당 경로에 대한 탐색을 종료하면 된다.
    # 빈 공간이거나 거울을 설치할 수 있는 자리인데 설치를 안할 경우, 방향을 유지한채로 직진하면 된다.
    # 거울을 설치할 수 있는 자리인데 설치를 할 경우, 방향을 바꿔야하며, 거울 설치 횟수를 증가시킨채로 경로 탐색을 이어가야한다.

    # 위의 4가지 경우에서, 거울 설치 횟수가 늘어나는 경우는 (거울을 설치할 자리에 도착 + 그 자리에 거울을 설치) 밖에 없다.
    # 그러므로, 큐에서 뽑아낸 출발지점에서 거울을 만날때까지 방향을 유지한채로 직진하다가 거울을 만나서 설치하는 경우에만 큐에 새로운 출발지점을 삽입해주면 된다.

    while 0 <= movePosX < N and 0 <= movePosY < N and listMap[movePosX][movePosY] != '*':

        # 거울을 지나침 + 해당 자리에 거울 설치일 때만, 큐에다가 탐색경로를 넣는다면, 큐의 들어가있는 탐색경로가 거울 방문이 적은 순서임을 보장할 수 있다.
        # 그 전까지는 방향을 유지한채로 계속 직진하며, 직진하다보면 벽을 만나거나 범위를 벗어나는 경로는 자연스럽게 걸러진다.
        # 거울을 설치할 수 있지만, 설치하지 않는 경우는 그냥 직진이랑 똑같이 취급할 수 있다.

        # 큐에 있는 거울을 n번 지나친 경로는 거울을 n+1 지나친 경로만 넣을 수 있다.
<<<<<<< HEAD
=======
    while 0 <= movePosX < N and 0 <= movePosY < N and listMap[movePosX][movePosY] != '*':
>>>>>>> b99453e (파일 재추가)
=======
>>>>>>> 8785cd6 (20221230 스터디 문제 추가 주석)
=======
    while 0 <= movePosX < N and 0 <= movePosY < N and listMap[movePosX][movePosY] != '*':
>>>>>>> b99453e (파일 재추가)
        if listMap[movePosX][movePosY] == "!":
            if direction == 0 or direction == 2:
                q.append(((movePosX, movePosY), mirrorCount+1, 1))
                q.append(((movePosX, movePosY), mirrorCount+1, 3))
            else:
                q.append(((movePosX, movePosY), mirrorCount+1, 0))
                q.append(((movePosX, movePosY), mirrorCount+1, 2))

        if movePosX == endPosX and movePosY == endPosY:
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
            q.clear()  # 도착지점에 도착했으므로, 나머지 경우는 더 찾아볼 필요가 없다.
            break

        # 한 출발점을 기준으로 주어진 방향으로 갈 수 있을 때까지 계속 직진한다.
        # 거울을 만나면 꺾는 방향으로의 새로운 경로를 큐에 삽입할 것이고,
        # 거울을 만나도 설치하지 않는 경우 or 빈공간인 경우에는 방향을 유지하여 계속 직진처리하면 된다.
=======
            q.clear()
            break

>>>>>>> b99453e (파일 재추가)
=======
            q.clear()  # 도착지점에 도착했으므로, 나머지 경우는 더 찾아볼 필요가 없다.
            break

        # 한 출발점을 기준으로 주어진 방향으로 갈 수 있을 때까지 계속 직진한다.
        # 거울을 만나면 꺾는 방향으로의 새로운 경로를 큐에 삽입할 것이고,
        # 거울을 만나도 설치하지 않는 경우 or 빈공간인 경우에는 방향을 유지하여 계속 직진처리하면 된다.
>>>>>>> 8785cd6 (20221230 스터디 문제 추가 주석)
=======
            q.clear()
            break

>>>>>>> b99453e (파일 재추가)
        movePosX += dx[direction]
        movePosY += dy[direction]

print(mirrorCount)
