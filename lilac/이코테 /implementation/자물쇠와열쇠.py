
#! 이게 어떻게 프로그래머스 레벨 3이야...
def rotate(key):
    n = len(key)  # 행
    m = len(key[0])  # 열
    new_key = [[0]*n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            new_key[j][n-1-i] = key[i][j]

    return new_key


def check(new_lock, size):
    for i in range(size, size*2):
        for j in range(size, size*2):
            if new_lock[i][j] != 1:
                return False
    return True


def solution(key, lock):
    answer = True

    # 열쇠를 돌리거나 움직여서 나올 수 있는 경우의 수를 구한다.
    # 실제 자물쇠에 낀다

    m = len(key)
    n = len(lock)

    new_lock = [[0]*(n*3) for _ in range(n*3)]

    for i in range(n):
        for j in range(n):
            new_lock[n+i][n+j] = lock[i][j]

    for _ in range(4):
        key = rotate(key)

        for x in range(n-m+1, n*2):
            for y in range(n-m+1, n*2):
                # 확장된 자물쇠 기준 (n-m+1,n-m+1) 부터 (2n-1,2n-1) 를 출발점으로 m*m 키 행렬을 더해보면 됌
                for a in range(m):
                    for b in range(m):
                        new_lock[x+a][y+b] += key[a][b]

                # 자물쇠 영역이 전부 1로 채워져 있는가? (맞는 열쇠가 존재)
                if check(new_lock, n):
                    return True

                for a in range(m):
                    for b in range(m):
                        new_lock[x+a][y+b] -= key[a][b]

    return False
