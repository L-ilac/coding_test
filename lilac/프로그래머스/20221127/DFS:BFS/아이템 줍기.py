from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    queue = deque()
    direction = [(0, 1), (0, -1), (-1, 0), (1, 0)]  # 상하좌우
    map = [[0] * 104 for _ in range(104)]

    queue.append((characterX*2, characterY*2, 0))  # starting point

    # map setting
    for r in rectangle:
        for y in range(r[1]*2, (r[3]*2) + 1):
            for x in range(r[0]*2, (r[2]*2) + 1):
                map[y][x] = 1

    for r in rectangle:
        for y in range(r[1]*2 + 1, r[3]*2):
            for x in range(r[0]*2 + 1, r[2]*2):
                map[y][x] = 0

    # map을 2배로 확대했다는 사실을 기억할 것.
    while queue:
        now = queue.popleft()
        map[now[1]][now[0]] = 0
        print(now)

        if (now[0], now[1]) == (itemX*2, itemY*2):
            # 몇걸음 움직였냐 카운트 필요
            answer = int(now[2]/2)
            break

        for dir in direction:
            # 상하좌우 순서로 갈 수 있는지 확인
            if map[now[1]+dir[1]][now[0]+dir[0]] == 1:
                # 갈 수 있는 모든 방향 넣기
                queue.append((now[0]+dir[0], now[1]+dir[1], now[2]+1))

    return answer
