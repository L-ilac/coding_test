def Selection_sort(array):
	for i in range(len(array)-1):
		print(i)
		min_index = i 
		for j in range(i+1,len(array)):
			if array[j] < array[min_index]:
				min_index = j
		
		array[i], array[min_index] = array[min_index], array[i]


array = [9,8,7,6,5,4,3,2,1]
Selection_sort(array)

print(array)
