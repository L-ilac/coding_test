def solution(num):
    start = 1 # 시작
    cal = 1 # 계산 되어지는 값
    count = 1 # 계속 늘어나는 값

    if num == start: # 초기값이랑 입력받아온 값이랑 같으면
        print(count) # 출력
        return # 멈추기
    # 아니라면
    while True: # 멈추기 전까지
        cal += count * 6 # 계산 되어지는 값에 6씩 곱해지는 값을 더해줌
        count += 1 # 갯수 카운트
        if num <= cal: # 범위 안에 들면
            print(count) # 갯수 출력
            break # 후에 멈추기

N = int(input())
solution(N)
