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





# 실패 코드

'''
from collections import deque
n=int(input())

graph=[list(map(str,input())) for _ in range(n)]
door=[]
for i in range(n):
    for j in range(n):
        if graph[i][j]=="#":
            door.append([i,j])
check=[[False for _ in range(n)] for _ in range(n)]
dist=[[-1 for _ in range(n)] for _ in range(n)]
start_x=door[0][0]
start_y=door[0][1]
end_x=door[1][0]
end_y=door[1][1]

dx=[0,0,1,-1]
dy=[1,-1,0,0]
check[start_x][start_y]=True
dist[start_x][start_y]=0



def bfs(x,y):

    q=deque()

    for k in range(4):
        x,y=start_x+dx[k],start_y+dy[k]
        if 0<=x<n and 0<=y<n:
            if graph[x][y] == ".":
                q.append((x,y,k))
                check[x][y]=True
                dist[x][y]=0
            elif graph[x][y] == "!":
                q.append((x,y,k))
                check[x][y]=True
                dist[x][y]=1

    while q:
        ex,ey,previous=q.popleft()

        if ex==end_x and ey==end_y:
            break
        
        if graph[ex][ey]=="." or graph[ex][ey]=="#":
            
            if previous==0:
                nx,ny=ex,ey+1
        
            elif previous==1:
                nx,ny=ex-1,ey

            elif previous==2:
                nx,ny=ex+1,ey

            elif previous==3:
                nx,ny=ex,ey-1
            
            if graph[nx][ny] != "*" and check[nx][ny]==False:
                check[nx][ny]=True
                dist[nx][ny]=dist[ex][ey]
                q.append((nx,ny,previous))
        
        elif graph[ex][ey]=="!":
            if previous==0:
                nx,ny=ex+1,ey
                previous1=2
                nx2,ny2=ex-1,ey
                previous2=1
                nx3,ny3=ex,ey+1
                previous3=0
            
                
        
            elif previous==1:
                nx,ny=ex,ey+1
                previous1=0
                nx2,ny2=ex,ey-1
                previous2=3
                nx3,ny3=ex-1,ey
                previous3=1

            elif previous==2:
                nx,ny=ex,ey+1
                previous1=0
                nx2,ny2=ex,ey-1
                previous2=3
                nx3,ny3=ex+1,ey
                previous3=2

            elif previous==3:
                nx,ny=ex+1,ey
                previous1=2
                nx2,ny2=ex-1,ey
                previous2=1
                nx3,ny3=ex,ey-1
                previous3=3

            if graph[nx][ny] != "*" and check[nx][ny]==False:
                check[nx][ny]=True
                dist[nx][ny]=dist[ex][ey]+1
                q.append((nx,ny,previous1))
            
            if graph[nx2][ny2] != "*" and check[nx2][ny2]==False:
                check[nx2][ny2]=True
                dist[nx2][ny2]=dist[ex][ey]+1
                q.append((nx2,ny2,previous2))
            
            if graph[nx3][ny3] != "*" and check[nx3][ny3]==False:
                check[nx3][ny3]=True
                dist[nx3][ny3]=dist[ex][ey]
                q.append((nx3,ny3,previous3))
               

bfs(start_x,start_y)
print(dist[end_x][end_y])

'''
