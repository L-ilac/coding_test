def solution(bridge_length, weight, truck_weights):
    answer = 0
    queue = [0] * bridge_length

    for truck in truck_weights:
        if sum(queue) + truck <= weight:
            queue.pop(0)
            queue.append(truck)
            answer += 1
        else:
            while True:
                queue.pop(0)
                if sum(queue) + truck <= weight:
                    queue.append(truck)
                    answer += 1
                    break
                else:
                    queue.append(0)
                    answer += 1

    answer += bridge_length

    return answer
