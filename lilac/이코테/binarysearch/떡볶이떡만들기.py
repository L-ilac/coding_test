n, m = map(int, input().split())

length = list(map(int, input().split()))


length.sort()

# 절단기 높이 0 ~ length[-1]
start = 0
end = length[-1]


while start <= end:
    mid = (start + end)//2  # 절단기 높이
    # print(mid)

    give = 0
    for i in length:
        give += i-mid if i > mid else 0

    if give < m:
        end = mid - 1
    else:
        start = mid + 1

print(end)

# ! 어떤 요소를 이진탐색의 기준으로 잡을 것인지 설정하는게 제일 어렵고, 머리를 많이 써야하는 부분.
