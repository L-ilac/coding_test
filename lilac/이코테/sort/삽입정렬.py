

a = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]


for i in range(1, len(a)):
    # * 거꾸로 내려가면서 정렬시키는 특징
    for j in range(i, 0, -1):  # ! i에서 1까지 -1 줄여가며 반복
        if a[j] < a[j-1]:
            a[j], a[j-1] = a[j-1], a[j]
        else:
            break

print(a)

# ! 2번째 원소부터 어느 위치에 현재 데이터가 들어가야하는지 판단하고 삽입한다.
