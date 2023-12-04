n = int(input())

weights = list(map(int, input().split()))

weights.sort()

target = 1  # 무게추로 측정 가능한지 판단하고 싶은 값

for w in weights:
    if target >= w:
        target += w
    else:
        break

print(target)
