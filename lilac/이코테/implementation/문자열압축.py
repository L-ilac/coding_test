from collections import deque


def solution(s):
    answer = len(s)

    for i in range(1, (len(s)//2) + 1):
        tmp_s = s[:]
        tmp = []

        while True:
            if len(tmp_s) > i:
                tmp.append(tmp_s[0:i])
                tmp_s = tmp_s[i:]
            else:
                break

        tmp.append(tmp_s)

        # 단위로 문자열은 잘랐음.

        i, j = 0, 1
        cnt = 1
        result = 0

        while True:
            if tmp[i] == tmp[j]:
                cnt += 1
                j += 1
            else:
                if cnt > 1:
                    result += len(str(cnt))
                result += len(tmp[i])

                i = j
                j = i+1
                cnt = 1

            if j == len(tmp):
                if cnt > 1:
                    result += len(str(cnt))
                result += len(tmp[i])
                break

        answer = min(answer, result)

    print(answer)


solution("aabbaccc")


def solution2(s):
    answer = len(s)

    # 1. 문자열을 1,2,3,.... 문자열 전체 길이/2 단위로 자르는 경우에 대해서 전부 검사해야함
    # 2. 각각 자른 문자열을 기준으로, 반복되는 문자열을 체크하여, 새로운 압축된 문자열을 만든다.
    # 3. 새로 만든 문자열의 길이를 최솟값과 비교하여 더 작을 경우 갱신한다.

    for step in range(1, (len(s)//2) + 1):

        splited = deque()
        for i in range(0, len(s), step):  # ! for문 range(start, end+1, step)
            splited.append(s[:][i:i+step])

        previous = splited.popleft()
        cnt = 1
        compressed = ''

        while splited:
            now = splited.popleft()

            if previous == now:
                cnt += 1
            else:
                if cnt > 1:
                    compressed += str(cnt) + previous
                else:
                    compressed += previous

                # 위의 조건문을 한줄로 작성하는 법
                #compressed += str(cnt) + previous if cnt > 1 else previous

                cnt = 1
                previous = now

        if cnt > 1:
            compressed += str(cnt) + previous
        else:
            compressed += previous
        #compressed += str(cnt) + previous if cnt > 1 else previous

        answer = min(answer, len(compressed))

    print(answer)


solution2("aabbaccc")
