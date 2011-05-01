
import math

lowerbound = 10 # we skip single digit since prob specifies "sum"
upperbound = int(math.pow(9.0,5.0)*6) # kinda obvious...
def main():
	result = 0
	for i in xrange(lowerbound, upperbound+1):
		if i == sum([math.pow(float(x),5.0) for x in str(i)]):
			result += i
	
	print result

if __name__ == "__main__":
	main()
