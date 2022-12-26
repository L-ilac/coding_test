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
# 5번 cctv : 1종류
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

# product 의 중요성.
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
blind_spot = 0

for cctv_comb in total_cctv_combinations:
    tmp_zone = copy.deepcopy(zone)
    applied_zone = apply_cctv(tmp_zone, n, m, cctv_comb)
    blind_spot = get_blind_spot(applied_zone, n, m)
    min_blind_spot = min(min_blind_spot, blind_spot)
    del tmp_zone

print(min_blind_spot)
