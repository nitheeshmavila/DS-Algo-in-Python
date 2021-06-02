# solition
# O(m * (m+n)) where m is the no of chars in document and n is the no of chars in characters
# O(1)
def generateDocument(characters, document):
    for char in document:
        count_in_doc = find_count(document, char)
        count_chars = find_count(characters, char)
        if count_in_doc > count_chars:
            return False
    return True

def find_count(string, char):
    # return string.count(char)
    count = 0
    for c in string:
        if c == char:
            count += 1
    return count

# Solition2
# O(c * (m+n)) where m is the no of chars in document and n is the no of chars in characters
# where c is no of unique characters in document
# O(c) 
def generateDocument(characters, document):
    already_seen = set()
    for char in document:
        if char in already_seen:
            continue
        count_in_doc = find_count(document, char)
        count_chars = find_count(characters, char)
        if count_in_doc > count_chars:
            return False
        already_seen.add(char)
    return True

def find_count(string, char):
    # return string.count(char)
    count = 0
    for c in string:
        if c == char:
            count += 1
    return count

# solution3 
# O(n + m + c) Time where m is no of char in document, n is no of char in characters, c is no of unique chars in document
# O(c + d) Space c is no of unique chars in document, d is no of unique chars in characters
def generateDocument(characters, document):
    doc_char_freq = get_character_freq(document)
    char_freq = get_character_freq(characters)

    for char, freq in doc_char_freq.items():
        if char not in char_freq:
            return False
        if freq > char_freq[char]:
            return False
    return True



def get_character_freq(string):
    char_freq = {}
    for c in string:
        char_freq[c] = char_freq.get(c, 0) + 1
    return char_freq


# solution4
# O(n + m) Time where m is no of char in document, n is no of char in characters
# O(d) d is no of unique chars in characters
def generateDocument(characters, document):
    char_freq = {}
    for c in characters:
        char_freq[c] = char_freq.get(c, 0) + 1
    
    for char in document:
        if char not in char_freq or char_freq[char] == 0:
            return False
        char_freq[char] -= 1

    return True