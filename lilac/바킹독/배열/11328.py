n = int(input())

for _ in range(n):
    a, b = map(list, input().split())

    a.sort()
    b.sort()

    flag = True

    if len(a) != len(b):
        flag = False
    else:
        for i in range(len(a)):
            if a[i] != b[i]:
                flag = False
                break

    if flag:
        print("Possible")
    else:
        print("Impossible")
        

# ! flag 말고 다른 방법으로 푸는법? -> from collections import Counter