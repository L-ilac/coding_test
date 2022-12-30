# 볼 수 있는 방향이 전부 다른 cctv가 주어졌을 때, cctv에 의해서 감시되지 않는 사각지대를 구하는 문제
# product를 적절히 사용해서 풀어야 풀 수 있었다.
import sys
import copy
from itertools import product
n, m = map(int, input().split())

# 맵 세팅
zone = []
for _ in range(n):
    zone.append(list(map(int, sys.stdin.readline().split())))

# 1번 cctv : 4종류 (1,0) (1,1) (1,2) (1,3) 상, 하, 좌, 우
# 2번 cctv : 2종류 (2,0) (2,1) 상하, 좌우
# 3번 cctv : 4종류 (3,0) (3,1) (3,2) (3,3) 상우, 상좌, 하우, 하좌
# 4번 cctv : 4종류 (4,0) (4,1) (4,2) (4,3) 상, 하, 좌, 우(튀어나온 부분 기준)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
# 5번 cctv : 1종류 (5,0)

=======
# 5번 cctv : 1종류
>>>>>>> b99453e (파일 재추가)
=======
# 5번 cctv : 1종류 (5,0)

>>>>>>> 8c3377f (123)
=======
# 5번 cctv : 1종류
>>>>>>> b99453e (파일 재추가)
d = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # 상하좌우

move = {
    (1, 0): [d[0]], (1, 1): [d[1]], (1, 2): [d[2]], (1, 3): [d[3]],
    (2, 0): [d[0], d[1]], (2, 1): [d[2], d[3]],
    (3, 0): [d[0], d[2]], (3, 1): [d[0], d[3]], (3, 2): [d[1], d[2]], (3, 3): [d[1], d[3]],
    (4, 0): [d[0], d[1], d[2]], (4, 1): [d[0], d[1], d[3]], (4, 2): [d[0], d[2], d[3]], (4, 3): [d[1], d[2], d[3]],
    (5, 0): [d[0], d[1], d[2], d[3]]
}

cctv = []

cctv_cnt = 0
for y in range(n):
    for x in range(m):  # x좌표, y좌표, cctv 타입
        if zone[y][x] == 1:
            tmp = []
            for i in range(4):
                tmp.append((x, y, (zone[y][x], i)))
            cctv.append(tmp)
        if zone[y][x] == 2:
            tmp = []
            for i in range(2):
                tmp.append((x, y, (zone[y][x], i)))
            cctv.append(tmp)
        if zone[y][x] == 3:
            tmp = []
            for i in range(4):
                tmp.append((x, y, (zone[y][x], i)))
            cctv.append(tmp)
        if zone[y][x] == 4:
            tmp = []
            for i in range(4):
                tmp.append((x, y, (zone[y][x], i)))
            cctv.append(tmp)
        if zone[y][x] == 5:
            tmp = []
            for i in range(1):
                tmp.append((x, y, (zone[y][x], i)))
            cctv.append(tmp)

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD

=======
>>>>>>> b99453e (파일 재추가)
=======

>>>>>>> 8c3377f (123)
=======
>>>>>>> b99453e (파일 재추가)
# ! product 의 중요성. -> 다른 사람의 코드 참고 안했으면 못풀었음.
# ! product를 쓰는 이유는 한 cctv가 볼 수 있는 방향이 여러개라서, 방향별로 모든 조합을 다 구해야하기 떄문이다.
# ! cctv 자체는 cctv의 좌표로 구분하면 되지만, 좌표는 같은데 방향이 다른 cctv들은 한 그룹에 묶어놔야했기 때문에, 한 그룹에서 하나씩 뽑아서 합치는 형식으로 구성해야한다.
# ! 모든 cctv를 하나의 리스트에 다 넣고 조합을 구하려하면, 동일한 cctv의 다른 방향끼리 묶일 수 있다. -> 실제로 겪었던 문제
total_cctv_combinations = list(product(*cctv))


def apply_cctv(zone, n, m, cctv):
    for cam_x, cam_y, cam_type in cctv:  # cam -> x좌표, y좌표, cctv 타입

        for dx, dy in move[cam_type]:
            # bfs적 접근이 아니라 그냥 한 방향으로 끝까지 쭉가야됌
            new_x, new_y = cam_x+dx, cam_y+dy
            while True:
                if -1 < new_x < m and -1 < new_y < n:
                    if zone[new_y][new_x] == 6:
                        break
                    elif zone[new_y][new_x] == 0:
                        zone[new_y][new_x] = "#"
                else:
                    break

                new_x += dx
                new_y += dy

    return zone


def get_blind_spot(zone, n, m):  # 안전지대를 크기 구하는 함수
    cnt = 0
    for y in range(n):
        for x in range(m):
            if zone[y][x] == 0:
                cnt += 1

    return cnt


min_blind_spot = sys.maxsize
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
# ! cctv가 하나도 없는 경우에는 그냥 사각지대 갯수를 세야되니까

=======
>>>>>>> b99453e (파일 재추가)
=======
# ! cctv가 하나도 없는 경우에는 그냥 사각지대 갯수를 세야되니까

>>>>>>> 8c3377f (123)
=======
>>>>>>> b99453e (파일 재추가)
blind_spot = 0

for cctv_comb in total_cctv_combinations:
    tmp_zone = copy.deepcopy(zone)
    applied_zone = apply_cctv(tmp_zone, n, m, cctv_comb)
    blind_spot = get_blind_spot(applied_zone, n, m)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD

    min_blind_spot = min(min_blind_spot, blind_spot)

    del tmp_zone


=======
=======

>>>>>>> 8c3377f (123)
    min_blind_spot = min(min_blind_spot, blind_spot)

    del tmp_zone

<<<<<<< HEAD
>>>>>>> b99453e (파일 재추가)
=======

>>>>>>> 8c3377f (123)
=======
    min_blind_spot = min(min_blind_spot, blind_spot)
    del tmp_zone

>>>>>>> b99453e (파일 재추가)
print(min_blind_spot)
