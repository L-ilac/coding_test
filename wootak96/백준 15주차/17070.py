n=int(input())

graph=[list(map(int,input().split())) for _ in range(n)]

dp=[[[0 for _ in range(3)]for _ in range(n)]for _ in range(n)]
# dp[i][j][0] = ㅡ     dp[i][j][1] =  \         dp[i][j][2] = ㅣ         
dp[0][1][0]=1
for i in range(n):
    for j in range(1,n):
        for k in range(3):
            if k==0:
                if j+1<=n-1 and graph[i][j+1]!=1:
                    dp[i][j+1][0]+=dp[i][j][k]

                if j+1<=n-1 and i+1<=n-1 and graph[i][j+1]!=1 and graph[i+1][j+1]!=1 and graph[i+1][j]!=1:
                    dp[i+1][j+1][1]+=dp[i][j][k]

            elif k==1:
                if j+1<=n-1 and graph[i][j+1]!=1:
                    dp[i][j+1][0]+=dp[i][j][k]

                if j+1<=n-1 and i+1<=n-1 and graph[i][j+1]!=1 and graph[i+1][j+1]!=1 and graph[i+1][j]!=1:
                    dp[i+1][j+1][1]+=dp[i][j][k]

                if i+1<=n-1 and graph[i+1][j]!=1:
                    dp[i+1][j][2]+=dp[i][j][k]

            elif k==2:
                if j+1<=n-1 and i+1<=n-1 and graph[i][j+1]!=1 and graph[i+1][j+1]!=1 and graph[i+1][j]!=1:
                    dp[i+1][j+1][1]+=dp[i][j][k]

                if i+1<=n-1 and graph[i+1][j]!=1:
                    dp[i+1][j][2]+=dp[i][j][k]


print(sum(dp[n-1][n-1]))
