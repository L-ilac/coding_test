import sys
from itertools import combinations
import copy

n,m=map(int,sys.stdin.readline().split())
real_graph=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]

cnt=0
chicken_store=[]
for i in range(n):
    for j in range(n):
        if real_graph[i][j]==2:
            chicken_store.append([i,j])

chicken_store=list(combinations(chicken_store,m))

def chicken_dis(x): #([0, 1], [4, 4])
    graph=copy.deepcopy(real_graph)
    cs=[]
    cnt=0
    for i in range(n):
        for j in range(n):
            if graph[i][j]==2:
                if [i,j] in x:
                    cs.append([i,j])
                    
                else:
                    graph[i][j]=0
    ans=0
    for i in range(n):
        for j in range(n):
            if graph[i][j]==1:
                dis=sys.maxsize
                for x,y in cs:
                    dis=min(dis,abs(x-i)+abs(y-j))
                ans+=dis       
    
    return ans

real_ans=[]
for i in chicken_store:
    real_ans.append(chicken_dis(i))
    
print(min(real_ans))
