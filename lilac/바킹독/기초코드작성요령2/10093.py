a, b = map(int, input().split())

if a - b != 0:
    print(max(a, b) - min(a, b) - 1)
    arr = [i for i in range(min(a, b) + 1, max(a, b))]
    print(*arr)
else:
    print(0)
