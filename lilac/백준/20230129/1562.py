# 길이가 10인 0~9를 모두 포함하는 계단수는 9876543210 밖에 없음.
# 9 87 과 98 7 의 경우 각 사이에 넣는 케이스가 겹치는 경우가 있다
# 0과 9는 각 경계선이라 한가지 방향으로 밖에 못감
# ! 이해했음 다시 풀것.

n = int(input())

dp = [] * n
