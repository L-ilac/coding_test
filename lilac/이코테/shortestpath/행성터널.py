import heapq
import sys

10000000000

q = []

n = int(input())
planets = []
# ! 임의의 행성 2개 사이의 이동가능한 경로가 총 3개씩 존재한다고 생각하자.
# ! 여기서 만약에 정렬을 이용하면, 좌표값을 기준으로 앞/뒤만 생각하면 된다.

# 최대 10만개의 행성 * 2 -> 20만개의 경로 * 3 = 60만개
# 128mb -> 32000000

for i in range(0, n):
    x, y, z = map(int, sys.stdin.readline().rstrip().split())
    planets.append((x, y, z, i))  # ! x,y,z, 행성번호


def addPath(pos):
    for i in range(len(planets)):
        # ! 행성사이의 거리, 출발행성, 도착행성
        if i > 0:
            q.append((abs(planets[i][pos]-planets[i-1][pos]),
                     planets[i][3], planets[i-1][3]))
        if i < len(planets)-1:
            q.append((abs(planets[i][pos]-planets[i+1][pos]),
                     planets[i][3], planets[i+1][3]))


planets.sort(key=lambda x: x[0])  # x좌표 순서로 정렬
addPath(0)
planets.sort(key=lambda x: x[1])  # y좌표 순서로 정렬
addPath(1)
planets.sort(key=lambda x: x[2])  # z좌표 순서로 정렬
addPath(2)


total_cost = 0
parent = [i for i in range(n)]


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


q.sort(reverse=True)


# ! len(set(parent)) != 1 으로 모든 부모가 똑같은지 검사하면 시간초과 -> list를 set으로 바꾸는 과정이 O(n) 만큼 소요되기 때문
while q:
    cost, start, end = q.pop()

    # ! 사이클이 발생하지 않으면 해당 간선을 추가
    if find_parent(parent, start) != find_parent(parent, end):
        total_cost += cost
        union_parent(parent, start, end)


print(total_cost)
