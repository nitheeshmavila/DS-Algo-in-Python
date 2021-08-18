

# QNS
# Should we consider uppercase/lowercase ?
# Should we consider white space ?


# O(N LOGN) Where N is the length of the string
# O(1)
def permutation(string1, string2):

    if len(string1) != len(string2): return False

    string1 = "".join(sorted(string1))
    string2 = "".join(sorted(string2))
    return string1 == string2


# O(M+D) SPACE - where M is the no of unique chars in string1, D is the no of unique chars in string2
# O(N+K) TIME - Where N is no of chars in string1 and K is the no of chars in strong2
def permutation(string1, string2):

    if len(string1) != len(string2): return False

    original_char_count = {}
    for ch in string1:
        original_char_count[ch] = original_char_count.get(ch, 0) + 1
    
    char_count = {}
    for c in string2:
        char_count[c] = char_count.get(c, 0) + 1
    
    for key, value in char_count.items():
        if key not in original_char_count or original_char_count[key] != value:
            return False
    return True


# O(M) SPACE - where M is the no of unique chars in string1
# O(N+K) TIME - Where N is no of chars in string1 and K is the no of chars in strong2
def permutation(string1, string2):

    if len(string1) != len(string2): return False

    original_char_count = {}
    for ch in string1:
        original_char_count[ch] = original_char_count.get(ch, 0) + 1
    
    for ch in string2:
        if ch not in original_char_count: return False
        original_char_count[ch] = original_char_count.get(ch) - 1
        if original_char_count[ch] < 0: return False
    return True

    

print(permutation("ree","eer"))
