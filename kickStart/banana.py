def add_to_dictionary(trees, i, j, qty_bunches):
	qty_trees = j - i + 1
	t = (qty_trees, i, j) 
	current_bunches_list = trees.get(qty_bunches, [])
	current_bunches_list.append(t)
	trees[qty_bunches] = current_bunches_list


def create_sorted_dictionary(N, K, B):
	# preprocessing, building a dictionary
	# keys are number of bunches and values area a tuple
	# in which the tuple = (number of trees, first tree included, last tree included)
	
	trees = {}

	for i in range(N):
		qty_bunches = B[i]

		if qty_bunches <= K:
			add_to_dictionary(trees, i, i, qty_bunches)

			for j in range(i+1, N):
				qty_bunches += B[j]

				if qty_bunches <= K:
					add_to_dictionary(trees, i, j, qty_bunches)
				else:
					break

	# Sorting the dictionary
	for qty_bunches in trees:
		trees[qty_bunches] = sorted(trees[qty_bunches], key=lambda x: x[0]) # same as trees[i].sort()

	return trees


def find_solution(N, K, trees):
	min_qty_trees = N+1

	for qty_bunches in trees:
		current_bunches_list = trees[qty_bunches]
		if qty_bunches == K:
			min_qty_trees = min(min_qty_trees, current_bunches_list[0][0])
		else:
			remaining_bunches = K - qty_bunches

			for t1 in current_bunches_list:
				remaining_list = trees.get(remaining_bunches, None)
				if remaining_list != None:
					for t2 in remaining_list:
						if t1[1] > t2[2] or t2[1] > t1[2]:
							current_qty_trees = t1[0] + t2[0]
							min_qty_trees = min(min_qty_trees, current_qty_trees)
							break

	if min_qty_trees > N:
		min_qty_trees = -1

	return min_qty_trees


### MAIN

T = int(input())

for t in range(T):
	N, K = map(int, input().split())
	B = list(map(int, input().split()))

	## Building dictionary
	trees = create_sorted_dictionary(N, K, B)
	
	## Finding the solution
	min_qty_trees = find_solution(N, K, trees)

	print(f"Case #{t+1}: {min_qty_trees}")
