from heapq import heappush, heappop

n=int(input())
g=[]
for _ in range(n):
    g.append(list(map(int,input().split())))
g.sort()
heap=[]


for i in range(n):
    if i==0:
        heappush(heap,[g[i][1],g[i][0]])
    

    else:
        if g[i][0]<heap[0][0]:
            heappush(heap,[g[i][1],g[i][0]])
        
        else:
         
            heappop(heap)
            heappush(heap,[g[i][1],g[i][0]])

print(len(heap))
