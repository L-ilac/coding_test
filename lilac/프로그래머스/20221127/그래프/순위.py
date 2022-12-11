
def solution(n, results):
    answer = 0
    win_graph = [set() for _ in range(n+1)]
    lose_graph = [set() for _ in range(n+1)]
    fix = set()

    for result in results:
        win_graph[result[0]].add(result[1])  # 누구를 이겼는가?
        lose_graph[result[1]].add(result[0])  # 누구에게 졌는가?

    # 실력이 정해져 있고, 실력이 좋은 선수가 항상 이기기 때문에, 무조건 전적은 [n승 0패/n-1승 1패/.../1승 n-1패/0승 n패]
    # 승, 패 모든 정보가 있다면 등수를 확정 지을 수 있고, 확정된 순위를 통해서 새롭게 업데이트 할 수 있음.

    for i in range(1, n+1):  # 모든 선수의 수 만큼 반복문 진행
        # i가 이긴사람들(win_graph)은 i가 진 사람들(lose_graph)에게 모두 짐
        for j in win_graph[i]:
            lose_graph[j].update(lose_graph[i])

        # i가 진 사람들(lose_graph)은 i가 이긴 사람들(win_graph)을 모두 이길 수 있음
        for k in lose_graph[i]:
            win_graph[k].update(win_graph[i])

    print(win_graph)
    print(lose_graph)

    for i in range(1, n+1):  # 순위가 확정된 사람들 세기
        if len(win_graph[i]) + len(lose_graph[i]) == n-1:
            answer += 1

    return answer
