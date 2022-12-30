from collections import deque
n=int(input())
# time : 초기시간, degree : 진입차수, g : 간선
time=[0 for _ in range(n+1)]
degree=[0 for _ in range(n+1)]
g=[[] for _ in range(n+1)]

# 진입차수, 간선, 초기시간 설정
for i in range(n):
    arr=list(map(int,input().split()))
    for j in range(len(arr)-1):
        if j==0:
            time[i+1]=arr[j]
        
        else:
            g[arr[j]].append(i+1)
            degree[i+1]+=1

q=deque()
ans=0

# 진입차수가 0이면 필요한 선수건물이 없다는 뜻이고 처음에 바로 작업 시작 가능하니깐 큐에 넣음
for i in range(1,n+1):
    if degree[i]==0:
        q.append(i)

# 답 저장할 ans
ans=[0]*(n+1)

while q:
    x=q.popleft()
    # 초기시간 더함
    ans[x]+=time[x]
    
    # 간선에 있는 정보로 다음 건물 찾고 그 건물 접근했으니까 진입차수 줄여줌
    for y in g[x]:
        degree[y]-=1
        
        # 최대값으로 갱신해야함, 예제 
        ans[y] = max(ans[y], ans[x])
        if degree[y]==0:
            q.append(y)

for i in range(1,n+1):
    print(ans[i])
