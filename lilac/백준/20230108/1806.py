# 10,000 이하의 자연수로 이루어진 길이 N짜리 수열이 주어진다.
# 이 수열에서 연속된 수들의 부분합 중에 그 합이 S 이상이 되는 것 중, 가장 짧은 것의 길이를 구하는 프로그램을 작성

# ! 수열의 최대 길이가 100000이기 때문에, 투포인터를 이용한 계산을 통해 시간복잡도를 최소화하는 것이 포인트
# * 접근법
# 1. 수열의 맨 처음 값을 부분합으로 설정한 뒤, 부분합이 s보다 큰지 작은지 검사한다.
# 2-1. 부분합이 s보다 작다면, 값을 늘려야하므로, right를 늘려서 값을 추가한다.
# 2-2. 부분합이 s보다 크다면, 값을 줄여야하므로, left를 늘려서 값을 빼준다.
# 3. 조건을 만족하는 가장 짧은 수열의 길이를 구해야하므로, right가 수열 총 길이에 도달할때까지 반복한다.


import sys
n, s = map(int, input().split())
series = list(map(int, sys.stdin.readline().split()))


left = 0
right = 0

# 가장 맨처음 부분합
partial_sum = series[left]
# 가장 짧은 수열의 길이를 저장하는 변수
shortest = sys.maxsize

# * right 포인터가 수열에 끝까지 도달할 때까지 반복문 수행
while right < n:

    # ! 부분합이 s이상이라면, 해당 수열의 길이를 shortest와 비교하여 갱신해주어야함
    if partial_sum >= s:
        shortest = min(shortest, right-left+1)

        # * 갱신 후에는 조건을 만족하는 다음 수열을 찾기 위해 수열의 가장 맨 앞 값을 뺴준다.
        partial_sum -= series[left]

        # * left 포인터 조정
        left += 1
    # ! 부분합이 s이하라면, right 포인터를 증가시켜 수열을 늘려주어야한다.
    else:
        right += 1
        # ! right 포인터를 늘렸는데 범위를 벗어날 경우, 조건을 만족하지 못하는 상태로 반복문 탈출
        if right >= n:
            break
        # * 범위를 벗어나지 않을 경우, 부분합에 수열에 마지막으로 추가된 값을 더해줌
        partial_sum += series[right]

# 만약 수열이 조건을 만족못해서 shortest를 갱신하지 못했다면, s를 만들 수 있는 수열이 존재하지 않는 것.
if shortest == sys.maxsize:
    print(0)
else:
    print(shortest)
