from collections import deque


def solution(number, k):
    # 모든 자리에 대하여 자기보다 최초로 큰 숫자가 몇자리 뒤에 나오는지 카운트하고, 그 카운트가 k보다 작다면 삭제한다.
    answer = ''
    num = deque(list(number))
    cnt = 1

    while k > 0:
        cnt = 1
        tmp = num.popleft()

        if int(tmp) == 9:
            answer += tmp
            continue

        for i in num:  # 시간 제일 많이 잡아먹는 부분.
            if int(tmp) < int(i):
                break
            cnt += 1

        if cnt <= k:
            k -= 1
            continue

        answer += tmp

    answer += ''.join(num)  # 남은 문자열들은 전부 붙여줘야함.

    return answer
