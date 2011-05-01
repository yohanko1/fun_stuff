
def fib(n):
	a, b = 1, 2
	result = 0

	while a < n:
		if 0 == a % 2:
			result += a
		a, b = b, a+b

	print result


fib(4000000)
