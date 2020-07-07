def findKthLargest(nums, k):
	nums.sort()

	if k == 0 or len(nums) == 0:
		return None
	elif k == 1:
		return nums[-1]

	last_num = nums[-1]
	qty_num = 1

	for i in range(len(nums)-2,-1,-1):
		if nums[i] < last_num:
			last_num = nums[i]
			qty_num += 1
			if qty_num == k:
				return last_num

	return None

print(findKthLargest([3, 5, 2, 4, 6, 8], 3))
# 5
