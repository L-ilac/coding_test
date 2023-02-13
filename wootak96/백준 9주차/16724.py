import sys
from collections import deque
n,m=map(int,input().split())

graph=[list(map(str,sys.stdin.readline())) for _ in range(n)]
parent=[[[i,j] for j in range(m)] for i in range(n)]
check=[[False for _ in range(m)] for _ in range(n)]
ans=0

# 부모 찾는수함수
def find(x,y):
    if parent[x][y]!=[x,y]:
        parent[x][y]=find(parent[x][y][0],parent[x][y][1])

    return parent[x][y]

# 부모가 다르면 부모 통일해주는 함수
def union(x,y,nx,ny):
    [x,y]=find(x,y)
    [nx,ny]=find(nx,ny)

    if x<nx:
        parent[nx][ny]=[x,y]
    elif x>nx:
        parent[x][y]=[nx,ny]
    else:
        if y<ny:
            parent[nx][ny]=[x,y]
        else:
            parent[x][y]=[nx,ny]

def bfs(x,y):
    global ans
    check[x][y]=True
    q=deque()
    q.append((x,y))

    while q:
        x,y=q.popleft()
        if graph[x][y]=="U":
            nx,ny=x-1,y
        elif graph[x][y]=="D":
            nx,ny=x+1,y
        elif graph[x][y]=="L":
            nx,ny=x,y-1
        elif graph[x][y]=="R":
            nx,ny=x,y+1

        if 0<=nx<n and 0<=ny<m:
            if find(nx,ny)!=find(x,y):
                # 일반적인 경우 
                if check[nx][ny]==False:
                    union(x,y,nx,ny)
                    check[nx][ny]=True
                    q.append((nx,ny))
                # 이미 사이클이 만들어져 있는데 중간에 들어가는 경우
                else:
                    union(x,y,nx,ny)
            # 사이클 갯수 
            else:
                ans+=1
                return


for i in range(n):
    for j in range(m):
        if check[i][j]==False:
            bfs(i,j)


print(ans)
