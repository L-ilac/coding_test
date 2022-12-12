# 연구소
from itertools import combinations
from collections import deque
from copy import deepcopy

WALL_CNT = 3
N, M = map(int, input().split())
zido = []

for _ in range(N):
    zido.append(list(map(int, input().split())))

def get_virus_location():
    virus_lst = []
    for i in range(N):
        for j in range(M):
            if zido[i][j] == 2:
                virus_lst.append((i, j))
    return virus_lst

virus_lst = get_virus_location()
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(zido):

    queue = deque()
    for v in virus_lst:
        queue.append(v)
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if 0 <= tx < N and 0 <= ty < M and zido[tx][ty] == 0:
                zido[tx][ty] = 2
                queue.append((tx, ty))

    res = 0
    for z in zido:
        res += z.count(0)

    return res

walls = list(combinations([x for x in range(N * M)], WALL_CNT))

res = 0
for wall in walls:

    put_wall = True
    tmp_zido = deepcopy(zido)

    for w in wall:
        x = w // M
        y = w % M
        if zido[x][y] != 0:
            put_wall = False
        else:
            tmp_zido[x][y] = 1
        
    if not put_wall:
        continue
    
    res = max(res, bfs(tmp_zido))

print(res)
