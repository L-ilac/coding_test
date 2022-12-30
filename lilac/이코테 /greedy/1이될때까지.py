n, k = map(int, input().split())

cnt = 0


while n >= k:
    cnt += n % k
    n -= n % k
    n //= k
    cnt += 1

cnt += n-1

print(cnt)
