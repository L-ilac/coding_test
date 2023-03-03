import copy
import sys
from collections import deque
k=int(input())
for _ in range(k):
    n,m=map(int,sys.stdin.readline().split())
    graph=[list(map(str,sys.stdin.readline().rstrip())) for _ in range(n)]
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    key={}
    keys=input()
    for i in keys:
        key[i]=True
    start=[]
    ans=0
    key["."]=True
    
    
    # 처음 스타트할 지점 찾기
    for i in range(n):
        for j in range(m):
            # 테두리에 있는데 벽이 아닌 지점들은 모두 다 스타트지점(문, 열쇠, 문서 모두 다)
            if i==0 or i==n-1 or j==0 or j==m-1:
                if graph[i][j]!="*":
                    start.append([i,j])
                    # 테두리에 문서가 있으면 문서 먹고 .으로 바꿈
                    if graph[i][j]=="$":
                        ans+=1
                        graph[i][j]="."
                    # 테두리에 열쇠(소문자)가 있으면 키목록에 추가하고 .으로 바꿈
                    elif graph[i][j]!="." and graph[i][j]==graph[i][j].lower():
                        key[graph[i][j]]=True
                        graph[i][j]="."
                        
                    # 테두리에 있는 대문자는 그냥 아무 처리 안하고 스타트지점에 집어넣음

    def bfs(x,y):
        global ans
        q=deque()
        check[x][y]=True
        if graph[x][y]!=".":
            if graph[x][y].lower() in key.keys():
                graph[x][y]="."
                q.append((x,y))
        else:  
            q.append((x,y))
    
        while q:
            x,y=q.popleft()
    
            for k in range(4):
                nx,ny=x+dx[k],y+dy[k]
                if 0<=nx<n and 0<=ny<m and check[nx][ny]==False:
                    if graph[nx][ny] !="*":
                        #일반적인 길(.)이면
                        if graph[nx][ny]==".":
                            check[nx][ny]=True
                            q.append((nx,ny))

                        else:
                            # 문서면
                            if graph[nx][ny]=="$":
                                graph[nx][ny]="."
                                ans+=1
                                check[nx][ny]=True
                                q.append((nx,ny))
                            
                            else: # 소문자(열쇠면)
                                if graph[nx][ny]==graph[nx][ny].lower():
                                    key[graph[nx][ny].lower()]=True
                                    graph[nx][ny]="."
                                    check[nx][ny]=True
                                    q.append((nx,ny))
                                    
                                    #대문자(문이면)
                                else:# 열쇠가 있으면
                                    if graph[nx][ny].lower() in key.keys():
                                        graph[nx][ny]="."
                                        check[nx][ny]=True
                                        q.append((nx,ny))
                                        #열쇠가 없으면
                                    else:
                                        continue
    
    while True:
        temp_graph=copy.deepcopy(graph)
        # 계속해서 bfs탐색하면서 그래프 비교, 이전 그래프와 비교했는데 달라진게 없으면 이제 끝난 것
        
        # 한번 돌 때 스타트지점에 있는 모든 점들을 기준으로 bfs 돈다. 그러면 각 지점에서 처리할 수 있는 것들은 모두 처리가 됨.
        for x,y in start:
            check=[[False for _ in range(m)]for _ in range(n)]
            bfs(x,y)
            
        if temp_graph==graph:
            break    
    print(ans)
