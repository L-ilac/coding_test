# 어쨌든 최단 경로이므로 오른쪽, 밑으로만 움직여야하며, 오른쪽으로 m-1번, 밑으로 n-1번 움직여야함.
# 출발지점으로부터 모든 칸에 대해 최단거리를 업데이트하면서 도착지점까지 간다.
# m -> x좌표 n-> y좌표 (x,y) -> map[y][x]
def solution(m, n, puddles):
    dp_map = [[1] * m for _ in range(n)]

    for p in puddles:  # 웅덩이 길 설정
        if p[1] == 1:  # (?,1) 이 웅덩이라면, ? 이후 모든 값들을 0으로 처리해줘야함
            for i in range(p[0]-1, m):
                dp_map[0][i] = 0
            continue

        if p[0] == 1:  # (1,?) 이 웅덩이라면, ? 이후 모든 값들을 0으로 처리
            for i in range(p[1]-1, n):
                dp_map[i][0] = 0
            continue

        dp_map[p[1]-1][p[0]-1] = 0

    # 경계선 상은 제외하고 보는게 맞음. y=1, x=1 빼고 업데이트
    for i in range(1, n):
        for j in range(1, m):
            if dp_map[i][j] != 0:
                dp_map[i][j] = (dp_map[i-1][j] + dp_map[i][j-1]) % 1000000007

    # 나머지 연산의 위치에 대한 문제...?
    answer = dp_map[n-1][m-1] % 1000000007
    return answer
