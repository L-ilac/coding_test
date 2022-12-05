# 겹치는 건 싫어
N, K = map(int, input().split())
lst = list(map(int, input().split()))
cnt = [0] * 100001

left, right = 0, 0
res = 0

while right < len(lst):
    if cnt[lst[right]] < K:
        cnt[lst[right]] += 1
        right += 1
        res = max(res, right - left)
    else:
        cnt[lst[left]] -= 1
        left += 1

print(res)
    




# 1번 풀이 (Counter + queue 사용)
# from collections import deque, Counter

# N, K = map(int, input().split())
# lst = input().split()
# queue = deque()
# res = 0
# cnt = 0

# for a in lst:
#     queue.append(a)
#     cnt += 1

#     if Counter(queue)[a] > K:
#         while queue:
#             x = queue.popleft()
#             cnt -= 1
#             if x == a:
#                 break

#     res = max(res, cnt)
