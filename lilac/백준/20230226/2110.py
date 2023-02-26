import sys
n, c = map(int, input().split())

house = []
for _ in range(n):
    house.append(int(sys.stdin.readline().rstrip()))

house.sort()

left = 0
right = house[-1] - house[0]  # ! gap의 크기를 기준으로 이분 탐색

answer = 0
while left <= right:
    mid = (left+right) // 2

    # 몇 개의 공유기를 설치할 수 있는지 조사
    installed = 1  # (맨 첫 집에는 무조건 설치)
    last_installed = 0  # 인덱스 저장

    for i in range(1, n):
        distance = house[i] - house[last_installed]

        if distance >= mid:
            last_installed = i
            installed += 1

    # print(mid, installed)

    if installed >= c:
        left = mid + 1
        answer = mid
    else:
        right = mid - 1


# 1 2 4 8 9

print(answer)
