import math

def check_odd_prime(n):
	for i in xrange(3, int(math.sqrt(n))+1, 2):
		if n != i and n % i == 0:
			return False	

	return True


def main():

	count = 1	# start counting from 2
	i = 1	# prime: let's start with 3

	while i > 0:
		i += 2
		if check_odd_prime(i):
			count += 1
			if count == 10001:
			#if count == 6:
				break

	print i

if __name__ == "__main__":
	main()
