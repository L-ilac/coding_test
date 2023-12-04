import sys


def who_wins(tmp):
    # . 이 승자가 될 수도 있음 ㅋㅋㅋㅋㅋㅋㅋㅋㅋ ㅅㅂ

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

    # ! 둘다 승리조건을 만족했을 경우 -> 한명이 완성하면 게임이 끝나기때문에 발생할수 없음
    if len(winner) == 2:
        print("invalid")
    # ! 한명만 승리조건을 만족했을 경우
    elif len(winner) == 1:
        # * 후공이 승리한 경우
        if winner.pop() == "O":
            if o_cnt == x_cnt:
                print("valid")
            else:
                print("invalid")
        # * 선공이 승리한 경우 (숫자가 같으면서 이길 수 없음)
        else:
            if o_cnt == x_cnt:
                print("invalid")
            else:
                print("valid")
    else:
        if x_cnt + o_cnt == 9:
            print("valid")
        else:
            print("invalid")
