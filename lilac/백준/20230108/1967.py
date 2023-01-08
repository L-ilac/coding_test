# 문제 접근법
# ! 1. 모든 non-leaf 노드에 대해서 자기자신으로부터 가장 말단에 있는 leaf 노드까지의 모든 길이를 구한다.
# ! 2. 매번 길이를 구할 때마다, 최대값을 갱신할 수 있다면 갱신함.
# ! 3. 1~2에서 구한 leaf노드 까지의 모든 길이중 가장 긴 2개를 선택하여 더해서 가장 길다면, 가장 긴 지름으로 갱신.

# ? pypy로만 통과한 풀이, python3으로는 36%에서 막힘. -> 사실상 완전탐색이기 때문

from collections import defaultdict
import sys
sys.setrecursionlimit(10002)
n = int(input())

graph = defaultdict(list)
non_leaf = set()

for _ in range(n-1):
    # 부모, 자식, 가중치 순
    parent, child, weight = map(int, sys.stdin.readline().split())
    # 부모 노드
    non_leaf.add(parent)
    # parent -> child 경로가 비용이 weight
    # ! dfs를 부모 -> 자식 방향으로만 수행하기 위해 단방향으로 설정
    graph[parent].append((child, weight))


# ! start 노드를 기준으로 자식 중에 가장 먼거리에 있는 노드까지의 거리를 구하는 함수
def dfs(start, total):
    # 더이상 자식이 없다면
    if not graph[start]:
        return total

    max_route = 0
    for child, weight in graph[start]:
        max_route = max(max_route, dfs(child, total + weight))

    return max_route


longest_radius = 0

for node in non_leaf:
    tmp = []
    for child, weight in graph[node]:
        tmp.append(weight + dfs(child, 0))

    tmp.sort(reverse=True)

    long = 0

    # * 이진 트리가 아닐 수 있기 때문에, 상위 2개만 골라서 쓴다.
    if len(tmp) > 2:
        long += tmp[0] + tmp[1]
    else:
        long += sum(tmp)

    longest_radius = max(longest_radius, long)


print(longest_radius)
