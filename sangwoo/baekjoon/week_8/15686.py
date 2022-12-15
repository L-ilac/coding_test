# 치킨 배달

from itertools import combinations

N, M = map(int, input().split())
zido = []

for _ in range(N):
    zido.append(list(map(int, input().split())))


# 치킨 집, 가정 집 위치 확인
def check_location():
    chicken_lst = []
    house_lst = []

    for x in range(N):
        for y in range(N):
            if zido[x][y] == 2:
                chicken_lst.append((x, y))
            elif zido[x][y] == 1:
                house_lst.append((x, y))
    
    return chicken_lst, house_lst

def check_distance(chicken_lst, house_lst):
    res = 0
    for house in house_lst:
        tmp = float('inf')
        
        for chicken in chicken_lst:
            tmp = min(tmp, abs(house[0]-chicken[0]) + abs(house[1]-chicken[1]))
        res += tmp

    return res

chicken_lst, house_lst = check_location()
res = float('inf')
for c in list(combinations(chicken_lst, M)):
    res = min(res, check_distance(c, house_lst))

print(res)