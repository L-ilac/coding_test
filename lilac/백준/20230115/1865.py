import sys

inf = sys.maxsize

tc = int(input())


def bellman_ford():
    distance = [inf] * (n+1)

    for i in range(n):
        for edge in edges:
            # print(edge)
            cur_node = edge[0]
            next_node = edge[1]
            edge_cost = edge[2]

            # ! distance[cur_node] != inf 조건이 없어도 되는 이유에 대해서 정확하게 알아야함.
            # ! 일반적인 벨만포드 알고리즘은 정해져있는 출발점을 기준으로 각 나머지 정점까지의 최단거리를 구하는 알고리즘이다.
            # ! 그렇기 때문에 그래프상에서 길이 없어서 도달할 수 없는 정점까지의 거리는 inf로 남겨져야되는게 맞음.
            # ! 즉 일반적인 벨만포드 알고리즘은 출발점을 기준으로 도달할 수 없는 정점들에서 발생하는 음수 사이클을 찾을 수 없음.
            # ! 그래서 distance[cur_node] != inf 조건을 빼면,
            # ! 특정 출발점 기준 각 지점까지의 거리를 구하는 것이 아닌, 그래프 내에 음수사이클이 존재하는지 판단하는 알고리즘으로 바뀜
            # ! distance 리스트도 거리를 저장하는 용도가 아니라, 음수사이클을 판단할 수 있는 변화가 존재하기 위한 수단으로 사용함.
            if distance[next_node] > distance[cur_node] + edge_cost:
                distance[next_node] = distance[cur_node] + edge_cost

                # 음수 순환이 존재하는것
                if i == n-1:
                    return True

    return False


for _ in range(tc):
    # 지점수, 도로갯수, 웜홀갯수
    n, m, w = map(int, input().split())
    edges = []

    # 도로정보
    for _ in range(m):
        # 연결된 지점 2개, 이동하는데 걸리는 시간
        # ! 두 지점을 연결하는 도로가 한 개보다 많을 수 있다.
        s, e, t = map(int, input().split())
        edges.append((s, e, t))
        edges.append((e, s, t))

    # 웜홀정보
    for _ in range(w):
        # 시작지점, 도착지점, 줄어드는 시간(0<= t<=10000)
        # ! 웜홀은 단방향이며, 가중치가 음수임
        s, e, t = map(int, input().split())
        edges.append((s, e, -t))

    # 벨만포드는 출발점을 제외한 노드 갯수만큼 모든 edge 에 대해 처리

    if bellman_ford():
        print("YES")
    else:
        print("NO")


#! https://www.acmicpc.net/board/view/72995 주의할점, 꼭 읽어볼 것
#! https://yabmoons.tistory.com/365 벨만포드 알고리즘 설명
