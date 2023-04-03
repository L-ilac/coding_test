from heapq import heappush,heappop

n=int(input())

house=[]
go=[]
temp=[]

#temp에 모든 집~사무실 넣고
for _ in range(n):
    x,y=map(int,input().split())    
    start=min(x,y)
    end=max(x,y)
    temp.append([start,end])



limit=int(input())


# limit보다 길이가 큰 집~사무실 들은 애초에 고려 대상이 아님, 무조건 불가능
for start,end in temp:
    if end-start<=limit:

        # 확인해야할 집들의 순서는 도착지점을 기준으로 사무실 위치를 기준으로 우선순위 큐에 넣음
        heappush(house,[end,start])

        # 출발점 (go) 설정
        go.append(start)

# go는 오름차순으로 설정
# can_ride = 현재 상황에서 철도를 이용할 수 있는 집~사무실
can_ride=[]

go=list(set(go))
go.sort()


ans=0
for start in go:



    # go에 있는 출발점들을 기준으로 사무실의 위치는 현재 출발점 + limit
    end=start+limit

    # 사무실의 위치가 start보다 작으면 버림
    while can_ride and can_ride[0][0]<start:
        heappop(can_ride)

    # 사무실의 위치가 start보다 크고 end보다 작으면 조건부합하므로 can_ride에 넣음
    while house and house[0][0]<=end:
        y,x=heappop(house)
        heappush(can_ride,[x,y])
    
    
    ans=max(ans,len(can_ride))


print(ans)
