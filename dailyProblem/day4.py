class Solution: 
	def getRange(self, arr, target):

		first = -1
		last = -1
		for i in range(len(arr)):
			if arr[i] == target:
				first = i
				break

		if first != -1:
			for i in range(len(arr)-1,0,-1):
				if arr[i] == target:
					last = i
					break
		

		return [first,last]
    # Fill this in.
  
# Test program 
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8] 
x = 2
print(Solution().getRange(arr, x))
# [1, 4]