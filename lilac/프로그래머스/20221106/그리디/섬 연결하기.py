# 연결해야하는 섬을 갖고 있는 다리중에 가장 저렴한걸 고른다.
# 1. 초기에는 가장 싼 값의 다리를 추가
# 2. 연결된 섬들중 1개, 연결되지 않은 섬들중 1개를 포함하는 다리들중 가장 싼 것을 고르기
# 3. 선택된 다리를 연결하는 섬을 제외한 후 2~3번 과정 반복
def solution(n, costs):
    answer = 0
    unconnected = set(list(range(0, n)))  # 연결되지 않은 섬의 목록
    costs.sort(key=lambda x: x[2])

    # 맨 처음에는 가장 저렴한 다리를 선택
    cheapest = costs[0]

    # 선택된 섬들은 다리에 의해 연결 되었음.
    unconnected.discard(cheapest[0])
    unconnected.discard(cheapest[1])

    # 다리 건설 비용 추가
    answer += cheapest[2]

    # 모든 섬들이 연결될 때까지 다리를 건설한다.
    while unconnected:
        # 이미 연결된 섬들중 1개, 연결 안된 섬들중 1개를 연결하는 다리중에 가장 저렴한 다리를 골라야함.
        for bridge in costs:
            if any(i in unconnected for i in bridge[:2]) and any(i not in unconnected for i in bridge[:2]):
                unconnected.discard(bridge[0])
                unconnected.discard(bridge[1])
                answer += bridge[2]
                break

    return answer
