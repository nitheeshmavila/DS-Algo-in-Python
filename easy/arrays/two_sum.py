# O(N^2) Time, Where N is the no of elements inside the array
# O(1) Space

def twoNumberSum(array, targetSum):
    
	for i in range(len(array) - 1):
		for j in range(i+1, len(array)):
			if array[i] + array[j] == targetSum:
				return [array[i], array[j]]
	return []


# O(N) Time, Where N is the no og
# O(N) Space
def twoNumberSum(array, targetSum):
	compliments = set()
	
	for num in array:
		if num in compliments:
			return [num, targetSum - num]
		compliments.add(targetSum - num)
	return []

# O(N logN) Time where N is the no of elements
# O(1) SPACE
def twoNumberSum(array, targetSum):
	array.sort()
	
	left = 0
	right = len(array) - 1
	
	while left < right:
		current_sum = array[left] + array[right]
		if current_sum == targetSum:
			return [array[left], array[right]]
		elif current_sum < targetSum:
			left += 1
		else:
			right -= 1
	return []
