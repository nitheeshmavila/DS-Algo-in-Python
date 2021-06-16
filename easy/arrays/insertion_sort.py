# O(N^2) Time complexity where N is the no of elements in the array
def insertionSort(array):
	
	for i in range(1, len(array)):
		idx = i
		
		while idx > 0 and array[idx]  < array[idx-1]:
			array[idx], array[idx-1] = array[idx-1], array[idx]
			idx -= 1
		
	return array
