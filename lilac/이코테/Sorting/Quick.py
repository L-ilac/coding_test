# 코드의 일관성을 위해 리스트의 index - 1 과정은 무시한다.
# Naivest Version
def Quick_sort(array, start, end): 
	if len(array) == 1:
		return

	if start >= end:
		return
	
	pivot = array[start]
	left = start + 1
	right = end

	while True:
		while array[left] < pivot and left <= end:
			left += 1
		while array[right] > pivot and right > start:
			right -= 1

		if left > right :
			break

		array[left],array[right] = array[right], array[left]

	array[start], array[right] = array[right], array[start]

	# right가 피벗의 최종 위치이므로 피벗 기준으로 앞뒤로 나눈다.
	Quick_sort(array,start,right-1)  # start와 right -1 이 값이 같으면 피벗 좌측 array의 요소가 1개, right-1이 더 작으면 빈 배열
	Quick_sort(array,right+1,end) # right+1와 end 이 값이 같으면 피벗 우측 array의 요소가 1개, end이 더 작으면 빈 배열 


# 대충 짜면 이런데, 여기서 뭘 더 추가해야할까?


# case 1. 일반적인 swap : left 와 right 가 교차되지 않는 경우 => left는 pivot보다 큰 값을 찾고, right는 pivot보다 작은 값을 찾는다.

# case 2. left 와 right 가 같은 값을 가리키게 되는 경우의 swap : left가 end까지 갔거나, right 가 start + 1 지점 까지 갔을 때. ->

# 주어진 array 에서 한쌍이라도 case 1에 의해 swap이 발생했다면 case 2 가 발생할 수 없음.