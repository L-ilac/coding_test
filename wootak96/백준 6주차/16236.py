import sys
import heapq
from collections import deque


n=int(sys.stdin.readline())
graph=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]

dx=[0,-1,0,1]
dy=[1,0,-1,0]

# 아기 상어 시작 위치 확인
for i in range(n):
    for j in range(n):
        if graph[i][j]==9:
            ex,ey=i,j
        
lv=2
eat=0
time=0



def bfs(x,y):
    
    global lv
    global time
    global ex,ey
    global eat
    heap_q=[]
    graph[x][y]=0
    q=deque()
    q.append((x,y))
    dist[x][y]=0
    # bfs를 이용해 최단거리의 먹이 찾음
    while q:
        sx,sy=q.popleft()
        for k in range(4):
            nx,ny=sx+dx[k],sy+dy[k]
            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny]<=lv and dist[nx][ny]==-1:
                    dist[nx][ny]=dist[sx][sy]+1
                    # 우선순위 큐를 이용해 거리, 행, 열순으로 우선순위를 둠
                    if 0<graph[nx][ny]<lv: 
                        heapq.heappush(heap_q,(dist[nx][ny],nx,ny))
                      
                    q.append((nx,ny))
    # 만약 큐에 먹이가 있으면 먹고 레벨 처리, 없으면 먹이가 없다는 뜻이므로 종료
    if heap_q:
        ti,fx,fy=heapq.heappop(heap_q)
        graph[fx][fy]=0
        eat+=1
        if eat==lv:
            eat=0
            lv+=1
        time += ti
        ex,ey=fx,fy
    else:
        print(time) 
        exit()
        
while True:
    dist=[[-1 for _ in range(n)] for _ in range(n)]
    bfs(ex,ey)
