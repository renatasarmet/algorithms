def two_sum(list_numbers, k):
	possible_numbers = {}

	for n in list_numbers:
		if n in possible_numbers:
			return True
		else:
			rest = k - n
			possible_numbers[rest] = 1

	return False


print(two_sum([4,7,1,-3,2], 5))
# True
