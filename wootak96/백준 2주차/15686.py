import sys
#조합 함수 호출
from itertools import combinations 
import copy

n,m=map(int,sys.stdin.readline().split())
real_graph=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]

cnt=0
#치킨집 찾기
chicken_store=[]
for i in range(n):
    for j in range(n):
        if real_graph[i][j]==2:
            chicken_store.append([i,j])

#가능한 치킨집 조합
chicken_store=list(combinations(chicken_store,m))

# 치킨집 거리 계산
def chicken_dis(x):
    
    # real_graph에다가 계산하면 치킨집이 변하니까 복사본(graph) 만들어서 복사본에다가 계산
    graph=copy.deepcopy(real_graph)
    cs=[]
    cnt=0
    for i in range(n):
        for j in range(n):
            if graph[i][j]==2:
                if [i,j] in x:
                    #조합에 있는 치킨집이라면 cs에 넣음
                    cs.append([i,j])
                else:
                    #조합에 없으면 치킨집이라도 그냥 빈공간 처리
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
