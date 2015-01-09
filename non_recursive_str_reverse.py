# string reversal, non-recursively

s = 'string'

def swap_reversal(string):
	string_list = list(string)
	new_string = ''
	
	for i in range(len(string_list) / 2):
		temp = string_list[i]
		string_list[i] = string_list[-(i+1)]
		string_list[-(i+1)] = temp
	
	for i in range(len(string_list)):
		new_string += string_list[i]
	
	return new_string

if __name__ == '__main__':
	print swap_reversal(s)