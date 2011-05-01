import math

k = math.factorial(100)

print sum(int(str(k)[i]) for i in xrange(0,len(str(k))))
