class MaxStack:
	def __init__(self):
		self.value = []
		self.max_num = []

	def push(self, val):
		self.value.append(val)
		if not self.max_num or val > self.max_num[-1]:
			self.max_num.append(val)
		else:
			self.max_num.append(self.max_num[-1])

	def pop(self):
		if self.value:
			self.value.pop()
			self.max_num.pop()

	def max(self):
		if self.max_num:
			return self.max_num[-1]
		else:
			return None


s = MaxStack()
s.push(1)
s.push(2)
s.push(3)
s.push(2)
print(s.max())
# 3
s.pop()
s.pop()
print(s.max())
# 2
