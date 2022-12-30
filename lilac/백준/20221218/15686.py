# 문제 접근법
# 1. 치킨집 위치를 모두 구한다.  + 집의 위치를 모두 구한다.
# 2. 폐업 시키지 않을 치킨집의 좌표를 구한다.(combinations을 이용해서 모든 조합을 구한다.)
# 3. 폐업 시키지 않을 모든 치킨집에 대해서 각 집의 치킨거리를 구하고 최솟값을 구한다.

from itertools import combinations

n, m = map(int, input().split())

# 맵 세팅
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

all_chicken = []  # 치킨 집 위치
house = []  # 집 위치
for y in range(n):
    for x in range(n):
        if graph[y][x] == 2:
            all_chicken.append((x, y))
        if graph[y][x] == 1:
            house.append((x, y))

saved_chicken = list(combinations(all_chicken, m))  # 폐업하지않을 치킨집 조합

# 최솟값을 구하기 위한 inf 설정
city_chicken_distance = 1e9


def get_distance(s_c):
    chicken_distance = [1e9] * len(house)
    for c_x, c_y in s_c:  # 치킨집 조합 1개에 대해서
        for idx, h in enumerate(house):  # 특정 집의 최소거리를 구해야하므로, idx를 이용한다.
            chicken_distance[idx] = min(
                chicken_distance[idx], abs(c_x-h[0])+abs(c_y-h[1]))

    return sum(chicken_distance)


# 구한 모든 치킨집 조합에 대해서 최소 도시 치킨 거리 계산
for s_c in saved_chicken:
    city_chicken_distance = min(city_chicken_distance, get_distance(s_c))

print(city_chicken_distance)
