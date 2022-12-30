n, m, k = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()

total = 0
total += arr[-1]*(m-(m//k)) + arr[-2] * (m//k)
print(total)
