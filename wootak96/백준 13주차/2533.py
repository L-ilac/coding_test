import sys
sys.setrecursionlimit(10**7)
n=int(sys.stdin.readline())
g=[[] for _ in range(n+1)]
check=[False for _ in range(n+1)]
dp=[[1,0] for _ in range(n+1)]

# dp[n][0] : n번째 트리를 루트로 하는 서브 트리 기준, 루트가 얼리어답터일 때
# dp[n][1] : n번째 트리를 루트로 하는 서브 트리 기준, 루트가 얼리어답터가 아닐 때


for _ in range(n-1):
    x,y=map(int,sys.stdin.readline().split())
    g[x].append(y)
    g[y].append(x)

def dfs(x):
    check[x]=True
    for y in g[x]:
        if check[y]==False:
            dfs(y)

            # 루트가 얼리어답터면, 자식이 얼리어답터일 때, 아닐 때 최소값 비교
            dp[x][0]+=min(dp[y][0],dp[y][1])

            # 루트가 얼리어답터 아니면, 자식이 무조건 얼리어답터
            dp[x][1]+=dp[y][0]

dfs(1)
print(min(dp[1][0],dp[1][1]))
