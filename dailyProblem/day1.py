class Solution:
	def lengthOfLongestSubstring(self, s):

		DEBUG = False # flag to print informations to debug during the process

		dic = {}
		maxLen = 0
		currentLen = 0
		startIndex = 0

		if DEBUG: 
			maxSub = ""
			currentSub = ""
			print(f"String: {s}")

		# for each letter in s
		for i in range(len(s)): 

			# if this letter is already in our substring
			if (s[i] in dic) and (dic[s[i]] >= startIndex): 

				if DEBUG: print(f"Repeated letter {s[i]}")

				# finish this substring and update the maxLen
				if(currentLen > maxLen):
					maxLen = currentLen
					if DEBUG: maxSub = currentSub

				# Create a new substring starting after the last ocurrency of the letter 
				currentLen = i - dic[s[i]]
				startIndex = dic[s[i]] + 1
				dic[s[i]] = i

				if DEBUG: 
					currentSub = s[startIndex:i+1]
					print(f"{currentSub} ... {currentLen}")

			# else, if this is a new letter, just add it to the substring
			else:
				currentLen += 1
				dic[s[i]] = i

				if DEBUG: 
					currentSub += s[i]
					print(f"{currentSub} ... {currentLen}")

		# last check maxLen 
		if(currentLen > maxLen):
			maxLen = currentLen
			if DEBUG: maxSub = currentSub

		return maxLen


print(Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))