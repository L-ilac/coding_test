from collections import deque
import sys

dx=[0,1,0,-1]
dy=[1,0,-1,0]
n=int(input())

graph=[list(map(str,input())) for _ in range(n)]

# 어떤 방향에서 온게 최소값인지 모르니깐 4방향에 대해서 모든 값을 구해야 함
check = [[[0]*4 for _ in range(n)] for _ in range(n)]
door=[]

# 출발지 도착지 저장
for i in range(n):
    for j in range(n):
        if graph[i][j]=="#":
            door.extend([i,j])

sx,sy,fx,fy=door

# 출발지 설정하고 방향 설정
for k in range(4):
    nx,ny=sx+dx[k],sy+dy[k]
    if 0<= nx< n and 0<=ny <n:
        if graph[nx][ny] != "*":
            dir=k
            break
q=deque()
def bfs(x, y, dir):
    q.append([x, y, dir])
    check[x][y][dir] = 0
    ans = []
    while q:
        x, y, dir = q.popleft()
        
        # 방향 유지한채 다음으로 움직일 칸 설정
        nx = x + dx[dir]
        ny = y + dy[dir]
        if 0 <= nx < n and 0 <= ny < n:
            if not check[nx][ny][dir] or check[nx][ny][dir] > check[x][y][dir]: # 한번도 도달 안했거나 도달했는데 더 작은값으로 갱신할 수 있으면
                if graph[nx][ny] != '*': # 벽이 아니라면 방향 유지
                    check[nx][ny][dir] = check[x][y][dir] 
                    
                    # 만약 도착지라면 ans에 따로 넣음
                    if nx == fx and ny == fy:
                        ans.append(check[nx][ny][dir])
                        continue
                    q.append([nx, ny, dir])
                    
                    # 만약 거울이라면 방향 바꿔야 하므로 turn함수 실행
                    if graph[nx][ny] == '!':
                        turn(nx, ny, dir)

    print(min(ans))

def turn(x, y, dir): 
    # 바꿔야 하는 방향은 90 or 270 회전이므로 일정한 구간 반복으로  구현 가능
    ndir = [(dir+1) % 4, (dir+3) % 4]
    for d in ndir:
        if not check[x][y][d] or check[x][y][d] > check[x][y][dir] + 1: # 한번도 도달 안했거나 도달했는데 더 작은값으로 갱신할 수 있으면
            check[x][y][d] = check[x][y][dir] + 1
            q.append([x, y, d])

bfs(sx, sy, dir)
