# naive implementation

def dec2bin(n):
	if n == 0:
		return '0'
	bin_str = ''
	while n > 0:
		bin_str = str(n%2)+bin_str
		n=n>>1
	
	return bin_str

def is_palindrom(n):
	if n == '':
		return True
	
	if n[0] == n[len(n)-1]:
		return is_palindrom(n[1:-1])

	return False

def main():
	result = 0
	for i in xrange(1,1000000):
		base2 = dec2bin(i)
		if is_palindrom(str(i)) and is_palindrom(base2):
			result += i

	print result

if __name__ == "__main__":
	main()
