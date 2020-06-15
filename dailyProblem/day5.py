class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None
  
	# Function to print the list
	def printList(self):
		node = self
		output = '' 
		while node != None:
			output += str(node.val)
			output += " "
			node = node.next
		print(output)


	# Iterative Solution
	def reverseIteratively(self, head):
		if(head):
			previous = head
			node = head.next
			head.next = None
			while node != None:
				future = node.next
				node.next = previous
				previous = node
				node = future


	# Recursive Solution      
	def reverseRecursively(self, head):
		if(head and head.next):
			self.reverseRecursively(head.next)
			head.next.next = head

		# I'm not sure if I can consider that always they will pass self = head. 
		# If I can assume that, just do this final check
		if head == self: 
			head.next = None
		# Else if I cannot assume that, I would implement an internal recursive function 
		# inside reverseRecursively (which would not be recursive, 
		# but would call the internal one - that contains the first 3 lines of this function -
		# and then assign None to head.next)


# Test Program
# Initialize the test list: 
testHead = ListNode(4)
node1 = ListNode(3)
testHead.next = node1
node2 = ListNode(2)
node1.next = node2
node3 = ListNode(1)
node2.next = node3
testTail = ListNode(0)
node3.next = testTail

print("Initial list: ")
testHead.printList()
# 4 3 2 1 0
testHead.reverseIteratively(testHead)
# testHead.reverseRecursively(testHead)
print("List after reversal: ")
testTail.printList()
# 0 1 2 3 4
