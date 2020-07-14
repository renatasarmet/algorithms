def max_subarray_sum(arr):
	if len(arr) == 0:
		return None

	max_sum = arr[0]
	current_sum = arr[0]

	for i in range(1,len(arr)):
		if current_sum >= 0:
			current_sum += arr[i]
		else:
			current_sum = arr[i]

		if current_sum > max_sum:
			max_sum = current_sum

	return max_sum


print(max_subarray_sum([34, -50, 42, 14, -5, 86]))
# 137
