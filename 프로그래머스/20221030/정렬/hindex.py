def solution(citations):
    answer = 0
    count = 0
    citations.sort()  # 모든 논문을 인용횟수를 기준으로 정렬(정렬안해도 돌아감)

    # h-index는 0(모든 논문이 0 일경우) ~ 최대 인용 횟수(최대 인용 횟수는 무조건 n이하) 중 1개일 것
    for i in range(citations[-1]+1):
        # i가 h -index의 조건을 만족하는가?
        for cited_num in citations:
            if i <= cited_num:  # i번이상 인용된 논문의 갯수 카운트
                count += 1

        if count >= i:  # i번 이상 인용된 논문의 갯수가 i개 이상이라면
            answer = i  # 현재까지 계산된 H-index
        else:  # 만약 조건을 만족하지 못하면, i번 이상 인용된 논문갯수가 i개 이상이 아니라는 말이므로 지금까지 계산된 값이 최대 h-index
            break

        count = 0  # 다음 계산을 위해 count 초기화

    return answer
