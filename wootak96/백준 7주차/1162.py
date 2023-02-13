import sys
from heapq import heappush, heappop 
INF=sys.maxsize

n,m,k=map(int,input().split())

distance=[[INF for _ in range(k+1)] for _ in range(n+1)]
for j in range(k+1):
  distance[1][j]=0


g=[[] for _ in range(n+1)]

for _ in range(m):
  a,b,weight=map(int,input().split())
  g[a].append([b,weight])
  g[b].append([a,weight])

def dijkstra():
    q=[]
    heappush(q,(0,1,0)) # 현재까지 가중치, 지점, 포장횟수

    while q:
        
        dist,node,pave=heappop(q)

        if distance[node][pave]<dist:
            continue
        if pave==k:
           for next in g[node]:
            cost = distance[node][pave] + next[1]
            if cost < distance[next[0]][pave]:
                distance[next[0]][pave]=cost
                heappush(q,(cost,next[0],pave))

        else:
           for next in g[node]:
            cost = distance[node][pave] + next[1]
            cost2 = distance[node][pave] + 0

            if cost < distance[next[0]][pave]:
              distance[next[0]][pave]=cost
              heappush(q,(cost,next[0],pave))

            if cost2 < distance[next[0]][pave+1]:
              distance[next[0]][pave+1]=cost2
              heappush(q,(cost2,next[0],pave+1))



dijkstra()

print(min(distance[n]))
