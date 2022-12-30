# 모든작업에 대해서 대기 시간(작업 시작 시간 - 요청이 들어온 시간)이 최소이면 됌. or 대기 시간의 총합이 최소
# 평균 -> 각 작업이 종료된 시점(초) - 각 작업이 요청된 시점(초) ==> 각 작업이 시작전에 대기한 시간
# greedy하게 가장 작업수행시간이 짧은 것을 선택
# 주어진 시간에 아예 작업이 존재하지 않는 구간도 생각해야함


def solution(jobs):
    jobs_num = len(jobs)
    jobs.sort(key=lambda x: (x[0], x[1]))  # 요청이 들어온 시간 순서대로 정렬(1.요청시간, 2.작업시간)

    answer = 0  # 각 작업의 대기시간과 작업시간을 전부 더해주고 마지막에 작업 갯수로 나눠서 평균 구하기
    clock = 0  # 현재 몇초가 지났는지 시각을 나타내매

    postponed = []  # 다른 작업이 실행되고 있는 동안 요청이 들어와서 강제로 연기된 작업들을 담는 배열

    while jobs:  # 남은 작업이 없을 때까지 수행
        tmp = jobs.pop(0)  # 요청시간이 제일 작업

        if tmp[0] > clock:  # 요청시간이 현재 clock 보다 크다면, 아무 작업이 없는 공백이 있었던 것이므로, 시간을 증가시켜줌
            clock = tmp[0]

        answer += clock-tmp[0]  # 작업이 요청 시점으로부터 대기한 시간
        answer += tmp[1]  # 작업 수행 시간

        clock += tmp[1]  # 작업 수행 시간만큼 시간 증가

        # 선택된 작업이 종료된 후
        while jobs and jobs[0][0] <= clock:  # 다른 작업이 실행되고 있는 동안 요청이 들어와서 강제로 연기된 작업들
            postponed.append(jobs.pop(0))

        # 다음번 선택될 수 있는 작업들 중에 실행시간이 제일 작은걸 선택
        postponed.sort(key=lambda x: -x[1])

        for job in postponed:
            jobs.insert(0, job)  # joblist 에다가 앞쪽으로 넣어주기

        postponed.clear()  # 다음번에 또 계산해야되니까 clear

    return int(answer/jobs_num)
