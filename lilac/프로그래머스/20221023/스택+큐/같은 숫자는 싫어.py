def solution(arr):
    answer = []
    sp = -1  # answer의 갯수를 체크하기 위한 포인터

    for num in arr:
        tmp = num  # arr의 가장 앞 원소, # pop 연산 쓰면 실행시간이 증가하는듯

        if not answer:  # answer이 비어있다면 그냥 추가
            pass

        # sp 와 len(answer) 의 성능차이도 존재, len(answer) 사용시 시간 증가
        elif answer[sp] == tmp:  # 비어있지않다면, answer의 가장 마지막 값과 tmp 비교
            continue

        answer.append(tmp)  # 겹치지 않는 값 answer에 추가
        sp += 1  # 원소 1개 추가되었으므로 +1

    return answer
