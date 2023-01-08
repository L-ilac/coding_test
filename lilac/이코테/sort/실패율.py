def solution(N, stages):
    answer = []
    result = []

    # 실패율 계산
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
