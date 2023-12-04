from itertools import combinations
from collections import defaultdict


def solution(orders, course):
    dic = defaultdict(int)

    answer = []

    new_orders = []
    for i in orders:
        new_orders.append(set(i))

    orders.sort(key=lambda x: len(x))

    for o in orders:
        for i in range(2, len(o)+1):
            for case in combinations(o, i):
                tmp = list(case)
                tmp.sort()

                dic[''.join(tmp)] += 1

    print(dic)

    return orders


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
