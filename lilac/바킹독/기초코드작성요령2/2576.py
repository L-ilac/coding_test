odd = []

for _ in range(7):
    tmp = int(input())
    if tmp % 2 == 1:
        odd.append(tmp)


if not odd:
    print(-1)
else:
    print(sum(odd))
    print(min(odd))
