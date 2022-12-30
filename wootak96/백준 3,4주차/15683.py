import sys
import itertools
from collections import deque
import copy

n,m=map(int,sys.stdin.readline().split())
graph=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]

# cctv 1~5번까지의 방향 설정
num1=[1,2,3,4]
num2=[[2,4],[1,3]]
num3=[[1,2],[2,3],[3,4],[4,1]]
num4=[[1,2,3],[1,2,4],[1,3,4],[2,3,4]]
num5=[[1,2,3,4]]
cctv=[]

num=[]

# 모든 cctv 위치와 종류 확인
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

# product함수로 만들 수 있는 경우의 수 num에 저장
num=list(itertools.product(*num))


ans=sys.maxsize
for x in range(len(num)):

    # 임시 그래프 만들고 임시 그래프에 테스트 해봄
    temp_graph = copy.deepcopy(graph)
   
    for i in range(len(cctv)):
    
        # 나눈 이유는 1번 cctv의 경우에 num에 있는 값들이 정수 하나의 형태로 나와 타입이 int고, 나머지 경우에는 여러 방향이라 정수가 여러개인 list 타입으로 나와서 케이스 분류를 함
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
    
    # 빈 구역 찾아서 
    for i in range(n):
        for j in range(m):
            if temp_graph[i][j]==0:
                cnt+=1
    ans=min(ans,cnt)

print(ans)
