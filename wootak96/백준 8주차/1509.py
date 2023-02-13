# 참고 https://yabmoons.tistory.com/592

import sys
INF=sys.maxsize

s=list(input())
n=len(s)
p=[[False for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        # 글자가 한자리 수일 때
        if i==j:
            p[i][j]=True    
        # 글자가 두자리 수일 때
        elif i==j-1:      
            if s[i]==s[j]:
                p[i][j]=True

# 글자가 세자리 수 이상일 때
# i,j 바꾼 이유는 안바꾸면 n의 3승까지 해야함
for j in range(n):
    for i in range(n):
        if j-i>=2:
            if s[i]==s[j] and p[i+1][j-1]==True:
                p[i][j]=True

# dp[0]에서 start-1이 나오면 -1(마지막 항)이 필요하기 때문에 n+1로 선언
dp=[INF]*(n+1)
# dp[-1]은 dp[0]을 위한 세팅
dp[-1]=0



for end in range(n):
    for start in range(end + 1):
        if p[start][end]:
            dp[end] = min(dp[end], dp[start-1] + 1)
print(dp[n-1])
