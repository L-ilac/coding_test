def check(answer):
    # 모든 기둥과 보에 대해서 유효한지 검사한다.
    for x, y, a in answer:
        # print(x, y, a)
        # 기둥이 유효한지 확인
        if a == 0:
            # 땅에 박혀있는 기둥은 무조건 유효함
            if y == 0:
                continue

            # 기둥 밑에 기둥과 보 둘 다 없다면, 잘못된 건물
            if [x, y-1, 0] not in answer and [x, y, 1] not in answer and [x-1, y, 1] not in answer:
                return False

        # 보가 유효한지 확인
        else:
            # 보의 양쪽 밑에 기둥이 없는 상태일 경우
            if [x, y-1, 0] not in answer and [x+1, y-1, 0] not in answer:
                # 양쪽 보가 하나라도 없으면 잘못된 건물
                if [x-1, y, 1] not in answer or [x+1, y, 1] not in answer:
                    return False

    # 모든 검사를 다 통과하면 건물은 올바른 건물
    return True


def solution(n, build_frame):
    answer = []

    for x, y, a, b in build_frame:
        # x,y 는 기둥 or 보를 설치 또는 삭제할 교차점의 좌표
        # a: 0 -> 기둥, 1-> 보  b: 0 -> 삭제, 1 -> 설치
        # print([x, y, a, b])
        # 기둥 삭제 # ! 기둥 삭제, 보 삭제로 나누지 않고, 기둥 or 보 삭제로 합쳐도 무관하다.
        if a == 0 and b == 0:
            if [x, y, a] in answer:
                answer.remove([x, y, a])
            else:
                continue

            if check(answer):
                continue
            else:
                answer.append([x, y, a])

        # 기둥 설치
        elif a == 0 and b == 1:
            answer.append([x, y, a])
            # print(answer)
            if check(answer):
                continue
            else:
                answer.remove([x, y, a])
        # 보 삭제
        elif a == 1 and b == 0:
            if [x, y, a] in answer:
                answer.remove([x, y, a])
            else:
                continue

            if check(answer):
                continue
            else:
                answer.append([x, y, a])
        # 보 설치
        elif a == 1 and b == 1:
            answer.append([x, y, a])
            if check(answer):
                continue
            else:
                answer.remove([x, y, a])

        # print(answer)

    answer.sort(key=lambda x: (x[0], x[1], x[2]))

    return answer
