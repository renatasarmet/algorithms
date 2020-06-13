class Solution: 

	def binarySearch(self, arr, start, end, target):
		size = len(arr[start:end])

		if (size == 0):
			return (-1)

		mid = start + (size // 2)

		if(arr[mid] == target):
			return (mid)
		elif(arr[mid] > target):
			return self.binarySearch(arr, start, mid, target)
		else:
			return self.binarySearch(arr, mid+1, end, target)


	def getRange(self, arr, target):
		# Find any occurrence
		midTarget = self.binarySearch(arr, 0, len(arr), target)

		if(midTarget != -1):
			first = midTarget
			last = midTarget

			# To find the first occurrence, start from midTarget and go left
			for i in range(midTarget-1, -1, -1):
				if arr[i] != target:
					first = i + 1
					break

			# To find the last occurrence, start from midTarget and go right
			for i in range(midTarget+1, len(arr)):
				if arr[i] != target:
					last = i - 1
					break
		else:
			first = -1
			last = -1

		return [first,last]
    # Fill this in.
  
# Test program 
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8] 
x = 2
print(Solution().getRange(arr, x))
# [1, 4]
