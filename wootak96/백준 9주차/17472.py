import sys
from collections import deque
from heapq import heappush,heappop
INF=sys.maxsize
n,m=map(int,sys.stdin.readline().split())
graph=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
dx=[0,0,1,-1]
dy=[1,-1,0,0]


# 대륙별로 구분하기, 대륙 1,2,3,4 ~~
def continent(x,y):
    check[x][y]=True
    q=deque()
    q.append((x,y))
    graph[x][y]=g

    while q:
        x,y=q.popleft()
        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny] != 0 and check[nx][ny]==False :
                    check[nx][ny]=True
                    graph[nx][ny]=g
                    q.append((nx,ny))


g=0
check=[[False for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if graph[i][j] != 0 and check[i][j]==False:
            g+=1
            continent(i,j)

            
# 대륙별로 부모 정설정
parent=[i for i in range(g+1)]

def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])

    return parent[x]


def union(a,b):
    a=find(a)
    b=find(b)

    if a<b:
        parent[b]=a
    else:
        parent[a]=b

# 최단거리 다리 찾는 bfs
def bfs(x,y,cnt,dir):
    fuck=graph[x][y] # 처음 시작하는 대륙의 번호
    check[x][y]=True
    q=deque()
    for k in range(4): # 처음 스타트 지점에서 갈 수 있는 네방향 확인하고 갈 수 있으면 큐에 입삽입
        nx,ny=x+dx[k],y+dy[k]
        if 0<=nx<n and 0<=ny<m:
            if graph[nx][ny]==0:
                q.append((nx,ny,cnt,k))

  
  
    while q:
        x,y,cnt,k=q.popleft()
        nx,ny=x+dx[k],y+dy[k]
        if 0<=nx<n and 0<=ny<m:
            if graph[nx][ny]==0:
                q.append((nx,ny,cnt+1,k)) # 계속 탐색할 수 있으면 방향 유지하면서 탐색

            elif graph[nx][ny] != fuck and graph[nx][ny] != 0: # 새로운 대륙 만나고 거리가 2이상이면 힙큐에입삽입
                if cnt+1>=2:
                    heappush(temp,[cnt+1,graph[nx][ny],fuck])
                    
                
temp=[]

# 최단거리 다리 탐색
for i in range(n):
    for j in range(m):
        if graph[i][j]!=0:
            bfs(i,j,0,-1)

if not temp:
    print(-1)
    exit()

cnt=0
ans=0

# 최소 스패닝 
while temp:
    dist,x,y=heappop(temp)
    if find(x)!=find(y):
        union(x,y)
        cnt+=1
        ans+=dist
    
    if cnt==g-1:
        break

if cnt!=g-1:
    print(-1)
else:
    print(ans)
