from collections import deque 

class Queue:
	def __init__(self):
		self.main_stack = deque()
		self.aux_stack = deque()
	
	def enqueue(self, val):
		# Move all elements from main_stack to aux_stack
		while self.main_stack:
			self.aux_stack.append(self.main_stack.pop())

		# Add val to main_stack
		self.main_stack.append(val)

		# Move all elements frmo aux_stack to main_stack
		while self.aux_stack:
			self.main_stack.append(self.aux_stack.pop())

	def dequeue(self):
		# Usual dequeue
		return self.main_stack.pop()


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
# 1 2 3
