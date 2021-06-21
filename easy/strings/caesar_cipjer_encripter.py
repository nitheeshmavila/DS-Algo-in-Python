
# O(N) space 
# O(N) time, Where N is the no of chars in the string
def caesarCipherEncryptor(string, key):
    alphabets = list('abcdefghijklmnopqrstuvwxyz')
    encrypted = []
    for ch in string:
        new_index = (alphabets.index(ch) + key) % 26
        encrypted.append(alphabets[new_index])
    return "".join(encrypted)


def caesarCipherEncryptor(string, key):
    encrypted = []
    for ch in string:
        new_code = ord(ch) + key
        unicode = new_code
        if new_code <= 122:
            unicode = 96 + (new_code % 122)

        encrypted.append(chr(unicode))
    return "".join(encrypted)

print(caesarCipherEncryptor("z", 1))