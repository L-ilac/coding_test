from collections import defaultdict
from itertools import combinations


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])

    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a


def sol(n, nationality):
    answer = 0
    pool = defaultdict(list)

    parent = [i for i in range(0, n + 1)]

    for a, b in nationality:
        union(parent, a, b)

    for i in range(1, n + 1):
        pool[parent[i]].append(i)

    pool_num = []

    for value in pool.values():
        pool_num.append(len(value))

    for i in combinations(pool_num, 2):
        answer += i[0] * i[1]

    return answer


print(sol(2, [[1, 2]]))
