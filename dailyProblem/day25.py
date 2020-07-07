def witnesses(heights):
	if len(heights) == 0:
		return 0

	max_height = heights[-1]
	qty_people = 1

	for i in range(len(heights)-2,-1,-1):
		if heights[i] > max_height:
			max_height = heights[i]
			qty_people += 1

	return qty_people


print(witnesses([3, 6, 3, 4, 1]))
# 3
