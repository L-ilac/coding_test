from collections import deque

n,m=map(int,input().split())

# g : 간선, degree : 진입정보
g=[[] for _ in range(n+1)]
degree=[0 for _ in range(n+1)]
for _ in range(m):
    u,v=map(int,input().split())
    g[u].append(v)

for i in g:
    for j in i:
        degree[j]+=1

q=deque()

# 진입차수 0이면 바로 q에 넣음
for i in range(1,n+1):
    if degree[i]==0:
        q.append(i)

while q:
    x=q.popleft()
    print(x,end=" ")
    for y in g[x]:
        degree[y]-=1

        if degree[y]==0:
            q.append(y)
