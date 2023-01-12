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

    if now[0] == 'B':
        tmp.append(now[::-1][:-1])

    if now[-1] == 'A':
        tmp.append(now[:-1])


if flag:
    print(1)
else:
    print(0)
