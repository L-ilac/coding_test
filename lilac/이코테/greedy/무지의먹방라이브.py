import heapq


def solution(food_times, k):
    answer = 0
    q = []
    # 1초에 음식은 1만큼만 먹을 수 있다.

    # 음식의 총 양이 시간보다 작거나 같으면 장애가 발생하기 전에 음식을 다 먹는다.
    if sum(food_times) <= k:
        return -1

    # 음식 순서가 작은 순서대로 힙에 삽입
    for idx, food in enumerate(food_times, start=1):
        heapq.heappush(q, (food, idx))

    # 여기부터는 주어진 k초 안에 음식을 전부 먹을 수 없는 경우(return -1 아님)

    # 바로 직전에 다 먹어치운 음식의 총량
    previous = 0
    while True:
        # 가장 적게 남은 음식
        smallest_food = heapq.heappop(q)

        # 가장 적게 남은 음식을 전부 먹으려면 걸리는 최소한의 시간
        # ! previous -> 1번째로 적게 남은 음식을 먹을때, 1번째로 적게 남은 음식의 양만큼 나머지 음식들의 양에서도 전부 뺴줘야하기 때문에
        consuming_time = (smallest_food[0]-previous) * (len(q)+1)

        # 가장 적게 남은 음식을 다 먹어도 시간이 남는다면
        if consuming_time < k:
            k -= consuming_time
            previous = smallest_food[0]
            continue
        # 가장 적게 남은 음식을 다 먹을만큼의 시간이 안남는다면
        else:
            heapq.heappush(q, smallest_food)
            break

    # 남은 음식들에 대하여 인덱스 순으로 정렬
    q.sort(key=lambda x: x[1])

    return q[k % len(q)][1]
