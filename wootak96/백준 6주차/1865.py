import sys

INF=sys.maxsize

def bf(start):
    dist=[INF]*(n+1)

    for i in range(n):
        # 반복마다 모든 간선 확인
        for j in range(2*m+w):
            cur = g[j][0] 
            next = g[j][1] 
            cost = g[j][2] 

            if dist[next] > cost + dist[cur]:
                dist[next] = cost + dist[cur]
                # i==n-1이면 n번 돌린건데 이때도 갱신이 발생하면 음의 싸이클 존재
                if i == n - 1:
                    return True
    return False

tc=int(input())

for _ in range(tc):
    n,m,w=map(int,input().split())
    g=[]

    for _ in range(m):
        s,e,t=map(int,input().split())
        g.append([s,e,t])
        g.append([e,s,t])

    for _ in range(w):
        s,e,t=map(int,input().split())
        g.append([s,e,-t])

    if bf(1):
        print("YES")
    else:
        print("NO")
