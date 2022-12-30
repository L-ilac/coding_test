n = int(input())
coins = list(map(int, input().split()))

coins.sort()

target = 1
while True:
    if target in coins:
        target += 1
        continue
    else:
        total = 0
        for c in coins:
            if c > target:
                break
            total += c

        if total < target:
            break
        else:
            target += 1

print(target)
target = 1
for c in coins:  # 코인은 작은 숫자부터 정렬되어있다.
    if target < c:
        break
    target += c


coins.sort()  # 오름차순으로 동전 정렬

"""target은 내가 가진 동전들로 다음번에 내가 만들어야하는 숫자이며 매 순간 타겟값을 만족시키는 동전 조합이 없는지 
체크하여 만들 수 없는 최소의 자연수를 구하면 된다.(그러므로 초기 타겟값은 가장 작은 자연수인 1)"""

target = 1
# 타겟보다 작은 자연수 값은 다 만들 수 있다고 가정

for coin in coins:  # 코인을 하나씩 꺼낸다고 생각하자.(가장 작은 코인부터 꺼내는 상황)
    if coin > target:  # 가장 작은 코인을 꺼냈는데, 타겟보다 코인의 값이 크면, 타겟에 해당하는 숫자를 내가 가진 코인으로 만들수 없음.
        break

    # 코인의 값이 타켓과 같거나 타겟보다 작으면, 다음번에 만들어야하는 숫자는 타겟에 방금 꺼낸 코인의 숫자를 더한 값임.
    target += coin
    # 이전 타겟 값 부터 바뀐 타겟 값 사이의 숫자들은 방금 꺼낸 코인을 이전 타겟보다 작은 숫자들을 만들 때 사용했던 조합에다가 새로 꺼낸 코인값만 더해주면 됌.
