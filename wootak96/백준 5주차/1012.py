z=int(input())
for _ in range(z):
    n,m,k=map(int,input().split())
    map_=[[0]*m for _ in range(n)]
    check=[[False]*m for _ in range(n)]

    for _ in range(k):
        x,y=map(int,input().split())
        map_[x][y]=1

    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    ans=[]
    def dfs(x,y,cnt):
        if cnt==0:
            ans.append(1)
        if check[x][y]==False:
            check[x][y]=True
        

        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if map_[nx][ny]==1 and check[nx][ny]==False:
                        dfs(nx,ny,cnt+1)
                

    for i in range(n):
        for j in range(m):
            if map_[i][j]==1 and check[i][j]==False:
                dfs(i,j,0)

    print(len(ans))
