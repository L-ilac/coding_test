from itertools import permutations
from itertools import combinations
from collections import deque

# 맨 처음 풀었을 때 답변, 거의 2~3시간 걸림


def solution(n, weak, dist):
    answer = 0
    # 주어진 weak 배열에 요소 사이마다 칸막이를 설치할 수 있다고 생각하자.
    split_comb = []
    min_person = 1e9

    for i in range(1, len(weak)+1):
        for i in combinations([i for i in range(len(weak))], i):
            split_comb.append(list(i))

    for split in split_comb:
        q = deque()
        for idx, value in enumerate(weak):
            if idx in split:
                q.append('/')
                q.append(value)
            else:
                q.append(value)

        # ! q는 칸막이 '/' 가 삽입된 큐이다. 칸막이는 최소 1개 들어가있음.
        while q[0] != '/':
            q.append(q.popleft())

        section = []
        tmp = []

        while q:
            now = q.popleft()

            if now == '/':
                if tmp:
                    section.append(tmp[:])
                    tmp.clear()
            else:
                tmp.append(now)
        section.append(tmp)

        # print(section)

        gap = []
        for s in section:
            if len(s) == 1:
                gap.append(1)
            else:
                if s[0] < s[-1]:
                    gap.append(s[-1]-s[0])
                else:
                    gap.append(n-s[0] + s[-1])

        # print(gap)
        # 구한 거리 랑 조사단이랑 비교
        gap.sort(reverse=True)
        fixed_cnt = len(gap)

        human = dist[:]
        human.sort(reverse=True)
        person_cnt = 0

        # print(gap)
        # print(human)

        while gap and human:
            now_gap = gap.pop(0)
            if now_gap <= human[0]:
                fixed_cnt -= 1
                person_cnt += 1
                human.pop(0)
            else:
                break

        if fixed_cnt == 0:
            min_person = min(min_person, person_cnt)

    if min_person == 1e9:
        return -1

    return min_person


# 답안을 보고 참고한 뒤에 다시 푼것
def solution2(n, weak, dist):
    # 수리하는 사람은 최소 1명 투입되어야함. 1명 ~ len(dist)명 까지 조합
    # 지도가 원형이므로 출발점이 len(weak)개로 간주하고 풀어야함.

    for i in range(1, len(dist)+1):
        # 전체 친구중 i명 뽑은 모든 순열 -> 친구들이 어떤 순서로 투입되냐도 고려해야하는 부분임
        perms = list(permutations(dist, i))

        # 각각의 조합에 대해서 len(weak)개 만큼 조사해야함
        for friends in perms:
            tmp = weak[:]  # 조사해야할 취약 구간
            # friends -> 조사에 투입될 친구 조합

            # 출발이 가능한 지점이 len(weak)개 임
            for _ in range(len(weak)):
                # 모든 weak에 대해 조사
                input_cnt = 1  # 투입될 친구의 수
                cover = tmp[0] + friends[input_cnt - 1]  # 투입된 친구가 조사할 범위
                for i in range(1, len(tmp)):
                    if cover < tmp[i]:  # 현재 투입된 친구가 커버할 수 있는 범위를 벗어났다면?
                        input_cnt += 1  # 추가 투입, 다음 친구는 tmp[i] 부터 탐색해야함
                        if input_cnt > len(friends):  # 현재 조합을 넘었다면 해당인원으로 전부 조사 실패
                            break
                        # 조사를 시작해야하는 위치 재설정
                        cover = tmp[i] + friends[input_cnt - 1]

                # 조합을 1명 ~ len(dist)명 순으로 넣고 있기 때문에, 빨리 구해진게 최소값임
                if input_cnt <= len(friends):
                    return input_cnt

                # 모든 출발점을 기준으로 조사해야함
                tmp.append(tmp[0] + n)
                tmp = tmp[1:]
                # tmp = tmp[1:] + [n+tmp[0]]

    # 만약에 모든 조합에 대해서 돌렸는데 return이 안됐다면?

    return -1
