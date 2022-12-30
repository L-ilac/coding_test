def solution(triangle):
    answer = 0

    # 삼각형을 모두 훑으면서 경로상 나올 수 있는 최대값으로 계속 업데이트 하면됌.
    # 1. 왼쪽 대각선 위만 있는 경우 -> n째 줄 m번째 = n-1번째 줄 m-1번째 요소 -> 가장 오른쪽에 있는 요소가 이에 해당
    # 2. 오른쪽 대각선 위만 있는 경우 -> n째 줄 m번째 = n-1번째 줄 m번째 요소 -> 가장 왼쪽에 있는 요소가 이에 해당
    # 3. 양쪽 대각선 위 둘다 있는 경우 -> max(1번, 2번)
    for i in range(len(triangle)):
        for j in range(len(triangle[i])):
            if i == 0:
                break
            else:
                if j == 0:
                    triangle[i][j] += triangle[i-1][j]
                elif j == len(triangle[i])-1:
                    triangle[i][j] += triangle[i-1][j-1]
                else:
                    triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])

    answer = max(triangle[-1])
    return answer
