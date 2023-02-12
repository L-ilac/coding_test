import sys
n, c = map(int, input().split())

house = []

for _ in range(n):
    house.append(int(sys.stdin.readline().rstrip()))

house.sort()

# 가장 가까운 공유기 2개 사이의 거리를 기준으로 삼는다면,
start = 1
end = house[-1] - house[0]  # 공유기가 가질 수 있는 가장 큰 간격
# result = 0

while start <= end:
    mid = (start+end) // 2

    last_installed = 0  # 마지막으로 공유기가 설치된 위치
    installed = 1  # 현재까지 설치된 공유기 수

    # mid 라는 간격을 가지고 공유기를 몇개 설치할 수 있는지 검사
    for i in range(1, len(house)):
        if house[i] - house[last_installed] >= mid:
            installed += 1
            last_installed = i

    # 설치된 공유기가 c보다 작으면 간격이 너무 커서 설치 못한것. 간격을 줄여야함
    if installed < c:
        end = mid - 1
    # 설치된 공유기가 c보다 같거나 크면, 간격이 딱 맞거나 작아서 널널한것. 따라서 간격을 늘려도 됌
    else:
        result = mid  # 주어진 갯수만큼의 공유기를 설치 성공했으므로, 답이 될 수 있는 값임
        start = mid + 1


print(result)

# ! 어렵다. 힌트 안봤으면 못풀었을 듯. 가장 인접한 공유기 2개 사이의 거리를 기준으로 잡는데까지는 성공했는데,
# ! 이후에 그 거리를 줄여야하는가 늘려야하는가에 대한 판단을 해주는 방법을 떠올리지 못함.
# ! 가장 인접한 공유기 2개 사이의 거리를 가정했을 때, 실제로 주어진 집 좌표에 가정한 간격으로 공유기를 몇개 설치 할 수 있는가를 직접 검사하여 간격을 늘리지 말지 결정함.
