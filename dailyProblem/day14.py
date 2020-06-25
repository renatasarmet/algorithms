def findPythagoreanTriplets(nums):
	squared = lambda x: x ** 2
	map_squares = map(squared, nums)
	nums = list(map_squares) # just to use the same memory
	set_squares = set(map_squares)

	for i in range(len(nums)):
		for j in range(i,len(nums)): # can we repeat the same number?
			if nums[i] + nums[j] in set_squares:
				return True

	return False


print findPythagoreanTriplets([3, 12, 5, 13])
# True
