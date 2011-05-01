import math


start, end = 1, 100
sum_sq, sum_num = 0, 0

num_list = range(start,end+1)

sum_num = pow(sum(num_list),2)

for i in num_list:
	sum_sq += pow(i,2)

print (sum_num - sum_sq)
