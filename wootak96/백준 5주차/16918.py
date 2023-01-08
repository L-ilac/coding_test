import sys
r,c,n=map(int,sys.stdin.readline().split())
graph=[list(map(str,sys.stdin.readline())) for _ in range(r)]
dx=[0,0,1,-1]
dy=[1,-1,0,0]

for i in range(r):
    for j in range(c):
        if graph[i][j]=="O":
            graph[i][j]=[graph[i][j],0]
        else:
            graph[i][j]=[graph[i][j],0]


now=0
while True:
    now+=1
    if now%2==0:
        for i in range(r): 
            for j in range(c):
                if graph[i][j][0]==".": # 빈칸에 폭탄 채우기
                    graph[i][j]=["O",0]
                else:
                    graph[i][j][1]+=1 # 폭탄인 애들은 시간 더해주기
    
    else: 
        temp=[] # 폭탄 터트리기
        for i in range(r):
            for j in range(c):
                if graph[i][j]==["O",2]:
                    temp.append([i,j]) 
        for x,y in temp:
            graph[x][y]=[".",0]
            for k in range(4):
                        nx,ny=x+dx[k],y+dy[k]
                        if 0<=nx<r and 0<=ny<c:
                            graph[nx][ny]=[".",0]

        for i in range(r): # 나머지 폭탄 시간 더해주기
            for j in range(c):
                if graph[i][j][0]=="O":
                    graph[i][j][1]+=1
    
    if now==n:
        break

for i in range(r):
    for j in range(c):
        print(graph[i][j][0],end="")
    print()
