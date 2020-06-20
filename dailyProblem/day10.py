class Node:
	def __init__(self, value):
		self.left = None
		self.right = None
		self.value = value


def findCeilingFloor(root_node, k, floor=None, ceil=None):
	if root_node.value == k:
		return (root_node.value, root_node.value)
	elif root_node.value > k:
		if(root_node.left):
			return(findCeilingFloor(root_node.left, k, floor=root_node.value, ceil=root_node.value))
		else:
			return(floor,root_node.value)
	else:
		if(root_node.right):
			return(findCeilingFloor(root_node.right, k, floor=root_node.value, ceil=root_node.value))
		else:
			return(root_node.value,ceil)


root = Node(8) 
root.left = Node(4) 
root.right = Node(12) 
  
root.left.left = Node(2) 
root.left.right = Node(6) 
  
root.right.left = Node(10) 
root.right.right = Node(14) 

print(findCeilingFloor(root, 5))
# (4, 6)
