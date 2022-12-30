n, k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

a = sorted(a)
b = sorted(b,reverse = True)

for i in range(k):
	if a[i] < b[i]: # a의 가장 작은 원소가 b의 가장 큰 원소보다 작다면, swap
		a[i],b[i] = b[i],a[i]
	else: # 그렇지 않다면, 즉 a의 가장 작은 원소가 b의 가장 큰 원소보다 크다면 a의 모든 원소는 b의 모든 원소보다 큼. 그럼 swap 필요 없음.
		break
		
print(sum(a))