import sys
n = int(input())
p = list(map(int, input().split()))

p_sum_left = [0] * n
p_sum_right = [0] * n

p_sum_left[0] = p[0]
p_sum_right[-1] = p[-1]

for i in range(1, n):
    p_sum_left[i] += p_sum_left[i-1] + p[i]
    p_sum_right[n-1-i] += p_sum_right[n-i] + p[n-1-i]


# print(p_sum_left)


# 맨 앞부터 i번째 사람까지 포함할수 있을 때, 만들 수 있는 최악의 스타성 지수

# 맨 앞부터 i-1번째 사람까지 포함할 수 있을 때, 만들 수 있는 최악의 스타성 지수 + i번째 사람을 포함하거나 안하거나


worst_left = [0] * n

# 맨 뒤부터 i번째 사람까지 포함할수 있을 때, 만들 수 있는 최악의 스타성 지수
worst_right = [0] * n


# 맨 앞부터 i번째 사람까지 포함할수 있을 때, 만들 수 있는 최고의 스타성 지수
best_left = [0] * n

# 맨 뒤부터 i번째 사람까지 포함할수 있을 때, 만들 수 있는 최고의 스타성 지수
best_right = [0] * n

worst_left[0] = p[0]
best_left[0] = p[0]

worst_right[-1] = p[-1]
best_right[-1] = p[-1]


min_p_sum = min(p[0], 0)
max_p_sum = max(p[0], 0)

for i in range(1, n):

    # ! worst에는 max를 빼주고, best에는 min을 빼주고 있다. 그 점을 밑의 질문과 같이 생각해볼것.
    worst_left[i] = min(p_sum_left[i]-max_p_sum, worst_left[i-1])
    best_left[i] = max(p_sum_left[i]-min_p_sum, best_left[i-1])

    #! min,max 값을 저장하는 이유에 대해 다시 생각해볼 것
    min_p_sum = min(min_p_sum, p_sum_left[i])
    max_p_sum = max(max_p_sum, p_sum_left[i])

min_p_sum = min(p[-1], 0)
max_p_sum = max(p[-1], 0)

for i in range(n-2, -1, -1):

    worst_right[i] = min(p_sum_right[i]-max_p_sum, worst_right[i+1])
    best_right[i] = max(p_sum_right[i]-min_p_sum, best_right[i+1])

    min_p_sum = min(min_p_sum, p_sum_right[i])
    max_p_sum = max(max_p_sum, p_sum_right[i])

# print(worst_left)
# print(worst_right)

# print(best_left)
# print(best_right)

answer = -sys.maxsize
for i in range(0, n-1):
    answer = max(worst_left[i] * worst_right[i+1],
                 best_left[i] * best_right[i+1])

print(answer)
