n = int(input())

house = list(map(int, input().split()))
house.sort()

# 집 개수가 짝수라면
if n % 2 == 0:
    print(house[(n//2)-1])
else:
    print(house[n//2])
