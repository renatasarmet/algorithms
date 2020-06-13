class Solution:
	def isPair(self, last, new):
		if last == "(" and new == ")":
			return True
		elif last == "[" and new == "]":
			return True
		elif last == "{" and new == "}":
			return True
		return False

	def isValid(self, s):
		stack = []
		for p in s:
			if p == "(" or p == "[" or p == "{":
				stack.append(p)
			else:
				last = stack.pop()
				if not self.isPair(last,p):
					return False

		if len(stack) > 0:
			return False
		return True



# Test Program
s = "()(){(())" 
# should return False
print(Solution().isValid(s))

s = ""
# should return True
print(Solution().isValid(s))

s = "([{}])()"
# should return True
print(Solution().isValid(s))