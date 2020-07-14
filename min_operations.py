
# You have to find the minimum number of operations to n to find 1
# op:
# -> 1: subtract 1
# -> 2: divide by 2
# -> 3: divide by 3

from collections import deque

def apply_op(node, op):
	if op == 3:
		return (node[0]/3, node[1]+1) if node[0] % 3 == 0 else None
	elif op == 2:
		return (node[0]/2, node[1]+1) if node[0] % 2 == 0 else None
	else:
		return (node[0]-1, node[1]+1)


def findNumber(n, operations):

	if n <= 0: # if we just have those 3 operations, we can never find 1 starting before that
		return None

	queue = deque([(n,0)])

	while queue:
		head = queue.popleft()
		if head[0] == 1:
			return head[1]

		for op in operations:
			new_node = apply_op(head, op)

			if new_node:
				queue.append(new_node)

	return None # return head[1]


operations = [1,2,3]
print(findNumber(10, operations))
# 3
