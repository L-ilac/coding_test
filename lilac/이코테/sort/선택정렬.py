a = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(a)-1):
    min_value, idx = a[i], i
    for j in range(i, len(a)):
        if a[j] < min_value:
            min_value = a[j]
            idx = j

    a[i], a[idx] = a[idx], a[i]

print(a)

# ! 정렬되지 않은 데이터중에 가장 작은 값을 구해서 정렬되지 않은 맨 앞 데이터와 바꾼다.
# ! 안쪽 for문에서 역순으로 내려가면서 정렬하는게 포인트. i의 값을 기준으로 i보다 작은 부분은 이미 정렬되어있다고 가정한다.
