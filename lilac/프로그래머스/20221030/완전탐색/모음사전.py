import itertools


def solution(word):
    answer = 0
    alphabet = ['A', 'E', 'I', 'O', 'U']
    case = []
    for i in range(1, 6):
        case.extend(''.join(i)
                    for i in list(itertools.product(alphabet, repeat=i)))
       # 중복순열을 이용하여 가능한 모든 경우의 수를 만든다.

    case.sort()  # 문자열의 경우 사전순으로 정렬

    for c in case:  # 입력된 단어가 몇번째 단어인지 찾는 반복문
        answer += 1
        if c == word:
            break

    return answer

    # return case.index(word)+1 # 1줄로 끝내는법


# 수학적 접근?
# def solution(word):
#     answer = 0
#     for i, n in enumerate(word):
#         answer += (5 ** (5 - i) - 1) / (5 - 1) * "AEIOU".index(n) + 1
#     return answer
