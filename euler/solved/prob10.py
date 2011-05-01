import math

def check_odd_prime(target):
	for i in xrange(3, int(math.sqrt(target))+1,2):
		if target % i == 0:
			return False

	return True 


result = 2

for i in xrange(3, 2000000, 2):
	if check_odd_prime(i):
		result += i

print result
