def solution(priorities, location):
    answer = 0
    print_list = []  # 인쇄가 완료된 문서 넣는 리스트
    a = []  # priorities를 (priority, isTarget)의 형태로 사용하기 위해 만든 리스트

    # a 만들기 -> a = [(index, priority) for index, priority in enumerate(priorities)] 로 더 간단하게 가능

    for i in range(len(priorities)):  # target일 경우 1, 나머지는 0으로 set
        if i == location:
            a.append((priorities[i], 1))
        else:
            a.append((priorities[i], 0))

    while a:
        tmp = a.pop(0)

        if tmp[0] >= max(priorities):  # 이게 가장 큰 우선순위를 갖고 있다면?
            print_list.append(tmp)  # 출력
            priorities.remove(tmp[0])  # 출력한 우선순위에 해당하는 요소 1개 제거
            if tmp[1] == 1:
                break  # 출력한 데이터가 target이라면 반복문 탈출

        else:
            a.append(tmp)  # 우선순위가 낮다면 맨뒤로

    return len(print_list)  # 반복문을 탈출시 가장 뒤에 있는 자료가 target이므로 리스트 길이가 곧 인쇄된 순서

# location의 값을 직접 1씩 앞으로 당기면서 계산하는 방식도 가능함.(맨앞에서는 len(list)-1 를 이용해 맨뒤로)
# if any(cur[1] < q[1] for q in queue): queue 안의 모든 요소에 대해 아무거나 조건을 만족하면 true
