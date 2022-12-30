import math


def solution(brown, yellow):
    answer = []

    total = brown + yellow  # 총 격자의 갯수

    # 카펫 가로 >= 카펫 세로
    for i in range(3, int(math.sqrt(total))+1):  # 세로 길이는 최소 3이상 sqrt(total) 이하
        if total % i != 0:  # 가능한 길이 조합 찾기 (가로,세로 둘다 자연수여야하므로)
            continue

        vertical = i  # 세로
        horizontal = int(total/i)  # 가로

        # xy = yellow + brown = (x-2)(y-2) + brown
        if brown + 4 == 2*(vertical+horizontal):
            return [horizontal, vertical]
