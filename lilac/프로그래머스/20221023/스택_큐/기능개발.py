import math


def solution(progresses, speeds):
    answer = []
    deploy = [int(math.ceil((100-i)/j)) for i, j in zip(progresses, speeds)]
    # 작업당 배포까지 걸리는 일 수 계산, math.ceil을 써서 올림처리해야함.

    stack = []  # 배포전 완료된 작업을 넣어놓는 임시 저장소

    for i in range(len(deploy)):
        if not stack:  # 스택이 아예 비어있으면 그냥 넣음 (맨 처음)
            stack.append(deploy[i])
        else:
            if max(stack) < deploy[i]:  # 우선순위가 높은 작업이 더 빨리 완료될 경우
                answer.append(len(stack))
                stack.clear()  # 임시로 저장되어 있던 모든 작업 배포
                stack.append(deploy[i])  # 더 오래걸리는 새로운 작업 저장
            else:
                stack.append(deploy[i])  # 우선순위가 높은 작업이 더 늦게 완료될 경우

    # 모든 작업을 다 비교하고 배포되지못한 작업들을 위한 처리
    if len(stack) == 0:
        pass
    else:
        answer.append(len(stack))

    return answer
