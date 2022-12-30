def Insertion_sort(array):
	for i in range(1,len(array)):
		for j in range(i,0,-1):
			if array[j-1] > array[j]:
				array[j-1], array[j] = array[j], array[j-1]
			else:
				break

array = [9,8,7,6,5,4,3,2,1]

Insertion_sort(array)

print(array)

# 안쪽 for문에서 역순으로 내려가면서 정렬하는게 포인트. i의 값을 기준으로 i보다 작은 부분은 이미 정렬되어있다고 가정한다.