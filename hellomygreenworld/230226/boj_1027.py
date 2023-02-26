# !usr/bin/env python
# -*- coding: utf-8 -*-
# boj 1027 고층건물

n = int(input())
buildings = list(map(int, input().split()))

m = max(buildings)
m_idx = buildings.index(m)

def calc_gradient(x1, y1, x2, y2):
    if x1 == x2:
        return 0
    gradient = abs((y2 - y1) / (x2 - x1))
    return gradient

gradients = []
for idx, building in enumerate(buildings):
    gradient = calc_gradient(idx, building, m_idx, m)
    gradients.append(gradient)

answer = 0
min_gradient = 0
for i in range(m_idx - 1, -1, -1):
    if i == m_idx - 1:
        answer += 1
        min_gradient = gradients[i]
        continue
    # 현재 기울기가 지금까지의 기울기의 최솟값보다 완만하면 보임
    if gradients[i] <= min_gradient:
        answer += 1
        min_gradient = min(min_gradient, gradients[i])
    # 현재 기울기가 지금까지의 완만함보다 가파르면 안보임
    # else:
    #     max_gradient = gradients[i]

min_gradient = 0
for i in range(m_idx + 1, len(buildings)):
    
    if i == m_idx + 1:
        answer += 1
        min_gradient = gradients[i]
        continue
    if gradients[i] <= min_gradient:
        answer += 1
        min_gradient = min(min_gradient, gradients[i])
    # else:
    #     min_gradient = gradients[i]

# print(gradients)
print(answer)
