import heapq


def solution(operations):
    answer = []
    queue = []

    for op in operations:
        # 주어진 명령어 파싱
        command = op.split()[0]
        number = int(op.split()[1])

        if command == 'I':
            queue.append(number)
        else:
            if queue:
                if number > 0:
                    queue.pop()  # 최대값
                    pass
                else:
                    queue.pop(0)  # 최소값
            else:  # 큐에 아무것도 없으면 연산을 무시함
                continue

        queue.sort()
    if queue:
        answer.append(queue[-1])  # 최대값
        answer.append(queue[0])  # 최소값
    else:
        answer = [0, 0]

    return answer
