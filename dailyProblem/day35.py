class Node(object):
	def __init__(self, val, next=None):
		self.val = val
		self.next = next

	def __str__(self):
		c = self
		answer = ""
		while c:
			answer += str(c.val) if c.val else ""
			answer += ' '
			c = c.next
		return answer


def findMinIndex(lists):
	min_index = 0
	for i in range(1,len(lists)):
		if lists[i].val < lists[min_index].val:
			min_index = i
	return min_index


def merge(lists):

	if len(lists) == 0:
		return None
	elif len(lists) == 1:
		return lists[0]

	# Get the first element 
	min_index = findMinIndex(lists)

	# Creating the root of the result node
	result = Node(lists[min_index].val)

	# Move the min_index
	lists[min_index] = lists[min_index].next

	if not lists[min_index]:
		del lists[min_index]

	current_node = result
	while lists:
		
		min_index = findMinIndex(lists)

		# Creating the root of the result node
		current_node.next = Node(lists[min_index].val)
		current_node = current_node.next

		# Move the min_index
		lists[min_index] = lists[min_index].next

		if not lists[min_index]:
			del lists[min_index]

	return result



a = Node(1, Node(3, Node(5)))
b = Node(2, Node(4, Node(6)))
c = Node(7, Node(8, Node(9,  Node(10,  Node(11)))))
print(merge([a, b, c]))
# 123456
