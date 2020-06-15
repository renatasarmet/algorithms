def sortNums(nums):
	# dictionaty that contains how many times each of those numbers appears in the list. It uses constant space.
	dic = {1: 0, 2: 0, 3: 0} 

	# count how many times each number appears
	for n in nums:
		dic[n] += 1

	# construct a new list with the right number of each number
	sortedList = []
	for i in dic:
		sortedList += [i] * dic[i]

	return sortedList



print(sortNums([3, 3, 2, 1, 3, 2, 1]))
# [1, 1, 2, 2, 3, 3, 3]
