n = int(input())
a = []

for _ in range(n):
	a.append(int(input()))


# a.sort(reverse=True)
a = sorted(a,reverse = True)

print(a)