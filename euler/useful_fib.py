
#http://stackoverflow.com/questions/2432669/test-if-a-number-is-fibonacci
# N is fib iff 5N^2+4 or 5N-4 is square number

import math

def is_square(n):
	return (pow(int(math.sqrt(n)),2) == n)

def is_fib(n):
	return is_square(5*n+4) or is_square(5*n-4)
