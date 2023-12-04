arr = [i for i in range(1, 21)]

for _ in range(10):
    a, b = map(int, input().split())

    tmp = arr[a - 1 : b]

    for i in range(b - a + 1):
        arr[b - 1 - i] = tmp[i]


print(*arr)
