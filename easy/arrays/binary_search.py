# O(long(N)) N is the no of elements in this array
def binarySearch(array, target):
    left = 0
    right = len(array) - 1

    while left <= right:
        print(array)
        mid = (right + left) // 2
        print(mid)
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

l = [23,3,4,5,6]
print(binarySearch(l, 3))

