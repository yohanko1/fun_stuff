
units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

scales = ["hundred", "thousand"]

result = 0

for i in range(1,1000):
	least_two = int(str(i)[-2:])
	if 0 < least_two < 20:
		result += len(units[least_two])
	elif 20 <= least_two <= 99:
		result = result + len(tens[int(str(least_two)[0])-2]) + len(units[int(str(least_two)[1])])

	if 99 < i < 1000:
		if least_two != 0:
			result += len('and')

		result += len(scales[0])
		result += len(units[int(str(i)[0])])

print result + len(scales[1]) + len('and') # count last number manually:1000
