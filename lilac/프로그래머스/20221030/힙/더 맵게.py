# 유일하게 힙을 온전하게 사용한 문제
import heapq


def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville)  # 주어진 입력 배열을 힙으로 만든다

    # 남은 음식이 1개이거나 모든 음식이 k보다 커지기 전까지 루프 수행
    while len(scoville) > 1 and any(K > food for food in scoville):

        first = heapq.heappop(scoville)  # 가장 안매움
        second = heapq.heappop(scoville)  # 2번째로 안매움
        new = first + (second*2)  # 새로운 음식 만들기
        heapq.heappush(scoville, new)  # 새로운 음식 힙에 넣기
        answer += 1  # 섞은 횟수 +1

    if len(scoville) == 1 and scoville[0] < K:  # 가능한 모든 음식을 섞었는데 k를 못넘을 경우
        answer = -1

    return answer
