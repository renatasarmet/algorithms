class Solution:
	def moveZeros(self, nums):
		last_index = 0

		for i in range(len(nums)):
			if nums[i] != 0:
				if last_index < i:
					nums[last_index] = nums[i]
					nums[i] = 0

				last_index += 1


nums = [0, 0, 0, 2, 0, 1, 3, 4, 0, 0]

Solution().moveZeros(nums)
print(nums)
# [2, 1, 3, 4, 0, 0, 0, 0, 0, 0]
