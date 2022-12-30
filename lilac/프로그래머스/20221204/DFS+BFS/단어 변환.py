# 그냥 한글자씩 차이 나는 단어끼리 graph 만들고, 최단거리 구해야하므로 bfs 돌리기
from collections import defaultdict, deque

# 글자 두개를 비교해서 한글자만 차이 나는지 true/false 반환


def cmpTwoWords(word1, word2):
    cnt = 0
    for i in range(len(word1)):
        if word1[i] == word2[i]:
            cnt += 1

    if cnt == len(word1) - 1:
        return True

    return False


def solution(begin, target, words):
    answer = 0
    queue = deque()

    # 그래프 연결 상태 표현
    # 중복된 단어가 없으므로, 무방향 그래프로 나타낼 수 있음
    graph = defaultdict(list)

    # 시작점도 그래프에 추가
    words.append(begin)

    # 각 단어에 해당하는 노드에 방문했는지 표현하는 딕셔너리
    visited = dict.fromkeys(words, False)

    # 타겟이 단어 목록에 없으면 애초에 못찾음
    if target not in words:
        return 0

    # 그래프 그리기 -> 두단어 비교해서 true 반환시 그래프 상에서 연결
    for word1 in words:
        for word2 in words:
            if cmpTwoWords(word1, word2):
                graph[word1].append(word2)

    # 출발에 해당하는 단어, 시작 지점으로 부터 몇칸 이동했는지 저장하기 위한 0
    queue.append([begin, 0])
    visited[begin] = True  # 방문 처리

    # bfs 수행
    while queue:

        now = queue.popleft()
        # 만약 타겟 찾을 경우 -> 현재까지 몇칸 이동했는지 반환
        if now[0] == target:
            return now[1]

        # 타겟이 아닐 경우, 현재 방문하고 있는 노드에서 '방문하지 않은' 갈 수 있는 모든 노드를 큐에 추가
        for i in graph[now[0]]:
            if not visited[i]:  # 방문하지 않은 노드에 대해서만 수행하면 됌
                visited[i] = True  # 방문 처리
                # 현재 노드(now) 기준으로 1칸 떨어진 노드를 추가하므로 now[1] + 1 처리
                queue.append([i, now[1]+1])

    # 끝까지 타겟을 못찾을 경우, 도달하지 못했으므로 0 반환
    return 0
