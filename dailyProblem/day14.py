def findPythagoreanTriplets(nums):
	nums = [x**2 for x in nums]
	set_squares = set(nums)

	for i in range(len(nums)):
		for j in range(i,len(nums)): # can we repeat the same number?
			if nums[i] + nums[j] in set_squares:
				return True

	return False


print(findPythagoreanTriplets([3, 12, 5, 13]))
# True
