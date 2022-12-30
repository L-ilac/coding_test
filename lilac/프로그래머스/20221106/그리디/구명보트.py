# 보트에는 최대 2명씩 밖에 탈 수 없다.
# 몸무게가 제한 무게의 1/2 초과인 사람들끼리는 같이 탈 수 없다. 그러므로 각 보트에 나누어져 배치되어야함.
# 몸무게가 제한 무게의 1/2 이하인 사람들은 각 나누어져 배치된 사람들 중 자신의 몸무게와 더했을때, 제한을 넘지 않는 사람과 같이 타야함.
# 조건을 만족하지 못하는 사람들은 그 사람들끼리 묶어서 새로운 보트에 배치해야함.
import math
import heapq


def solution(people, limit):
    answer = 0
    heavy = [person for person in people if person > limit/2]
    light = [person for person in people if person <= limit/2]

    heapq._heapify_max(heavy)
    heapq.heapify(light)

    if len(heavy) == 0:  # 가벼운 사람만 있을 때
        return math.ceil(len(light)/2)
    elif len(light) == 0:  # 무거운 사람만 있을 때
        return len(heavy)

    while heavy and light:  # 가벼운 사람이랑 무거운 사람이 섞여 있을 때
        tmp = heapq._heappop_max(heavy)  # 제일 무거운 사람 1명 pop
        if tmp + light[0] <= limit:  # 가장 가벼운 사람이 보트에 들어갈 수 있다면, 타면 되고, 못타면 나머지 사람들도 못탐
            heapq.heappop(light)

        # 만약 못타면, 무거운 사람은 혼자 보트 타는 거고, 가벼운 사람은 그 다음으로 무거운 사람과 탈 수 있는지 확인함
        answer += 1

    # 무거운 사람이 모두 다 빠졌다면, 나머지는 2명씩 그냥 짝지어서 타야함
    # 가벼운 사람이 모두 다 빠졌다면, 나머지는 1명씩밖에 못탐(전부 무거운 사람이기 때문에)
    answer += len(heavy)
    answer += math.ceil(len(light)/2)

    return answer


def solution2(people, limit):
    answer = 0
    people.sort()

    a = 0
    b = len(people) - 1
    while a < b:
        if people[b] + people[a] <= limit:
            a += 1
            answer += 1
        b -= 1
    return len(people) - answer
