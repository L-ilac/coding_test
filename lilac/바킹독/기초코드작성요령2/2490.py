for _ in range(3):
    tmp = list(map(int, input().split()))
    a = tmp.count(0)

    if a == 0:
        print("E")
    elif a == 1:
        print("A")
    elif a == 2:
        print("B")
    elif a == 3:
        print("C")
    else:
        print("D")
