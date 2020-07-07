class Node:
	def __init__(self, val, next=None):
		self.val = val
		self.next = next

	def __str__(self):
		current_node = self
		result = []
		while current_node:
			result.append(current_node.val)
			current_node = current_node.next
		return str(result)

def remove_kth_from_linked_list(head, k):
	current_node = head
	# check k next
	current_k_next_node = head
	count = 1
	while count <= k and current_k_next_node.next:
		current_k_next_node = current_k_next_node.next
		count += 1

	if count < k: # if the list is smaller than k
		return head
	elif count == k: # if we need to delete the first element of the list
		return head.next

	# keep searching
	while current_k_next_node is not None:
		last_node = current_node
		current_node = current_node.next
		current_k_next_node = current_k_next_node.next

	# remove current_node
	last_node.next = current_node.next

	return head


head = Node(1, Node(2, Node(3, Node(4, Node(5))))) # [1, 2, 4, 5]
# head = Node(1, Node(2, Node(3))) # [2, 3]
# head = Node(1, Node(2)) # [1, 2]

print(head)
# [1, 2, 3, 4, 5]
head = remove_kth_from_linked_list(head, 3)
print(head)
# [1, 2, 4, 5]
