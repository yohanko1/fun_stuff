import math

test_num = 10000

def get_proper_divisors(n):
	divisors = []
	for i in xrange(1, int(math.sqrt(n))+1):
		if n % i == 0:
			divisors.append(i)	
			divisors.append(n/i)	

	divisors.remove(n)
	return divisors

def is_amicable_pair(n1, n2):
	if n1 == n2:
		return False

	sum1 = sum(get_proper_divisors(n1))
	sum2 = sum(get_proper_divisors(n2))
	return n1 == sum2 and n2 == sum1

def main():
	result = 0
	for i in xrange(1, test_num+1):
		dn = sum(get_proper_divisors(i))
		if dn > test_num:
			continue
		if is_amicable_pair(i, dn):
			result += i

	print result

if __name__ == "__main__":
	main()
