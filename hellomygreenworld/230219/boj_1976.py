# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 1976 여행가자

n = int(input())
m = int(input())
graph = []
visited = [False] * (n + 1)
parent = [i for i in range(n + 1)]

for i in range(n):
    graph.append([idx + 1 for idx, i in enumerate(list(map(int, input().split()))) if i == 1])

plan = list(map(int, input().split()))

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
        return parent[x]
    return x

def union(x, y):
    x = find(x)
    y = find(y)

    if x > y:
        parent[x] = y
    else:
        parent[y] = x

for idx, connected_nodes in enumerate(graph):
    for v in connected_nodes:
        union(idx + 1, v)

result = True
root = parent[plan[0]]
for p in plan[1:]:
    if parent[p] != root:
        result = False
        break

if result == True:
    print("YES")
else:
    print("NO")