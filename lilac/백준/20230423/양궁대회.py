from itertools import combinations_with_replacement


def can_win(lion_info, apeach_info):
    apeach = 0
    lion = 0

    for i in range(11):
        if lion_info[i] > apeach_info[i]:
            lion += 10-i
        elif lion_info[i] == apeach_info[i] and lion_info[i] == 0:
            continue
        else:
            apeach += 10-i

    if lion > apeach:
        return lion - apeach
    else:
        return False


def solution(n, info):

    a = list(combinations_with_replacement(
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], n))
    answer = None

    score_gap = 0

    for case in a:
        # 라이언이 case에 해당하는 화살들을 쐈다고 가정
        # 라이언이 쏜 화살을 info 형태로 tmp에 저장
        tmp = [0] * 11

        for c in case:
            tmp[10-c] += 1

        is_win = can_win(tmp, info)

        # 라이언이 승리할 수 있는 경우
        if is_win:
            if is_win > score_gap:
                answer = tmp
                score_gap = is_win
            elif is_win == score_gap:
                tmp.reverse()
                answer.reverse()

                answer = max(tmp, answer)
                answer.reverse()

    if answer == None:
        return [-1]
    else:
        return answer
