def maximum_product_of_three(lst):
	# First check if it's possible and/or if there is just one solution and return it
	if len(lst) < 3:
		return None
	elif len(lst) == 3:
		return lst[0] * lst[1] * lst[2]

	# Sort the list
	lst.sort()

	# sorted list positive numbers
	positive_numbers = []

	# sorted list negative numbers
	negative_numbers = []

	has_zero = False

	for n in lst:
		if n > 0:
			positive_numbers.append(n)
		elif n < 0:
			negative_numbers.append(n)
		else:
			has_zero = True

	# If we have at most 1 negative number
	if len(negative_numbers) <= 1:
		# Use the 3 biggest positive numbers
		return positive_numbers[-3] * positive_numbers[-2] * positive_numbers[-1]

	# If we dont have positive numbers
	elif len(positive_numbers) == 0:
		# If we have 0
		if has_zero:
			# that's the answer --> 0
			return 0
		# Else if we dont have 0
		else:
			# Use the 3 smallest negative numbers
			return negative_numbers[-3] * negative_numbers[-2] * negative_numbers[-1]

	# In general case (if we have lots of positive and negative numbers)
	else:
		# If we got here, it means we have at least 2 negative numbers and we have at least 1 positive number
		# We will always need to use the biggest positive number

		# Then, we have two options:
		# - Use 2 of the biggest negative numbers (I know its a positive result)
		partial_result_negative = negative_numbers[0] * negative_numbers[1]

		# - Use the second and the third biggest positive numbers (if it exists)
		partial_result_positive = positive_numbers[-2] * positive_numbers[-3] if len(positive_numbers) >= 3 else -1

		return max(partial_result_negative, partial_result_positive) * positive_numbers[-1]
		

print(maximum_product_of_three([-4, -4, 2, 8]))
# 128
