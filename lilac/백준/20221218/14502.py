# 문제 접근법
# 1. 주어진 지도에서 벽을 설치할 수 있는 구역을 모두 찾아낸다 + 그 중 3개로 이루어진 조합(combinations)들을 모두 구한다.
# 2. 1번에서 구한 모든 조합에 대해 지도에 벽을 설치하고, 바이러스를 퍼뜨린후 안전구역 영역의 크기를 구한다.
# 문제 조건으로 맵 크기가 최소 3*3 ~ 최대 8*8 이라서 브루트포스가 가능한듯

import sys
import copy
from collections import deque
from itertools import combinations


def get_safezone(graph, virus):
    # 1. 바이러스 위치 찾기
    # 2. 바이러스 위치 기준으로 bfs, 도달할 수 있는 모든 위치에 대해 2로 바꿔주기
    # 3. 0 갯수 세기
    direction = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    visited = [[False] * m for _ in range(n)]
    queue = deque()
    result = 0

    # 바이러스의 초기 위치를 찾는 부분은 사실 밖으로 빼서, 밖에서 1번구하고 그냥 함수 인자로 넘겨주면 시간을 더 줄일 수 있을 듯
    # 왜냐하면, 모든 조합에 대해서 get_safezone() 을 돌리면 m*n 영역 탐색을 반복적으로(벽을 세우는 조합의 갯수만큼) 해줘야함
    # for x in range(m):
    #     for y in range(n):
    #         if graph[y][x] == 2:
    #             queue.append((x, y))

    queue.extend(virus)

    # bfs로 바이러스가 도달할 수 있는 공간에 다 퍼뜨리기
    while queue:
        now_x, now_y = queue.popleft()

        for dx, dy in direction:
            new_x, new_y = now_x + dx, now_y + dy

            if -1 < new_x < m and -1 < new_y < n and not visited[new_y][new_x]:
                if graph[new_y][new_x] == 0:
                    graph[new_y][new_x] = 2
                    visited[new_y][new_x] = True
                    queue.append((new_x, new_y))

    for x in range(m):
        for y in range(n):
            if graph[y][x] == 0:
                result += 1

    return result


# 벽을 설치할 수 있는 모든 위치를 얻고, 3개의 조합을 구하는 함수
def build_wall(graph):

    empty = []
    for x in range(m):
        for y in range(n):
            if graph[y][x] == 0:
                empty.append((x, y))

    result = list(combinations(empty, 3))

    return result


n, m = map(int, input().split())
zone = []

# 지도 세팅
for _ in range(n):
    zone.append(list(map(int, sys.stdin.readline().split())))

# 벽을 지을 수 있는 모든 조합
can_build_wall = build_wall(zone)

# 안전 구역 크기
safe_zone_size = 0

# 바이러스가 존재하는 위치 찾기
virus_point = []
for x in range(m):
    for y in range(n):
        if zone[y][x] == 2:
            virus_point.append((x, y))


for points in can_build_wall:
    # 존재하는 모든 조합에 대해서 동일한 초기 지도를 기준으로 벽을 설치해야하기 때문에, zone을 건드리면 초기 지도가 날라가기때문에 복사해서 사용
    tmp_zone = copy.deepcopy(zone)

    # 조합으로 결정된 위치에 벽 세우기
    for x, y in points:
        tmp_zone[y][x] = 1

    # 안전구역 크기 구하기
    tmp = get_safezone(tmp_zone, virus_point)

    # 안전구역의 최댓값 갱신
    safe_zone_size = max(safe_zone_size, tmp)

    # 복사한 지도 메모리 삭제
    del tmp_zone

print(safe_zone_size)
