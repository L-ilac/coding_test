import sys
sys.setrecursionlimit(100000)
n,m=map(int,input().split())

name=[]
for _ in range(n):
    name.append(int(sys.stdin.readline()))

dp=[[-1 for _ in range(1001)] for _ in range(n)]
def cal(idx,list_len):
    
    if idx>=n-1:
        return 0
    

    if dp[idx][list_len]!=-1:
        return dp[idx][list_len]
    
    # 한칸 밑에
    dp[idx][list_len] = (m-list_len)**2 + cal(idx+1,name[idx+1])

    # 이어서 쓸 수 있다면 
    if list_len + name[idx+1] + 1 <=m: 
      
        # 한칸 밑에 저은 경우랑 이어서 쓰는 경우 비교해서 최소값 갱신
        dp[idx][list_len]=min(dp[idx][list_len],cal(idx+1,list_len + 1 + name[idx+1]))

    return dp[idx][list_len]

print(cal(0,name[0]))
