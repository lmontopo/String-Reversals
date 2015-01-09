# string reversal using reversed range

s = 'string'

def string_reverse(string):
	reversed_string = '' 
	for i in range(len(string), 0, -1):
		reversed_string += string[i - 1]
	return reversed_string

if __name__ == '__main__':
	print string_reverse(s)


