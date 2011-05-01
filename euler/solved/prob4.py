
start, end = 100, 999
fun = range(start,end+1)
fun.reverse()
hotel = beach = fun

def is_palindrome(n):
	c = str(n)
	for i in xrange(0, len(c)/2+1):
		if c[i] != c[len(c)-1-i]:
			return False

	return True


def main():
	curr_max = 0;
	for check in hotel:
		for dive in beach:
			if is_palindrome(check*dive) and curr_max < check*dive:
				curr_max = check*dive

	print curr_max


if __name__ == "__main__":
	main()
