import sys
import heapq
INF=sys.maxsize
k=int(input())

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dist,node=heapq.heappop(q)
        
        if distance[node]<dist:
            continue

        for next in g[node]:
            cost = distance[node] + next[1]
            if cost < distance[next[0]]:
                distance[next[0]]=cost
                heapq.heappush(q,(cost,next[0]))
    


for _ in range(k):
    n,d,c=map(int,input().split())

    g=[[] for _ in range(n+1)]
    distance=[INF]*(n+1)

    for l in range(d):
        a,b,s=map(int,input().split())
        g[b].append((a,s))
    
   

    dijkstra(c)
    cnt=0
    ans=[]
    for i in distance:
        if i!=INF:
            cnt+=1
            ans.append(i)
            
    print(cnt,max(ans))
