# https://koosaga.com/14
# dfs를 제곱번 돌리는 n^2 말고 dfs를 두번 돌리는 n 방식

import sys
sys.setrecursionlimit(10**6)
n=int(sys.stdin.readline())
tree=[[] for _ in range(n+1)]

# 트리 간선 전처리
for _ in range(n-1):
    parent,son,g=map(int,sys.stdin.readline().split())
    tree[parent].append([son,g])
    tree[son].append([parent,g])

# dfs
def dfs(x,now):
    for node,g in tree[x]:
        if check[node]==-1:
            check[node]=now+g
            dfs(node,now+g)

check=[-1 for _ in range(n+1)]
check[1]=0
dfs(1,0)

max_=max(check)
max_index=check.index(max_)

check=[-1 for _ in range(n+1)]
check[max_index]=0
dfs(max_index,0)

print(max(check))
