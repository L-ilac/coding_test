def solution(N, stages):
    answer = []
    result = []

    # ! 실패율 계산 -> clear와 reach로 단순한 덧셈/뺼셈연산을 통해 실패율을 계산해야만 시간초과가 안나옴.
    for i in range(1, N+1):
        clear = 0
        reach = 0
        for user in stages:
            if user >= i:
                reach += 1
            if user > i:
                clear += 1

        if reach == 0:
            result.append((0, i))
            continue

        result.append(((reach-clear)/reach, i))

    result.sort(key=lambda x: -x[0])

    answer = [i[1] for i in result]

    return answer
