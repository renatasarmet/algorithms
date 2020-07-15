def capacity(arr):
	if len(arr) <= 1:
		return 0

	left_wall = 0
	total = 0

	# Stores the current height (counting the building or the water)
	heights = [0] * len(arr)
	heights[0] = arr[0]
	minimum_height = arr[0]

	for i in range(1,len(arr)):
		# Always going down
		if arr[i] < minimum_height:
			minimum_height = arr[i]
			heights[i] = arr[i]

		# If I find even a small wall
		elif arr[i] > minimum_height:
			heights[i] = arr[i]
			# from left wall to i-1, stablish new minimum_height
			for j in range(left_wall+1,i):
				new_height = min(arr[i],arr[left_wall])
				total += new_height - heights[j] 
				heights[j] = new_height
				minimum_height = arr[i]

			# If it's now the biggest
			if arr[i] >= arr[left_wall]:
				left_wall = i

	# print(heights)

	return total


print(capacity([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
#       X
#   X   XX X
#_X_XX_XXXXXX
# 6

print(capacity([2,0,1]))
# X
# X_X
# 1


print(capacity([2,0,1,2]))
# X  X
# X_XX
# 3

print(capacity([2,0,1,0,2]))
# X   X
# X_X_X
# 5

print(capacity([3,2,1]))
# X  
# XX 
# XXX
# 0
