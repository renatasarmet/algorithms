# Todo: salvar o fatorial anterior pra nao ter que ficar recalculando
def fatorial(number):	
	fat = 1
	while number > 1:
		fat *= number
		number -= 1
	return fat


def staircase(n):
	if n <= 0:
		return 0

	# start with base case - always climb 1
	unique_ways = 1 
	number_of_ones = n
	number_of_twos = 0

	# at each iteration, try inserting one more case of number 2
	while number_of_ones > 1:
		number_of_ones -= 2
		number_of_twos += 1

		# number_of_ones * 1 + number_of_twos * 2 == n:
		# calculate permutation
		unique_ways += fatorial(number_of_ones + number_of_twos) / (fatorial(number_of_ones) * fatorial(number_of_twos))

	return int(unique_ways)


print(staircase(4))
# 5
print(staircase(5))
# 8
