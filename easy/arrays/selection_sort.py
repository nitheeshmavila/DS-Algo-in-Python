
# O(N^2) TIME where N is the no of elements in the array
# O(1) SPACE
def selection_sort(array):

    for i in range(len(array)):

        left = i
        right = i + 1

        while right < len(array):
            if array[left] > array[right]:
                left = right
            right += 1
        
        array[i], array[left] = array[left], array[i]
    return array
