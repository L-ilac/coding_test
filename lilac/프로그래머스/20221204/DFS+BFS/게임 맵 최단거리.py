from collections import deque


def solution(maps):
    answer = 0
    queue = deque()
    direction = [(0, 1), (0, -1), (-1, 0), (1, 0)]  # 상하좌우
    flag = False
    n = len(maps[0])  # 가로 최대길이(x좌표)
    m = len(maps)  # 세로 최대길이(y좌표)

    start = [0, 0, 1]  # x좌표, y좌표, 현 지점까지의 이동 거리
    queue.append(start)
    maps[start[1]][start[0]] = 0

    while queue:
        now = queue.popleft()

        if now[0] == n-1 and now[1] == m-1:
            answer = now[2]
            flag = True
            break

        for d in direction:
            if -1 < now[0] + d[0] < n and -1 < now[1] + d[1] < m:
                if maps[now[1] + d[1]][now[0] + d[0]] == 1:
                    maps[now[1] + d[1]][now[0] + d[0]] = 0
                    queue.append([now[0] + d[0], now[1] + d[1], now[2]+1])

    if flag:
        return answer
    else:
        return -1
