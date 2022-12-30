n, k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

count = 0
max_sum = 0
c = a+b

a = sorted(a, reverse= True)
c = sorted(c, reverse= True)

for i in c:
	if i in a:
		max_sum += i
		a.remove(i)
		continue
	else:
		max_sum += i
		a.pop()
		count += 1
	
	if count == k or not a:
		break

for i in range(len(a)):
	max_sum += a[i]

print(max_sum)