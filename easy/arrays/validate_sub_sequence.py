# 0(N) N is the length of the array 
# O(1) Space
def isValidSubsequence(array, sequence):

    idx = 0 # array
    idy = 0 # seq
    while(idx < len(array) and idy < len(sequence)):
        seq_num = sequence[idy]
        array_num = array[idx]
        if (seq_num == array_num):
            idy += 1
        idx += 1
    if idy == len(sequence):
        return True
    return False


# Solution 2 
# O(N)
# O(1)
def isValidSubsequence(array, sequence):
    idx = 0
    for num in array:
        if idx == len(sequence):
            return True
        if num == sequence[idx]:
            idx += 1

    return idx == len(sequence)

