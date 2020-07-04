class Solution:
	def minSubArrayLen(self, nums, s):

		min_len = len(nums) + 1
		dic_len = {} # for each index, store the length
		dic_value = {} # for each index, store the value of the sum until s

		for i in range(len(nums)):
			dic_len[i] = 0
			dic_value[i] = 0

			for j in list(dic_value):
				dic_value[j] += nums[i]
				dic_len[j] += 1

				if dic_len[j] < min_len:
					if dic_value[j] >= s:
						min_len = dic_len[j]

						# se ele ja for maior que a soma, posso parar de contar
						del dic_len[j]
						del dic_value[j]
				else:
					# se ele ja for maior que o tamanho, posso parar de contar
					del dic_len[j]
					del dic_value[j]

		return min_len if min_len <= len(nums) else 0

print(Solution().minSubArrayLen([2, 3, 1, 2, 4, 3], 7))
# 2
