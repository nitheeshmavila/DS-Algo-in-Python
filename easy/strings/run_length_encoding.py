

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

update_encoded_list(run_length, character, encoded_list):
    encoded_list.append(str(run_length))
    encoded_list.append(character)


#A A A A A A A A A A
#2 3 4 5 6 7 8 9