NEGATIVE_INF = -1001

def divide_and_conquer(array):
	len_array = len(array)
	if len_array == 1:
		return array[0]

	mid = int(len_array/2)

	max_left = NEGATIVE_INF
	sum_value = 0
	for i in range(mid-1,-1,-1):
		sum_value += array[i]
		max_left = max(max_left, sum_value)

	max_right = NEGATIVE_INF
	sum_value = 0
	for i in range(mid,len_array,1):
		sum_value += array[i]
		max_right = max(max_right, sum_value)

	sum_mixed = max_left + max_right

	sum_1 = divide_and_conquer(array[:mid]) #left
	sum_2 = divide_and_conquer(array[mid:]) #right

	return max(sum_1, sum_2, sum_mixed)


n = int(input())
for i in range(n):
	len_array = int(input())
	array = list(map(int, input().split()))

	max_sum = divide_and_conquer(array)

	print("Soma maxima =", max_sum)
