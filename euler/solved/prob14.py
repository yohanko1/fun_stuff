# running slow...optimization needed
def iter_seq(n):
	if n % 2 == 0:
		return n/2
	else:
		return 3*n + 1

def get_chain_num(n):
	k = iter_seq(n)
	count = 2
	while k != 1:
		k = iter_seq(k)
		count += 1
		
	return count

def main():
	curr_max = 0
	result = 0
	for i in xrange(1, 1000000+1):
		candidate = get_chain_num(i)
		if curr_max < candidate:
			curr_max = candidate
			result = i
			
	print result

if __name__ == "__main__":
	main()
