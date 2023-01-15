# 주어진 정육면체 전개도가 올바른지 판단
# 정사각형이 떨어져 있는 경우는 없다.
# ! 주어진 그래프에서 정육면체의 전개도로 주어진 형태를 좌표 or 배열 형태로 저장한다.
# ! 구한 전개도의 형태가 실제 정육면체의 [기본 전개도(11종류) * 상하좌우반전 * 회전 4방향]에 속하는지 검사한다.

from collections import deque, defaultdict


def bfs(board):
    n, m = len(board), len(board[0])
    points = []

    d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited = [[False]*m for _ in range(n)]
    q = deque()

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and board[i][j] == 1:
                q.append((i, j))
                visited[i][j] = True

                while q:
                    nowx, nowy = q.popleft()
                    points.append((nowx, nowy))

                    for dx, dy in d:
                        newx, newy = nowx+dx, nowy+dy

                        if 0 <= newx <= n-1 and 0 <= newy <= m-1:
                            if not visited[newx][newy] and board[newx][newy] == 1:
                                visited[newx][newy] = True
                                q.append((newx, newy))

    return points


board = []

for _ in range(3):
    tmp = []
    for _ in range(6):
        data = list(map(int, input().split()))
        tmp.append(data)

    board.append(tmp)

basic = [{(0, 2), (1, 0), (1, 1), (1, 2), (1, 3), (2, 2)},
         {(0, 1), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0)},
         {(0, 2), (1, 0), (1, 1), (1, 2), (1, 3), (2, 1)},
         {(0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0)},
         {(0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 1)},
         {(0, 0), (0, 1), (0, 2), (1, 2), (1, 3), (1, 4)},
         {(0, 0), (0, 1), (1, 1), (1, 2), (1, 3), (2, 2)},
         {(0, 0), (0, 1), (1, 1), (1, 2), (1, 3), (2, 3)},
         {(0, 2), (1, 0), (1, 1), (1, 2), (2, 2), (2, 3)},
         {(0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 3)},
         {(0, 0), (0, 1), (1, 1), (1, 2), (2, 2), (2, 3)}]


def rotate(basic):
    result = []
    for case in basic:
        max_x = max(x for x, y in list(case))
        tmp = set()
        for x, y in list(case):
            tmp.add((y, max_x - x))

        result.append(tmp)

    return result


def mirror(basic):
    result = []
    for case in basic:
        max_x = max(x for x, y in list(case))
        max_y = max(y for x, y in list(case))

        tmp = set()
        for x, y in list(case):
            tmp.add((max_x-x, y))
        result.append(tmp)

        tmp = set()
        for x, y in list(case):
            tmp.add((x, max_y-y))
        result.append(tmp)

    return result


for b in board:
    points = bfs(b)
    min_x = min([x for x, y in points])
    min_y = min([y for x, y in points])

    new_points = set([(x-min_x, y-min_y) for x, y, in points])

    if new_points in basic:
        print("yes")
    elif new_points in rotate(basic):
        print("yes")
    elif new_points in rotate(rotate(basic)):
        print("yes")
    elif new_points in rotate(rotate(rotate(basic))):
        print("yes")
    elif new_points in mirror(basic):
        print("yes")
    elif new_points in rotate(mirror(basic)):
        print("yes")
    elif new_points in rotate(rotate(mirror(basic))):
        print("yes")
    elif new_points in rotate(rotate(rotate(mirror(basic)))):
        print("yes")
    else:
        print("no")
