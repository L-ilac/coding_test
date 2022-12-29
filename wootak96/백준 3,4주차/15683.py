import sys
import itertools
from collections import deque
import copy

n,m=map(int,sys.stdin.readline().split())
graph=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]

# cctv 1~5번 , 1번 위쪽, 2번 오른쪽, 3번 아래쪽, 4번 왼쪽
num1=[1,2,3,4] 
num2=[[2,4],[1,3]]
num3=[[1,2],[2,3],[3,4],[4,1]]
num4=[[1,2,3],[1,2,4],[1,3,4],[2,3,4]]
num5=[[1,2,3,4]]
cctv=[]
num=[]

# 모든 cctv 위치와 어떤 종류의 cctv인지 확인
for i in range(n):
    for j in range(m):
        if graph[i][j] != 0 and graph[i][j] != 6:
            if graph[i][j]==1:
                cctv.append([i,j])
                num.append(num1)
            elif graph[i][j]==2:
                cctv.append([i,j])
                num.append(num2)
            elif graph[i][j]==3:
                cctv.append([i,j])
                num.append(num3)
            elif graph[i][j]==4:
                cctv.append([i,j])
                num.append(num4)
            elif graph[i][j]==5:
                cctv.append([i,j])
                num.append(num5)

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def bfs_up(x,y):
    q=deque()
    q.append((x,y))
    while q:
        ex,ey=q.popleft()
        k=3
        nx,ny=ex+dx[k],ey+dy[k]
        if 0<=nx<n and 0<=ny<m:
            if temp_graph[nx][ny] != 6:
                if temp_graph[nx][ny]==0:
                    temp_graph[nx][ny]="#"
                    q.append((nx,ny))
                else:
                    q.append((nx,ny))
def bfs_right(x,y):
    q=deque()
    q.append((x,y))
    while q:
        ex,ey=q.popleft()
        k=0
        nx,ny=ex+dx[k],ey+dy[k]
        if 0<=nx<n and 0<=ny<m:
            if temp_graph[nx][ny] != 6:
                if temp_graph[nx][ny]==0:
                    temp_graph[nx][ny]="#"
                    q.append((nx,ny))
                else:
                    q.append((nx,ny))
def bfs_down(x,y):
    q=deque()
    q.append((x,y))
    while q:
        ex,ey=q.popleft()
        k=2
        nx,ny=ex+dx[k],ey+dy[k]
        if 0<=nx<n and 0<=ny<m:
            if temp_graph[nx][ny] != 6:
                if temp_graph[nx][ny]==0:
                    temp_graph[nx][ny]="#"
                    q.append((nx,ny))
                else:
                    q.append((nx,ny))
def bfs_left(x,y):
    q=deque()
    q.append((x,y))
    while q:
        ex,ey=q.popleft()
        k=1
        nx,ny=ex+dx[k],ey+dy[k]
        if 0<=nx<n and 0<=ny<m:
            if temp_graph[nx][ny] != 6:
                if temp_graph[nx][ny]==0:
                    temp_graph[nx][ny]="#"
                    q.append((nx,ny))
                else:
                    q.append((nx,ny))

# num에는 브루트포스 방식으로 모든 경우를 테스트할 cctv의 방향들이 저장돼 있음  
num=list(itertools.product(*num))


ans=99999
for x in range(len(num)):
    # 임시 지도 만들고 임시 지도에서 테스트 케이스 하나씩 실행
    temp_graph = copy.deepcopy(graph)
   
    for i in range(len(cctv)):
        if type(num[x][i])==int:
            if num[x][i]==1:
                bfs_up(cctv[i][0],cctv[i][1])
            elif num[x][i]==2:
                bfs_right(cctv[i][0],cctv[i][1])
            elif num[x][i]==3:
                bfs_down(cctv[i][0],cctv[i][1])
            elif num[x][i]==4:
                bfs_left(cctv[i][0],cctv[i][1])

        else:
            for j in (num[x][i]):
                if j==1:
                    bfs_up(cctv[i][0],cctv[i][1])
                elif j==2:
                    bfs_right(cctv[i][0],cctv[i][1])
                elif j==3:
                    bfs_down(cctv[i][0],cctv[i][1])
                elif j==4:
                    bfs_left(cctv[i][0],cctv[i][1])
   
   
    cnt=0
    for i in range(n):
        for j in range(m):
            if temp_graph[i][j]==0:
                cnt+=1
    ans=min(ans,cnt)

print(ans)
