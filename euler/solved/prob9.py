import math
import sys

a,b = 1,1

while a > 0:
	b = 1
	while b > 0:
		a_sq, b_sq = pow(a,2), pow(b,2) 
		c = math.sqrt(a_sq + b_sq)
		 
		if a+b+c == 1000:
			print a*b*c
			sys.exit()
		
		if c > 1000:
			break

		b += 1
	a += 1
