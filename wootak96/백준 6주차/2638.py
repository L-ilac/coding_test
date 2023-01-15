from collections import deque
import sys


n,m=map(int,sys.stdin.readline().split())
graph=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
cheese=0

# 총 치즈 갯수 확인
for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            cheese+=1

dx=[0,0,1,-1]
dy=[1,-1,0,0]

graph[0][0]=-1

# 오염된 공기는 -1로 바꾸는 bfs 함수
def outside_air_bfs(x,y):
    q=deque()
    q.append((x,y))
    check[x][y]=True

    while q:
        sx,sy=q.popleft()
        for k in range(4):
            nx,ny=sx+dx[k],sy+dy[k]
            if 0<=nx<n and 0<=ny<m :
                if check[nx][ny]==False and graph[nx][ny]==0 or check[nx][ny]==False and graph[nx][ny]==-1:
                    check[nx][ny]=True
                    graph[nx][ny]=-1
                    q.append((nx,ny))

# 외부 치즈 확인하는 함수
def outside_cheese():
    global cheese
    for i in range(n):
        for j in range(m):
            
            if graph[i][j]==1:
                cnt=0
                for k in range(4):
                    ni,nj=i+dx[k],j+dy[k]
                    if graph[ni][nj]==-1:
                        cnt+=1
                # 외부 공기와 닿은 면적이 두 개 이상이면 외부 치즈로 판단
                if cnt>=2:
                    graph[i][j]="*"
                    cheese-=1
    # 외부 치즈를 오염된 공기로 바꿈
    for i in range(n):
        for j in range(m):
            if graph[i][j]=="*":
                graph[i][j]=-1
    
z=1

while cheese!=0:
    check=[[False for _ in range(m)] for _ in range(n)]
    outside_air_bfs(0,0)

    outside_cheese()
  
    z+=1
print(z-1)
