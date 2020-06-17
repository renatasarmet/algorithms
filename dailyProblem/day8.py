def singleNumber(nums):
	nums.sort() # Sort the list
	repeated = True

	for i in range(len(nums)):
		if repeated:
			lastNumber = nums[i]
			repeated = False
		else:
			if nums[i] == lastNumber:
				repeated = True
			else:
				return nums[i-1]

	return nums[0] # when there is just 1 number

print(singleNumber([4, 3, 2, 4, 1, 3, 2]))
# 1