def solution(n, lost, reserve):
    answer = 0
    lost.sort()
    reserve.sort()

    # 모든 잃어버린 학생들은 자기 앞번호 뒷번호 둘 다 예비가 있으면 무조건 앞번호 것을 빌린다.
    # 자기가 잃어버리고 자기 예비 체육복을 입어야하는 경우를 선처리 해줘야함
    # 1(reserve) 2(lost) 3(reserve) 4(reserve,lost) 5(lost) -> 4번이 3번꺼 빌리면, 5번이 4번꺼 빌릴수 있는데?
    for i in range(1, n+1):
        if i in lost and i in reserve:  # 자기가 잃어버리고 자기 예비를 입어야하는 경우
            lost.remove(i)
            reserve.remove(i)

    for i in lost[:]:
        tmps = [i-1, i+1]

        if all(tmp in reserve for tmp in tmps):  # 앞뒤로 예비 있으면 앞번호꺼 빌리기
            lost.remove(i)
            reserve.remove(i-1)
        else:
            if tmps[0] in reserve:
                lost.remove(i)
                reserve.remove(tmps[0])
            elif tmps[1] in reserve:
                lost.remove(i)
                reserve.remove(tmps[1])
            else:
                pass

    answer = n-len(lost)

    return answer
