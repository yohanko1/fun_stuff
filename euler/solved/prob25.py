import math

def fib():
	a,b = 1,1
	n = 1
	
	while True:
		if len(str(a)) >= 1000:
			break
		a, b = b, a+b
		n += 1
	
	print n


fib()
