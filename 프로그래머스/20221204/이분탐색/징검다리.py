# 주어진 조건에서 나올 수 있는 가장 먼 간격은 0 ~ distance(시작 ~ 끝) 이다.
# 제거해야하는 바위는 n개 이고, 바위를 제거함에 따라 간격의 값이 달라진다.
# 문제의 조건을 만족하기 위해서, 간격의 최솟값이 존재할 수 있는 범위를 절반씩 줄여가며, 해당 값이 최솟값을 만족할 수 있는 값인지를 검사해야한다.
# 만약 최솟값이 x라면, 0부터 시작해서 distance까지 순차적으로 각 바위를 들리면서, 간격이 모두 x를 넘을 수 있도록 바위를 제거하거나 유지시킨 뒤, 제거한 바위의 수가 주어진 조건에 맞는 갯수 인지를 체크한다.
# 바위를 제거하면 간격은 무조건 커진다. 즉, 바위를 주어진 조건보다 많이 제거해야한다는 것은 x 가 실제 최솟값보다 작기 때문이고, 바위를 조건보다 적게 제거했다는 것은, x가 실제 최솟값 보다 크기 때문이다.
# 그러므로 만약 제거한 바위수가 조건보다 작다면, x보다 큰 범위에서 최솟값을 다시 찾아야하고, 제거한 바위수가 조건보다 크다면, x보다 작은 범위에서 최솟값을 다시 찾아야한다.

def solution(distance, rocks, n):
    low = 0
    high = distance
    intervals = []

    rocks.append(0)
    rocks.append(distance)
    rocks.sort()  # 바위의 위치 정렬

    # 간격 구하기
    for i in range(len(rocks)-1):
        intervals.append(rocks[i+1]-rocks[i])

    while low <= high:
        mid = (low + high) // 2

        # 만약 mid 가 최솟값이라면, 모든 간격은 mid보다 크거나 같아야한다.
        # 0부터 시작해서, 각 바위를 접근하면서 간격이 mid보다 크거나 같은지 확인한다.
        # 누적된 간격이 mid를 넘을 때까지 바위를 제거하면서 간격을 누적시킨다.

        gap = 0
        removed = 0  # 제거된 바위의 갯수를 세야함
        min_gap = 0

        for i in intervals:  # 마지막 바위는 삭제할수 없음.
            gap += i

            if gap < mid:  # 간격이 mid 보다 작다면
                removed += 1  # 바위를 한개 제거
                continue
            else:  # 간격이 mid 보다 크거나 같다면
                if min_gap == 0:
                    min_gap = gap
                else:
                    min_gap = min(min_gap, gap)
                gap = 0  # 새롭게 간격을 측정하기 위해 초기화

        if removed > n:  # 제거된 바위가 조건보다 크다면, 너무 많이 제거한 것이므로, 현재 mid값이 최솟값보다 크다는 것
            high = mid-1
        else:  # 딱 n개 맞춰서 제거하는 경우와 n개 이하 갯수만큼 제거하는 경우가 동일하다.(질문하기 - 해설 내용 볼 것)
            answer = min_gap
            low = mid+1

    return answer
