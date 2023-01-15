from collections import deque
import sys
input=sys.stdin.readline
m,n,h=map(int,input().split())
dist=[[[-1 for _ in range(m)] for _ in range(n)] for _ in range(h)]

graph=[[list(map(int,input().split())) for _ in range(n)] for i in range(h)]
q=deque()
cnt=0
dx=[0,0,1,-1,0,0]
dy=[1,-1,0,0,0,0]
dp=[0,0,0,0,1,-1]
for z in range(h):
    for i in range(n):
        for j in range(m):
            if graph[z][i][j]==1:
                dist[z][i][j] = 0
                q.append((z,i,j))
            elif graph[z][i][j]==0:
                cnt+=1

if cnt==0:
    print(0)
    exit()

while q:
    p,x,y=q.popleft()
    for k in range(6):
        np,nx,ny=p+dp[k],x+dx[k],y+dy[k]
        if 0<=np<h and 0<=nx<n and 0<=ny<m:
            if graph[np][nx][ny]== 0 and dist[np][nx][ny]==-1:
                dist[np][nx][ny] = dist[p][x][y]+1
                q.append((np,nx,ny))

k=[]
for i in dist:
    for j in i:
        k.append(max(j))


for z in range(h):
    for i in range(n):
        for j in range(m):
            if dist[z][i][j]==-1 and graph[z][i][j]==0:
                
            
                print(-1)
                exit()

print(max(k))
