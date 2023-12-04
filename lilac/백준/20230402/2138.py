n = int(input())

now = list(map(int, list(input())))
want = list(map(int, list(input())))

# 같은 스위치를 여러번 누르는 것은 의미가 없다. -> N개의 스위치가 있으니까 N이하

tmp = now[:]
turn_on_1 = 0

# 0번째 스위치가 눌린 경우
turn_on_1 += 1
tmp[0] = abs(tmp[0]-1)
tmp[1] = abs(tmp[1]-1)


for i in range(1, n):
    if tmp[i-1] != want[i-1]:
        turn_on_1 += 1
        tmp[i-1] = abs(tmp[i-1]-1)
        tmp[i] = abs(tmp[i]-1)

        if i != n-1:
            tmp[i+1] = abs(tmp[i+1]-1)

if tmp[-1] != want[-1]:
    turn_on_1 = -1

#########################################

tmp = now[:]
turn_on_2 = 0
# 0번째 스위치가 안눌린 경우

for i in range(1, n):
    if tmp[i-1] != want[i-1]:
        turn_on_2 += 1
        tmp[i-1] = abs(tmp[i-1]-1)
        tmp[i] = abs(tmp[i]-1)

        if i != n-1:
            tmp[i+1] = abs(tmp[i+1]-1)

if tmp[-1] != want[-1]:
    turn_on_2 = -1

if turn_on_1 == -1 and turn_on_2 == -1:
    print(-1)
else:
    if min(turn_on_1, turn_on_2) == -1:
        print(max(turn_on_1, turn_on_2))
    else:
        print(min(turn_on_1, turn_on_2))
