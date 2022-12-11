import math


def solution(arr):
    operator = []
    operand = []
    INF = math.inf

    for c in arr:
        if c.isdecimal():
            operand.append(int(c))
        else:
            operator.append(c)

    m = len(operand)
    max_dp = [[-INF] * m for _ in range(m)]
    min_dp = [[INF] * m for _ in range(m)]

    for i in range(m):  # 초기 dp 설정
        max_dp[i][i] = operand[i]
        min_dp[i][i] = operand[i]

    for gap in range(1, m):  # i와 j의 간격
        for i in range(0, m-gap):
            j = i + gap
            for k in range(i, j):  # operand 의 i번째 숫자에서 j번째 숫자까지의 계산
                if operator[k] == '+':  # k-1번째 숫자 뒤의 연산자가 + 일때
                    max_dp[i][j] = max(
                        max_dp[i][j], max_dp[i][k] + max_dp[k+1][j])
                    min_dp[i][j] = min(
                        min_dp[i][j], min_dp[i][k] + min_dp[k+1][j])
                else:  # k-1번째 숫자 뒤의 연산자가 - 일때
                    max_dp[i][j] = max(
                        max_dp[i][j], max_dp[i][k] - min_dp[k+1][j])
                    min_dp[i][j] = min(
                        min_dp[i][j], min_dp[i][k] - max_dp[k+1][j])

    return max_dp[0][m-1]
