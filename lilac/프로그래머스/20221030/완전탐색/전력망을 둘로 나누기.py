# tree -> no circular
import itertools
import copy


def solution(n, wires):
    # 연결 정보를 딕셔너리로 만들고, 끊어질 줄을 딕셔너리에서 하나 뺀 상태로, 트리를 그린다.
    connected = {i: [] for i in range(1, n+1)}
    answer = 99

    for wire in wires:
        connected[wire[0]].append(wire[1])
        connected[wire[1]].append(wire[0])

    for wire in wires:
        visit = []
        queue = []
        tmp = copy.deepcopy(connected)
        tmp[wire[0]].remove(wire[1])
        tmp[wire[1]].remove(wire[0])

        queue.append(1)

        while queue:
            node = queue.pop(0)
            if node not in visit:
                visit.append(node)
                queue.extend(tmp[node])

        unconnected = n-len(visit)
        diff = abs(unconnected-len(visit))
        answer = min(answer, diff)


solution(7, [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]])


#  ans = n
#     for sub in (wires[i+1:] + wires[:i] for i in range(len(wires))):
#         s = set(sub[0])
#         [s.update(v) for _ in sub for v in sub if set(v) & s]
#         ans = min(ans, abs(2 * len(s) - n))
#     return ans
