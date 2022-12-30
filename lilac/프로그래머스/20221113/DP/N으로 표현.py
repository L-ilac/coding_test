# dp 테이블에 N을 각각 1번,2번...8번(최대) 나올 수 있는 결과값을 저장한다.
# 1번 : N
# 2번 : 1번에 있는 요소와 사칙연산을 이용해 만들 수 있는 모든 경우의 수 -> 2N, 0 , 1 , N^2, 11N(NN)
# 3번 : 1번,2번 섞어서 경우의 수 만들기 -> N + (2N,0,1,N^2), N - (2N,0,1,N^2), N * (2N,0,1,N^2) , N /(2N,0,1,N^2)
# 곱하기, 더하기는 교환법칙 성립해서 상관 없는데, 빼기, 나누기는 교환법칙이 성립안해서 순서 바꾼 것도 생각해야함. (1번 요소 - 2번 요소) != (2번 요소 - 1번 요소)

def solution(N, number):
    answer = 0
    dp_table = [[], [N], [], [], [], [], [], [], []]
    cnt = 2
    if N == number:
        return 1

    while cnt < 9:
        for i in range(1, int(cnt/2)+1):
            for num1 in dp_table[i]:
                for num2 in dp_table[cnt-i]:
                    dp_table[cnt].append(num1 + num2)
                    dp_table[cnt].append(num1 * num2)
                    if num1 - num2 >= 0:
                        dp_table[cnt].append(num1 - num2)
                    if num2 - num1 >= 0:
                        dp_table[cnt].append(num2 - num1)
                    if num2 != 0:
                        dp_table[cnt].append(int(num1 // num2))
                    if num1 != 0:
                        dp_table[cnt].append(int(num2 // num1))
        dp_table[cnt].append(int("1"*(cnt))*N)
        dp_table[cnt] = list(set(dp_table[cnt]))

        if number in dp_table[cnt]:
            return cnt

        cnt += 1

    return -1
