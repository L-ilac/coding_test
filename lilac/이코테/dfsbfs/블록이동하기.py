from collections import deque


def solution(board):
    n = len(board)
    answer = 0
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우
    robot = ((0, 0), (0, 1))  # 로봇 초기 위치
    q = deque()
    visited = set()

    q.append((robot, 0))  # 초기 로봇 위치 , 지금까지 이동 횟수

    # !이렇게 했을 때 구분이 될줄 알았는데 의도한 역할을 하진 않음
    # !((0,0),(0,1)) 과 ((0,1),(0,0))을 같은 것으로 취급하길 기대했지만, 다르게 취급함
    # !하지만, 탐색 오버헤드가 증가할 뿐, 탐색에는 영향이 없음 (같은지점에 대해서 최대 2번만 탐색하는 것)
    # !모범 답안에서는 로봇의 좌표 2개를 set으로 묶어서 visited를 배열로 만들어서 추가함
    # !즉, {(0,0),(0,1)} 과 {(0,1),(0,0)}은 같은 것으로 취급되기 때문에, visited에 1개씩만 들어갈 수 있게 할 수 있음
    visited.add(robot)

    while q:
        now_robot, step = q.popleft()

        if any(a == (n-1, n-1) for a in now_robot):
            answer = step
            break

        # 일반적인 상하좌우 이동
        for dx, dy in d:
            new_robot = ((now_robot[0][0]+dx, now_robot[0][1]+dy),
                         (now_robot[1][0]+dx, now_robot[1][1]+dy))

            # 예외 조건
            if any(0 > a[0] or a[0] > n-1 or 0 > a[1] or a[1] > n-1 for a in new_robot):
                continue
            if any(board[a[0]][a[1]] == 1 for a in new_robot):
                continue

            if new_robot in visited:
                continue

            visited.add(new_robot)
            q.append((new_robot, step + 1))

        # 회전 이동 (축을 어디로 잡아서 회전하냐)
        # 로봇의 방향 (좌우 or 상하)
        robot_dir = 0  # 좌우 = 0 상하 = 1
        if abs(now_robot[0][0] - now_robot[1][0]) == 1:
            robot_dir = 1

        possible = []

        # 로봇이 상하로 배치되어있을 때
        if robot_dir == 1:
            for i in range(2, 4):
                # 로봇 기준으로 좌우의 공간이 범위를 벗어나지 않는다면
                if all(0 <= rx+d[i][0] <= n-1 and 0 <= ry+d[i][1] <= n-1 for rx, ry in now_robot):

                    # 좌우의 공간은 둘다 0이어야함
                    if all(board[rx+d[i][0]][ry+d[i][1]] == 0 for rx, ry in now_robot):
                        possible.append(
                            (now_robot[0], (now_robot[0][0]+d[i][0], now_robot[0][1]+d[i][1])))
                        possible.append(
                            (now_robot[1], (now_robot[1][0]+d[i][0], now_robot[1][1]+d[i][1])))

            # 로봇이 좌우로 배치되어있을 떄
        else:
            for i in range(2):
                if all(0 <= rx+d[i][0] <= n-1 and 0 <= ry+d[i][1] <= n-1 for rx, ry in now_robot):
                    if all(board[rx+d[i][0]][ry+d[i][1]] == 0 for rx, ry in now_robot):
                        possible.append(
                            (now_robot[0], (now_robot[0][0]+d[i][0], now_robot[0][1]+d[i][1])))
                        possible.append(
                            (now_robot[1], (now_robot[1][0]+d[i][0], now_robot[1][1]+d[i][1])))

        for r in possible:
            # 예외 조건
            if r in visited:
                continue

            visited.add(r)
            q.append((r, step + 1))

    print(visited)
    print(len(visited))
    return answer


print(solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [
    0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]))
