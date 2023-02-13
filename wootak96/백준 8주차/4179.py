import sys
from collections import deque
INF=sys.maxsize
n,m=map(int,input().split())
graph=[list(map(str,input())) for _ in range(n)]
dx=[0,0,1,-1]
dy=[1,-1,0,0]
q=deque()

for i in range(n):
    for j in range(m):
        if graph[i][j]=="J":
            q.append((0,i,j))

for i in range(n):
    for j in range(m):
        if graph[i][j]=="F":
            q.append((-1,i,j))

ans="IMPOSSIBLE"
def bfs():
    global ans
    while q:
        time,x,y=q.popleft()

        if (x==0 or x==n-1 or y==0 or y==m-1) and graph[x][y]!="F" and time>-1:
            ans=time+1
            return
        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]

            if 0<=nx<n and 0<=ny<m and graph[nx][ny] != "#":
                
                if time!= -1 and graph[nx][ny] ==".":
                    graph[nx][ny]=time+1
                    q.append((time+1,nx,ny))

                elif time==-1 and graph[nx][ny] != "F" :
                    graph[nx][ny]="F"
                    q.append((-1,nx,ny))

            
bfs()
print(ans)
