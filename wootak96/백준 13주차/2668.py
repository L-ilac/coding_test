import sys
n=int(input())
g=[[] for _ in range(n+1)]
for i in range(1,n+1):
    k=int(input())
    g[i].append(k)

def dfs(x):
    global start
 
    for y in g[x]:
        if check[y]==False:
            if y==start:
                return True
            else:
                check[y]=True
                return dfs(y)
        

ans=[]
for i in range(1,n+1):
    check=[False for _ in range(n+1)]
    start=i
    if dfs(i):
        ans.append(i)

ans.sort()
print(len(ans))
for i in ans:
    print(i)
