import sys
n,c=map(int,input().split())
# n : 마을 수, c : 버스용량

m=int(input())
parcel=[]
for _ in range(m):
    sp,de,box=map(int,input().split())
    parcel.append([de,sp,box])


# 도착지점을 기준으로 오름차순 정렬
parcel.sort()

bus=[c for _ in range(n+1)]
cnt=0
ans=0



for de,sp,box in parcel:
    
    temp=min(bus[sp:de])
    temp=min(temp,box)
    ans+=temp
    for i in range(sp,de):
        bus[i]-=temp

print(ans)
