from collections import deque

gears = []

for _ in range(4):
    gears.append(deque(list(map(int, input()))))

# 톱니가 N극이라면 0, S극이라면 1,
# 2번 인덱스 -> 3시 방향 톱니, 6번 인덱스 ->9시방향 톱니
# deque.rotate(1) : 시계 방향 1칸 회전 ,  deque.rotate(-1) :  반시계 방향 1칸 회전


k = int(input())

for _ in range(k):
    gear_num, dir = map(int, input().split())
    gear_num -= 1

    # 돌릴 톱니바퀴 기준 오른쪽 방향에 있는 톱니바퀴들이 회전해야하는지 판단
    r_rotation = []
    for i in range(gear_num, 3):
        if gears[i][2] != gears[i+1][6]:
            r_rotation.append((i+1, dir * ((-1)**(i+1-gear_num)))
                              )  # (톱니바퀴 번호, 회전 방향)
        else:
            break

    # 돌릴 톱니바퀴 기준 왼쪽 방향에 있는 톱니바퀴들이 회전해야하는지 판단
    l_rotation = []
    for i in range(gear_num, 0, -1):
        if gears[i][6] != gears[i-1][2]:
            l_rotation.append((i-1, dir * (-1)**(gear_num-(i-1)))
                              )  # (톱니바퀴 번호, 회전 방향)
        else:
            break

    gears[gear_num].rotate(dir)

    for i, d in r_rotation:
        gears[i].rotate(d)

    for i, d in l_rotation:
        gears[i].rotate(d)

answer = 0

if gears[0][0] == 1:
    answer += 1

if gears[1][0] == 1:
    answer += 2

if gears[2][0] == 1:
    answer += 4

if gears[3][0] == 1:
    answer += 8

print(answer)
