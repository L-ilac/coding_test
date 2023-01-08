import sys
n,m=map(int,sys.stdin.readline().split())
graph=[list(map(str,sys.stdin.readline())) for _ in range(n)]
alpha_check=[False for _ in range(26)]
dx=[0,0,1,-1]
dy=[1,-1,0,0]
ans=0
def dfs(x,y,cnt):
    global ans
    ans = max(ans, cnt)
    alpha_check[ord(graph[x][y])-65]=True
    for k in range(4):
        nx,ny=x+dx[k],y+dy[k]
        if 0<=nx<n and 0<=ny<m and alpha_check[ord(graph[nx][ny])-65]==False:
            
                # 백트래킹으로 모든 경우를 탐색해야 하므로 방문했을 때 방문체크를 하고 dfs 실행 후 다시 방문체크 풀어줘야 한다.
                alpha_check[ord(graph[nx][ny])-65]=True
                dfs(nx,ny,cnt+1)
                alpha_check[ord(graph[nx][ny])-65]=False
    
dfs(0,0,1)
print(ans)
