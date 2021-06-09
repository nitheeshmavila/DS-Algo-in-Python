
# O(N) time, where N is the no of chars in string
# O(N) SPACE
def runLengthEncoding(string):
	encoded = []
	run_length = 1
	idx = 0
	while idx < len(string):
		char = string[idx]
		if idx == len(string) - 1:
            update_encoded_list(run_length, char, encoded)
			break
					
		if string[idx] == string[idx+1]:
            if  run_length == 9:
                update_encoded_list(run_length, char, encoded)
                run_length = 1
            else:
                run_length += 1
		else:
            update_encoded_list(run_length, char, encoded)
			run_length = 1
	    idx += 1
		
	return "".join(encoded)

def update_encoded_list(run_length, character, encoded_list):
    encoded_list.append(str(run_length))
    encoded_list.append(character)



# Solution 2 
# O(N) time
# O(N) space where N is the number of chars in string
def runLengthEncoding(string):
	encoded = []
	run_length = 1
	idx = 0
	
	for idx in range(len(string) -1):
		next_char = string[idx + 1]
		current_char = string[idx]
	
		if next_char != current_char or run_length == 9:
			encoded.append(str(run_length))
			encoded.append(current_char)
			run_length = 0

		run_length += 1

	encoded.append(str(run_length))
	encoded.append(string[-1])
	return "".join(encoded)


#A A A A A A A A A A
#2 3 4 5 6 7 8 9