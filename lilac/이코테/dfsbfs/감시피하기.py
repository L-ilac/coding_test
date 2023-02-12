import copy
from itertools import combinations

n = int(input())

board = []

teachers = []
vacant = []


for i in range(n):
    data = list(input().split())
    board.append(data)
    for j in range(n):
        # 선생님 위치
        if data[j] == 'T':
            teachers.append((i, j))
        # 장애물 설치할 수 있는 위치
        elif data[j] == 'X':
            vacant.append((i, j))


def search(tmp):
    for tx, ty in teachers:

        for dx, dy in d:
            new_x, new_y = tx+dx, ty+dy

            while True:
                # 지도밖으로 벗아나면 탈출
                if 0 > new_x or new_x > n-1 or 0 > new_y or new_y > n-1:
                    break

                # 장애물을 만난경우, 더이상 갈 수 없음
                if tmp[new_x][new_y] == 'O':
                    break

                # 학생을 만난경우, 해당 장애물을 설치 실패임
                if tmp[new_x][new_y] == 'S':
                    return False

                new_x += dx
                new_y += dy

    return True


walls_comb = list(combinations(vacant, 3))
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
flag = False

for walls in walls_comb:
    # 1. 실제 지도에 장애물 설치
    # 2. 선생님 위치 기준으로 감시할 수 있는 포인트 전부 탐색
    # ! 감시할때는 막히기전까지 갈 수 있을 때까지 가야하는게 포인트
    # 3. 선생님 감시위치 찾는 중에 s인 위치 있으면 no, 없으면 yes
    tmp = copy.deepcopy(board)
    cnt = 0
    # 장애물 설치
    for wx, wy in walls:
        tmp[wx][wy] = 'O'

    if search(tmp):
        print("YES")
        flag = True
        break
    else:
        continue

if flag:
    pass
else:
    print("NO")
