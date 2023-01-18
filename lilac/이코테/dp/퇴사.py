# n = int(input())

# dp = [0] * (n+1)

# case = []

# for _ in range(n):
#     t, p = map(int, input().split())
#     case.append((t, p))


# for idx, c in enumerate(case, start=1):
#     for i in range(idx+c[0]-1, n+1):
#         dp[i] = max(dp[i], dp[idx-1] + c[1])

# print(dp[-1])


n = int(input())

dp = [0] * (n+1)
cases = []

for _ in range(n):
    t, p = map(int, input().split())
    cases.append((t, p))


for idx, c in enumerate(cases, start=1):
    # ! idx일차에 상담이 가능하다면?
    if idx + c[0] - 1 <= n:
        #! idx일차에 시작한 상담이 끝나는 날 이후에는 새로운 상담을 진행할 수 있으므로,
        #! (idx-1일차까지의 이익 + idx일차에 상담을 진행했을 때 얻는 이익)으로 idx일차에 시작한 상담이 끝나는 날 이후의 이익들을 갱신해준다.
        for i in range(idx + c[0]-1, n+1):
            dp[i] = max(dp[i], dp[idx-1] + c[1])

print(dp[-1])


# ! 뒤에서부터 접근


n = int(input())

#! dp[i] -> i일차의 최대이익 (i일차에 잡힌 상담을 했을수도, 안했을수 도 있음)
dp = [0] * (n+2)

cases = []

for _ in range(n):
    t, p = map(int, input().split())
    cases.append((t, p))


#! i일에 상담을 할수없다면?(퇴사전에 완료하지 못함) -> i+1일까지의 이익을 그대로 가져와야함(강제임)
#! i일에 상담을 할수있다면? -> 해도 되고, 안해도 됌. 둘중에 이익이 큰걸 고르면 된다.

# * 상담을 할 수 있는 경우
#! i일에 상담을 할때의 이익 -> i일 상담의 이익 + i일 상담을 하는데 걸리는 시간 후의 이익)
#! i일에 상담을 안한다면? -> i+1일에 상담을 할때의 이익
#! 둘중에 이익이 큰 것을 선택한다.
for i in range(len(cases), 0, -1):
    # 정해진 상담일자에 시작해도 퇴사전에 못 끝내는 상담
    if i+cases[i-1][0] > n+1:
        dp[i] = dp[i+1]
    else:
        # i+1 접근 불가할 수 있는 경우
        dp[i] = max(dp[i+1], dp[i+cases[i-1][0]]+cases[i-1][1])

print(dp[1])
