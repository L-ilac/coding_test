from collections import deque
n,m=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(n)]
check=[[False for _ in range(m)] for _ in range(n)]

for i in range(n):
    hey=False
    for j in range(m):
        if graph[i][j]==2:
            start_x=i
            start_y=j
            hey=True
            break
    if hey==True:
        break

graph[start_x][start_y]=0

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def bfs(x,y):
    check[x][y]=True
    q=deque()
    q.append((x,y))
    while q:
        new_x,new_y=q.popleft()
        for k in range(4):
            nx,ny=new_x+dx[k],new_y+dy[k]
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny]==1 and check[nx][ny]==False:
                    check[nx][ny]=True
                    graph[nx][ny]=graph[new_x][new_y]+1
                    q.append((nx,ny))

bfs(start_x,start_y)
for i in range(n):
    for j in range(m):
        if check[i][j]==False and graph[i][j]!=0:
            graph[i][j]=-1


for i in graph:
    print(*i)
