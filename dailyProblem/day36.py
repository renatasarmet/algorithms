from collections import deque

class Node:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

	def __str__(self):
		# level-by-level pretty-printer
		nodes = deque([self])
		answer = ''
		while len(nodes):
			node = nodes.popleft()
			if not node:
				continue
			answer += str(node.value)
			nodes.append(node.left)
			nodes.append(node.right)
		return answer
		

def getNodeMid(nums):
	size = len(nums)
	if size == 0:
		return None

	mid = len(nums) // 2

	return Node(nums[mid], getNodeMid(nums[:mid]), getNodeMid(nums[mid+1:]))


def createBalancedBST(nums):
	nums.sort()
	return getNodeMid(nums)


print(createBalancedBST([1, 2, 3, 4, 5, 6, 7]))
# 4261357
#   4
#  / \
# 2   6
#/ \ / \
#1 3 5 7
