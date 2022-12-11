import itertools


def solution(k, dungeons):
    answer = -1
    case = list(range(len(dungeons)))  # 던전을 인덱스로 접근하기 위해 던전 갯수만큼 인덱스 삽입
    # 가능한 던전 방문 순서를 모두 구하기
    case = list(itertools.permutations(case, len(case)))

    for c in case:  # 모든 경우에 대하여
        tired = k  # 피로도가 k
        cnt = 0

        for i in c:
            if tired-dungeons[i][0] >= 0:  # 현재 입장하려는 던전의 최소 필요 피로도보다 내 피로도가 클때
                tired -= dungeons[i][1]  # 던전 입장하고, 소모 피로도를 뺌
                cnt += 1  # 방문한 던전 갯수 카운트
            else:
                break  # 최소 필요 피로도를 충족하지 못하면, 던전에 들어갈 수 없음

        answer = max(answer, cnt)  # 현재까지 연달아 입장한 던전의 최댓값

    return answer
