# 1. 교집합 형태의 지점 -> 교집합 부분으로 축소
# 2. 아예 겹치지 않는 형태의 지점 -> 독립된 부분으로 추가
# 3. 부분집합 형태의 지점 -> 부분집합 부분으로 축소

# 연속적이지 않은 구간 갯수를 센다.
def solution(routes):
    answer = 0
    for route in routes:  # [2, -1] -> 같이 진입 > 진출 인 경우, 전부 뒤집어서 생각한다.
        route.sort()

    routes.sort(key=lambda x: x[0])  # 모든 경로는 이제 진입 지점에 대해 오름차순으로 정렬됌.
    camsection = [-30000, 30000]

    for route in routes:
        # [진입, 진출] 이라고 생각했을때, 이전 진출 < 현재 진입 일 경우, 카메라 갯수 +1 하고, [현재 진입 , 현재 진출] 로 업데이트
        if camsection[1] < route[0]:
            answer += 1
            camsection[0], camsection[1] = route[0], route[1]
            continue

        camsection[0] = max(camsection[0], route[0])
        camsection[1] = min(camsection[1], route[1])

    answer += 1  # 모든 route를 전부 검사한 후, 마지막에 남겨진 camsection에 대한 카메라가 1개 필요함.

    return answer
