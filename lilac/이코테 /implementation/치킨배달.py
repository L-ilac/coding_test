from itertools import combinations

# 주어진 치킨집들에 대해서 집에서 가장 가까운 치킨 거리를 찾는 함수


def chicken_distance(store, house):
    smallest = []
    for h in house:
        tmp = 1e9
        for s in store:
            dist = abs(h[0]-s[0]) + abs(h[1]-s[1])
            tmp = min(dist, tmp)
        smallest.append(tmp)

    # 집 별로 가장 낮은 치킨 값의 모음
    return smallest


n, m = map(int, input().split())

city = []
house = []
store = []
# 지도 설정
for _ in range(n):
    city.append(list(map(int, input().split())))

# 집과 치킨집 찾기
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append((i, j))
        if city[i][j] == 2:
            store.append((i, j))

# 가능한 치킨집조합 구하기
store_comb = list(combinations(store, m))

# 도시 치킨 거리
city_chicken_dist = 1e9

for comb in store_comb:
    city_chicken_dist = min(city_chicken_dist, sum(
        chicken_distance(comb, house)))

print(city_chicken_dist)
