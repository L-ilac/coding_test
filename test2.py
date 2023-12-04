import sys


def who_wins(tmp):

    winner = set()

    for i in range(3):
        if tmp[i][0] == tmp[i][1] == tmp[i][2] and tmp[i][0] != '.':
            winner.add(tmp[i][0])

        if tmp[0][i] == tmp[1][i] == tmp[2][i] and tmp[0][i] != '.':
            winner.add(tmp[0][i])

    if tmp[0][0] == tmp[1][1] == tmp[2][2] and tmp[1][1] != '.':
        winner.add(tmp[1][1])

    if tmp[0][2] == tmp[1][1] == tmp[2][0] and tmp[1][1] != '.':
        winner.add(tmp[1][1])

    return winner


while True:
    a = sys.stdin.readline().rstrip()

    if a == "end":
        break

    tmp = list(a)

    o_cnt = tmp.count("O")
    x_cnt = tmp.count("X")

    # ! 갯수가 이상한 케이스는 여기서 전부 거르기
    if not (1 >= x_cnt-o_cnt >= 0):
        print("invalid")
        continue

    tmp = [tmp[:3], tmp[3:6], tmp[6:]]

    winner = who_wins(tmp)

    print(winner)