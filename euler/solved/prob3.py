import math

def find_divisors(target):
    divisors = []
	for i in xrange(1,int(math.sqrt(target)) + 1,2):
		if target % i == 0:
			divisors.append(i)	

	return divisors


def check_odd_prime(target):
	for i in xrange(3,int(math.sqrt(target)) + 1,2):
		if target % i == 0:	
			return False

	return True


def main():

	candidates = find_divisors(600851475143)
#	candidates = find_divisors(13195)

	candidates.reverse()

	for i in candidates:
		if check_odd_prime(i):
			print i
			return

if __name__ == "__main__":
	main()
