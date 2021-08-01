# Qn
# 1. Is the characters are in ASCII / UNICODE?

# SOL1 - store already seen characters, if again saw the same characters then not unique

def is_unique(string):
	already_seen = set()
	for char in string:
		if char in string:
			return False
		already_seen.add(char)
	return True

def is_unique(string):
	for i in range(len(string) - 1):
		for idx in range(i+1, len(string)):
			if string[i] == string[idx]:
				return False
	return True
	
def is_unique(string):
	array = list(string)	
	array.sort()
	for idx in range(len(array) - 1):
		next = idx + 1
		if array[idx] == array[next]:
			return False
	return True

def is_unique(string):
	char_set = [False for i in range(256)]
	for char in string:
		index = ord(char)
		if char_set[index]:
			return False
		char_set[index] = True
	return True

print(is_unique("abcd"))
