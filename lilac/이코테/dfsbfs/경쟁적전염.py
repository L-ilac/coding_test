import heapq
from collections import deque
n, k = map(int, input().split())

board = []
virus = []
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for i in range(n):
    data = list(map(int, input().split()))
    board.append(data)

    for j in range(n):
        if data[j] != 0:
            heapq.heappush(virus, (board[i][j], i, j))


target_t, target_x, target_y = map(int, input().split())


t = 0

while t < target_t:
    tmp = []
    while virus:
        vv, vx, vy = heapq.heappop(virus)

        for dx, dy in d:
            new_x, new_y = vx+dx, vy + dy

            if 0 <= new_x <= n-1 and 0 <= new_y <= n-1:
                if board[new_x][new_y] == 0:
                    board[new_x][new_y] = vv
                    heapq.heappush(tmp, (board[new_x][new_y], new_x, new_y))

    t += 1

    # ! 바이러스들이 퍼지는 순서를 섞이게 하지 않기 위함
    # ! 1초에 퍼지는 바이러스 1 > 1초에 퍼지는 바이러스 2 > 2초에 퍼지는 바이러스 1
    # ! 시간이 가장 높은 우선순위를 가지고, 시간이 같다면 그 다음이 바이러스 값이 낮은 순서대로임.
    virus = tmp

print(board[target_x-1][target_y-1])


# ! bfs인데 사실 위의 풀이와 별반 다를바 없음. heapq 대신 deque쓴거 밖에 차이가 없음

# import heapq
n, k = map(int, input().split())

board = []
virus = []
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for i in range(n):
    data = list(map(int, input().split()))
    board.append(data)

    for j in range(n):
        if data[j] != 0:
            virus.append((board[i][j], i, j))


target_t, target_x, target_y = map(int, input().split())


q = deque()
virus.sort(key=lambda x: x[0])
q.extend(virus)

t = 0
while t < target_t:
    tmp = []
    while q:
        vv, vx, vy = q.popleft()

        for dx, dy in d:
            new_x, new_y = vx + dx, vy + dy

            if 0 <= new_x <= n-1 and 0 <= new_y <= n-1:

                if board[new_x][new_y] == 0:
                    board[new_x][new_y] = vv
                    tmp.append((board[new_x][new_y], new_x, new_y))

    t += 1

    tmp.sort(key=lambda x: x[0])
    # ! 바이러스 튜플의 2번째 인자로 바이러스가 퍼지는 시간값을 넣으면, 매번 정렬할 필요 없이 시간을 기준으로 루프 탈출 가능 + 굳이 시간체크 while 을 쓸 필요가 없음

    q.extend(tmp)

print(board[target_x-1][target_y-1])
