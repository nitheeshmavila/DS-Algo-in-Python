# O(N^2) TIME where N is the no of elements in the array

def bubble(array):
	for i in range(len(array)):
		swapped = False
		for idx in range(len(array) - 1 - i):
			if array[idx] > array[idx+1]:
				array[idx], array[idx+1] = array[idx+1], array[idx]
				swapped = True
		if not swapped:
			break
	return array


