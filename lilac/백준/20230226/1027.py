import sys

n = int(input())

buildings = list(map(int, input().split()))


result = 0
# ! 한 빌딩을 기준으로 양쪽 방향으로 탐색한다.
for i in range(n):
    can_see = 0

    tmp_height = buildings[i]
    delta_right = -sys.maxsize
    delta_left = sys.maxsize

    for j in range(i-1, -1, -1):
        left = buildings[j]
        tmp_delta = (tmp_height - left) / (i-j)

        if tmp_delta < delta_left:
            delta_left = tmp_delta
            can_see += 1

    for j in range(i+1, n):
        right = buildings[j]
        tmp_delta = (right - tmp_height) / (j-i)

        if tmp_delta > delta_right:
            delta_right = tmp_delta
            can_see += 1

    print(can_see)
    result = max(result, can_see)


print(result)
