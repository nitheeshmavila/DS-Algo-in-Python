# O(N) time, where N is the length of the array
# O(1) space
def findThreeLargestNumbers(array):
    output = [None, None, None]

    for num in array:
        if output[2] is None or num >= output[2]:
            shift_left_and_update(output, 2, num)
        elif output[1] is None or num >= output[1]:
            shift_left_and_update(output, 1, num)
        elif output[0] is None or num >= output[0]:
            shift_left_and_update(output, 0, num)

def shift_left_and_update(array, idx, num):
    for i in range(idx + 1):
        if i == idx:
            output[i] = num
        else:
            output[i] = output[i+1]
                





