#string reversal 

s = 'string'

def recursion_reverse(string):
	if len(string) == 1:
		reverse = string
	elif len(string) > 1:
		reverse = string[-1] + recursion_reverse(string[:-1])
	return reverse

if __name__ == '__main__':
	print recursion_reverse(s)