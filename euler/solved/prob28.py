
import math

num_col = 1001

def main():
	result,	current_end, offset = 1, 1, 2

	# level starts from 1(center)
	for level in xrange(1, int(math.ceil(num_col/2))+1):
		current_begin = current_end+level*2
		current_end = current_begin+offset*3
		result += sum(range(current_begin, current_end+1, offset))
		offset += 2

	print result

if __name__ == "__main__":
	main()
