s = input()
t = input()

# 이거도 거꾸로 생각합시다
tmp = []
tmp.append(t)

flag = False

while tmp:

    now = tmp.pop(0)

    if now == s:
        flag = True
        break

    # ! 이전에 풀었던 문제와 다르게, 경우의 수가 2개가 나올 수 있는 케이스가 있음.
    if now[0] == 'B':
        tmp.append(now[::-1][:-1])

    if now[-1] == 'A':
        tmp.append(now[:-1])


if flag:
    print(1)
else:
    print(0)
