from collections import deque

n, k = map(int, input().split())

a = list(map(int, input().split()))

robots = []  # 로봇이 위치한 인덱스를 삽입

time = 1

# 초기 올리는 위치, 내리는 위치
inpos = 0
outpos = n-1

while True:

    # 1 회전
    inpos = (inpos - 1) % (2*n)
    outpos = (inpos + n-1) % (2*n)

    # 회전한 직후, 내리는 위치에 로봇이 있을 경우
    if robots and outpos in robots:
        robots.remove(outpos)

    # 2 가장 먼저 벨트에 올라간 로봇부터 -> 제일 앞에 있는 로봇이 가장 먼저들어온 로봇임
    for i in range(len(robots)):
        # 로봇이 이동할 다음 위치
        nextpos = (robots[i]+1) % (2*n)

        if nextpos not in robots and a[nextpos] >= 1:
            a[nextpos] -= 1
            robots[i] = nextpos

    if outpos in robots:
        robots.remove(outpos)

    # 3 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
    if a[inpos] > 0:
        a[inpos] -= 1
        robots.append(inpos)

    if a.count(0) >= k:
        break

    time += 1

print(time)


# ! deque().rotate 를 이용한 풀이


n, k = map(int, input().split())

a = deque(list(map(int, input().split())))

robot = deque([False]*n)  # 0~n-1 까지의 컨베이어 벨트에 로봇이 있는지 없는지를 나타내는 덱

time = 1


while True:
    # 1. 컨베이어벨트 회전

    a.rotate(1)  # 컨베이어 벨트는 길이가 2n
    robot.rotate(1)  # 로봇이 올려질 수 있는 부분은 컨베이어벨트에서 n만큼

    # 컨베이어 벨트가 회전했을 때, 내리는 위치에 있는 로봇은 내려야한다.
    robot[-1] = False

    # 내리는 위치를 제외한 로봇이 있을 수 있는 모든 칸에 대해 로봇이 다음 칸으로 움직일 수 있는지 판단
    for i in range(n-2, -1, -1):
        # i 위치에 로봇이 있다면, 다음칸으로 움직여야함
        if robot[i] and not robot[i+1] and a[i+1] >= 1:
            a[i+1] -= 1
            robot[i+1] = True
            robot[i] = False

    # 모든 로봇들이 움직인 후에, 내리는 위치에 있는 로봇은 내려야함
    robot[-1] = False

    # 3. 올리는 위치에 로봇이 올라갈 수 있다면 올려야함.

    if a[0] > 0:
        a[0] -= 1
        robot[0] = True

    # print(robot)

    # 4. 내구도가 0인 칸이 k개 이상이라면?

    if a.count(0) >= k:
        break

    time += 1

print(time)
