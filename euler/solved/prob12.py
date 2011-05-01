
import math

def triangle_divisors(n):
	tri = (n*(n+1))/2 # same as sum(i for i in range(1,n+1))
	count = 0
	for candidate in xrange(1, int(math.sqrt(tri))+1):
		if tri % candidate == 0:
			count += 1
	
	return tri, count*2 - 1*(tri/int(math.sqrt(tri)) == int(math.sqrt(tri)))
	# last term may not be necessary


def main():
	n = 1
	while True:
		tri, count =	triangle_divisors(n)
		n += 1
		if count > 500:
			break
	
	
	print tri
	

if __name__ == "__main__":
	main()
