
# Solution1
# O(N) where n is the length of the string
# O(N) Space
def isPalindrome(string):
    s = ""
    for i in range(len(string)-1, -1, -1):
        s += string[i]
    return s == string

def isPalindrome(string):
    return string == string[::-1]


# solution3
# O(N) Time  - N is the no of chars in the string
# O(1) SPACE
def isPalindrome(string):
    left = 0
    right = len(string) - 1

    while left < right:
        if string[left] == string[right]:
            right -= 1
            left += 1
        else:
            return False
    return True
