# 아기 상어

from collections import deque

N = int(input())
zido = []

x, y = 0, 0
for i in range(N):
    lst = list(map(int, input().split()))
    if 9 in lst:
        x, y = i, lst.index(9)
        lst[y] = 0
    zido.append(lst)

current_size = 2 # 아기상어의 현재 크기
eatting_cnt = 0 # 먹은 물고기 수

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 아기상어가 먹을 수 있는 먹이 반환
def get_food(sx, sy):
    foods = []
    queue = deque([(sx, sy, 0)]) # 마지막은 물고기 거리
    visited = [[0] * N for _ in range(N)]
    visited[sx][sy] = 1

    while queue:
        x, y, d = queue.popleft()
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if 0 <= tx < N and 0 <= ty < N and zido[tx][ty] <= current_size and visited[tx][ty] == 0:
                visited[tx][ty] = 1
                queue.append((tx, ty, d+1))
                if 0 < zido[tx][ty] < current_size:
                    foods.append((tx, ty, d+1))
    return foods

# 먹이가 여러개 있을 때 우선순위 결정
def get_priority(foods):

    # 1. 가까운 순서 
    # 2. 가장 위
    # 3. 가장 왼쪽
    lst = sorted(foods, key=lambda x : (x[2], x[0], x[1]))
    
    return lst[0]

res = 0
while True:
    foods = get_food(x, y)
    
    # 음식 없으면 엄마 상어한태 감
    if not foods:
        break
    
    food = get_priority(foods)
    x, y, d = food
    zido[x][y] = 0
    
    # 먹은 횟수 1 증가 , 사이즈 증가 
    eatting_cnt += 1
    if eatting_cnt == current_size:
        current_size += 1
        eatting_cnt = 0
    
    res += d


print(res)