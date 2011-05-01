import math

result = 0

for i in xrange(1, 1000+1):
	result += int(str(pow(i,i))[-10:])

print str(result)[-10:]
